#!/usr/bin/env pwsh
# Set up the implementation plan for a feature

[CmdletBinding()]
param(
    [switch]$Json,
    [switch]$Help
)

$ErrorActionPreference = 'Stop'

# Show help if requested
if ($Help) {
    Write-Output 'Usage: ./setup-plan.ps1 [-Json] [-Help]'
    Write-Output '  -Json     Output results in JSON format'
    Write-Output '  -Help     Show this help information'
    exit 0
}

# Load common functions
. "$PSScriptRoot/common.ps1"

# Get all paths and variables from the common functions
$paths = Get-FeaturePathsEnv

# Check that we are on the correct feature branch (validated only inside Git repos)
if (-not (Test-FeatureBranch -Branch $paths.CURRENT_BRANCH -HasGit $paths.HAS_GIT)) { 
    exit 1 
}

# Ensure the feature directory exists
New-Item -ItemType Directory -Path $paths.FEATURE_DIR -Force | Out-Null

# Copy the plan template if it exists, otherwise warn and create an empty file
$template = Join-Path $paths.REPO_ROOT '.specify/templates/plan-template.md'
if (Test-Path $template) { 
    Copy-Item $template $paths.IMPL_PLAN -Force
    Write-Output ('Copied plan template to {0}' -f $paths.IMPL_PLAN)
} else {
    Write-Warning ('Plan template not found at {0}' -f $template)
    # Create a basic plan file if the template does not exist
    New-Item -ItemType File -Path $paths.IMPL_PLAN -Force | Out-Null
}

# Output results
if ($Json) {
    $result = [PSCustomObject]@{ 
        FEATURE_SPEC = $paths.FEATURE_SPEC
        IMPL_PLAN = $paths.IMPL_PLAN
        SPECS_DIR = $paths.FEATURE_DIR
        BRANCH = $paths.CURRENT_BRANCH
        HAS_GIT = $paths.HAS_GIT
    }
    $result | ConvertTo-Json -Compress
} else {
    Write-Output ('Spec file: {0}' -f $paths.FEATURE_SPEC)
    Write-Output ('Implementation plan: {0}' -f $paths.IMPL_PLAN)
    Write-Output ('Spec directory: {0}' -f $paths.FEATURE_DIR)
    Write-Output ('Current branch: {0}' -f $paths.CURRENT_BRANCH)
    Write-Output ('Has Git: {0}' -f $paths.HAS_GIT)
}
