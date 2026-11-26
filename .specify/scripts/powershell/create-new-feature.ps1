#!/usr/bin/env pwsh
# Create a new feature
[CmdletBinding()]
param(
    [switch]$Json,
    [string]$ShortName,
    [int]$Number = 0,
    [switch]$Help,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$FeatureDescription
)
$ErrorActionPreference = 'Stop'

# Show help if requested
if ($Help) {
    Write-Host 'Usage: ./create-new-feature.ps1 [-Json] [-ShortName <name>] [-Number N] <feature description>'
    Write-Host ""
    Write-Host 'Options:'
    Write-Host '  -Json               Output in JSON format'
    Write-Host '  -ShortName <name>   Provide a custom short name for the branch (2-4 words)'
    Write-Host '  -Number N           Manually specify the branch number (overrides auto-detection)'
    Write-Host '  -Help               Show this help information'
    Write-Host ""
    Write-Host 'Examples:'
    Write-Host "  ./create-new-feature.ps1 'Add user authentication system' -ShortName 'user-auth'"
    Write-Host "  ./create-new-feature.ps1 'Implement OAuth2 integration for API'"
    exit 0
}

# Check if feature description provided
if (-not $FeatureDescription -or $FeatureDescription.Count -eq 0) {
    Write-Error 'Usage: ./create-new-feature.ps1 [-Json] [-ShortName <name>] <feature description>'
    exit 1
}

$featureDesc = ($FeatureDescription -join ' ').Trim()

# Resolve the repository root: prefer Git information; otherwise fall back to
# project-marker discovery so that repos initialized with --no-git still work.
function Find-RepositoryRoot {
    param(
        [string]$StartDir,
        [string[]]$Markers = @('.git', '.specify')
    )
    $current = Resolve-Path $StartDir
    while ($true) {
        foreach ($marker in $Markers) {
            if (Test-Path (Join-Path $current $marker)) {
                return $current
            }
        }
        $parent = Split-Path $current -Parent
        if ($parent -eq $current) {
            # Reached the filesystem root without finding a marker
            return $null
        }
        $current = $parent
    }
}

function Get-NextBranchNumber {
    param(
        [string]$ShortName,
        [string]$SpecsDir
    )
    
    # Fetch all remotes to get the latest branch info (ignore errors when there are no remotes)
    try {
        git fetch --all --prune 2>$null | Out-Null
    } catch {
        # Ignore fetch errors
    }
    
    # Use git ls-remote to find remote branches matching the pattern
    $remoteBranches = @()
    try {
        $remoteRefs = git ls-remote --heads origin 2>$null
        if ($remoteRefs) {
            $remoteBranches = $remoteRefs | Where-Object { $_ -match "refs/heads/(\d+)-$([regex]::Escape($ShortName))$" } | ForEach-Object {
                if ($_ -match "refs/heads/(\d+)-") {
                    [int]$matches[1]
                }
            }
        }
    } catch {
        # Ignore errors
    }
    
    # Check local branches
    $localBranches = @()
    try {
        $allBranches = git branch 2>$null
        if ($allBranches) {
            $localBranches = $allBranches | Where-Object { $_ -match "^\*?\s*(\d+)-$([regex]::Escape($ShortName))$" } | ForEach-Object {
                if ($_ -match "(\d+)-") {
                    [int]$matches[1]
                }
            }
        }
    } catch {
        # Ignore errors
    }
    
    # Check the specs directory
    $specDirs = @()
    if (Test-Path $SpecsDir) {
        try {
            $specDirs = Get-ChildItem -Path $SpecsDir -Directory | Where-Object { $_.Name -match "^(\d+)-$([regex]::Escape($ShortName))$" } | ForEach-Object {
                if ($_.Name -match "^(\d+)-") {
                    [int]$matches[1]
                }
            }
        } catch {
            # Ignore errors
        }
    }
    
    # Merge all sources and get the highest number
    $maxNum = 0
    foreach ($num in ($remoteBranches + $localBranches + $specDirs)) {
        if ($num -gt $maxNum) {
            $maxNum = $num
        }
    }
    
    # Return the next number
    return $maxNum + 1
}
$fallbackRoot = (Find-RepositoryRoot -StartDir $PSScriptRoot)
if (-not $fallbackRoot) {
    Write-Error 'Error: could not determine the repository root. Run this script from inside the repository.'
    exit 1
}

try {
    $repoRoot = git rev-parse --show-toplevel 2>$null
    if ($LASTEXITCODE -eq 0) {
        $hasGit = $true
    } else {
        throw "Git not available"
    }
} catch {
    $repoRoot = $fallbackRoot
    $hasGit = $false
}

Set-Location $repoRoot

$specsDir = Join-Path $repoRoot 'specs'
New-Item -ItemType Directory -Path $specsDir -Force | Out-Null

# Generate the branch name (with stop-word filtering and length control)
function Get-BranchName {
    param([string]$Description)
    
    # Common stop words (to be filtered out)
    $stopWords = @(
        'i', 'a', 'an', 'the', 'to', 'for', 'of', 'in', 'on', 'at', 'by', 'with', 'from',
        'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
        'do', 'does', 'did', 'will', 'would', 'should', 'could', 'can', 'may', 'might', 'must', 'shall',
        'this', 'that', 'these', 'those', 'my', 'your', 'our', 'their',
        'want', 'need', 'add', 'get', 'set'
    )
    
    # Lowercase and extract words (alphanumeric only)
    $cleanName = $Description.ToLower() -replace '[^a-z0-9\s]', ' '
    $words = $cleanName -split '\s+' | Where-Object { $_ }
    
    # Filter words: drop stop words and words shorter than 3 characters (unless they were all-caps acronyms in the original description)
    $meaningfulWords = @()
    foreach ($word in $words) {
        # Skip stop words
        if ($stopWords -contains $word) { continue }
        
        # Keep words of length >= 3, or words that appeared in all caps in the original description (possibly acronyms)
        if ($word.Length -ge 3) {
            $meaningfulWords += $word
        } elseif ($Description -match "\b$($word.ToUpper())\b") {
            # If the original description had it in all caps (possibly an acronym), keep the short word
            $meaningfulWords += $word
        }
    }
    
    # If there are meaningful words, take the first 3-4 to form the short name
    if ($meaningfulWords.Count -gt 0) {
        $maxWords = if ($meaningfulWords.Count -eq 4) { 4 } else { 3 }
        $result = ($meaningfulWords | Select-Object -First $maxWords) -join '-'
        return $result
    } else {
        # If there are no meaningful words, fall back to the original logic
        $result = $Description.ToLower() -replace '[^a-z0-9]', '-' -replace '-{2,}', '-' -replace '^-', '' -replace '-$', ''
        $fallbackWords = ($result -split '-') | Where-Object { $_ } | Select-Object -First 3
        return [string]::Join('-', $fallbackWords)
    }
}

# Generate the branch name
if ($ShortName) {
    # Use the supplied short name and sanitize it
    $branchSuffix = $ShortName.ToLower() -replace '[^a-z0-9]', '-' -replace '-{2,}', '-' -replace '^-', '' -replace '-$', ''
} else {
    # Generate the short name from the description (smart filtering)
    $branchSuffix = Get-BranchName -Description $featureDesc
}

# Determine the branch number
if ($Number -eq 0) {
    if ($hasGit) {
        # Check existing remote branches
        $Number = Get-NextBranchNumber -ShortName $branchSuffix -SpecsDir $specsDir
    } else {
        # Fall back to checking the local directory
        $highest = 0
        if (Test-Path $specsDir) {
            Get-ChildItem -Path $specsDir -Directory | ForEach-Object {
                if ($_.Name -match '^(\d{3})') {
                    $num = [int]$matches[1]
                    if ($num -gt $highest) { $highest = $num }
                }
            }
        }
        $Number = $highest + 1
    }
}

$featureNum = ('{0:000}' -f $Number)
$branchName = "$featureNum-$branchSuffix"

# GitHub enforces a 244-byte limit on branch names; truncate if exceeded
$maxBranchLength = 244
if ($branchName.Length -gt $maxBranchLength) {
    # Calculate how much of the suffix to keep (feature number 3 + hyphen 1 = 4)
    $maxSuffixLength = $maxBranchLength - 4
    
    # Truncate the suffix
    $truncatedSuffix = $branchSuffix.Substring(0, [Math]::Min($branchSuffix.Length, $maxSuffixLength))
    # Remove a trailing hyphen left by truncation
    $truncatedSuffix = $truncatedSuffix -replace '-$', ''
    
    $originalBranchName = $branchName
    $branchName = "$featureNum-$truncatedSuffix"
    
        Write-Warning "[specify] Warning: branch name exceeds GitHub's 244-byte limit"
        Write-Warning "[specify] Original: $originalBranchName ($($originalBranchName.Length) bytes)"
        Write-Warning "[specify] Truncated to: $branchName ($($branchName.Length) bytes)"
}

if ($hasGit) {
    try {
        git checkout -b $branchName | Out-Null
    } catch {
        Write-Warning ('Failed to create Git branch: {0}' -f $branchName)
    }
} else {
    Write-Warning ('[specify] Warning: no Git repository detected; skipped branch creation: {0}' -f $branchName)
}

$featureDir = Join-Path $specsDir $branchName
New-Item -ItemType Directory -Path $featureDir -Force | Out-Null

$template = Join-Path $repoRoot '.specify/templates/spec-template.md'
$specFile = Join-Path $featureDir 'spec.md'
if (Test-Path $template) { 
    Copy-Item $template $specFile -Force 
} else { 
    New-Item -ItemType File -Path $specFile | Out-Null 
}

# Set the SPECIFY_FEATURE environment variable for the current session
$env:SPECIFY_FEATURE = $branchName

if ($Json) {
    $obj = [PSCustomObject]@{ 
        BRANCH_NAME = $branchName
        SPEC_FILE = $specFile
        FEATURE_NUM = $featureNum
        HAS_GIT = $hasGit
    }
    $obj | ConvertTo-Json -Compress
} else {
    Write-Output ('Branch name: {0}' -f $branchName)
    Write-Output ('Spec file: {0}' -f $specFile)
    Write-Output ('Feature number: {0}' -f $featureNum)
    Write-Output ('Has Git: {0}' -f $hasGit)
    Write-Output ('Set SPECIFY_FEATURE environment variable to: {0}' -f $branchName)
}
