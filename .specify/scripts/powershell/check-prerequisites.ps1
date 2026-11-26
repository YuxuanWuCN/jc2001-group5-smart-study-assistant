#!/usr/bin/env pwsh

# Unified prerequisite validation script (PowerShell)
#
# Provides unified prerequisite validation for the Spec-Driven Development workflow.
# Replaces validation logic previously scattered across multiple scripts.
#
# Usage: ./check-prerequisites.ps1 [options]
#
# Options:
#   -Json               Output in JSON format
#   -RequireTasks       Require tasks.md to exist (implementation phase)
#   -IncludeTasks       Include tasks.md in the AVAILABLE_DOCS list
#   -PathsOnly          Only output path variables (do not run validation)
#   -Help, -h           Show help information

[CmdletBinding()]
param(
    [switch]$Json,
    [switch]$RequireTasks,
    [switch]$IncludeTasks,
    [switch]$PathsOnly,
    [switch]$Help
)

$ErrorActionPreference = 'Stop'

# Show help if requested
if ($Help) {
    Write-Output @"
Usage: check-prerequisites.ps1 [options]

Unified prerequisite validation for the Spec-Driven Development workflow.

Options:
  -Json               Output in JSON format
  -RequireTasks       Require tasks.md to exist (implementation phase)
  -IncludeTasks       Include tasks.md in the AVAILABLE_DOCS list
  -PathsOnly          Only output path variables (do not run validation)
  -Help, -h           Show help information

Examples:
  # Validate task phase prerequisites (plan.md required)
  .\check-prerequisites.ps1 -Json
  
  # Validate implementation phase prerequisites (plan.md + tasks.md required)
  .\check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
  
  # Only get feature paths (do not run validation)
  .\check-prerequisites.ps1 -PathsOnly

"@
    exit 0
}

# Load common functions
. "$PSScriptRoot/common.ps1"

# Get feature paths and validate the branch
$paths = Get-FeaturePathsEnv

if (-not (Test-FeatureBranch -Branch $paths.CURRENT_BRANCH -HasGit:$paths.HAS_GIT)) { 
    exit 1 
}

# Paths-only mode: output the paths and exit (JSON and -PathsOnly may be combined)
if ($PathsOnly) {
    if ($Json) {
        [PSCustomObject]@{
            REPO_ROOT    = $paths.REPO_ROOT
            BRANCH       = $paths.CURRENT_BRANCH
            FEATURE_DIR  = $paths.FEATURE_DIR
            FEATURE_SPEC = $paths.FEATURE_SPEC
            IMPL_PLAN    = $paths.IMPL_PLAN
            TASKS        = $paths.TASKS
        } | ConvertTo-Json -Compress
    } else {
        Write-Output "REPO_ROOT: $($paths.REPO_ROOT)"
        Write-Output "BRANCH: $($paths.CURRENT_BRANCH)"
        Write-Output "FEATURE_DIR: $($paths.FEATURE_DIR)"
        Write-Output "FEATURE_SPEC: $($paths.FEATURE_SPEC)"
        Write-Output "IMPL_PLAN: $($paths.IMPL_PLAN)"
        Write-Output "TASKS: $($paths.TASKS)"
    }
    exit 0
}

# Validate required directories and files
if (-not (Test-Path $paths.FEATURE_DIR -PathType Container)) {
    Write-Output ('Error: feature directory not found: {0}' -f $paths.FEATURE_DIR)
    Write-Output 'Run /speckit.specify first to create the feature directory structure.'
    exit 1
}

if (-not (Test-Path $paths.IMPL_PLAN -PathType Leaf)) {
    Write-Output ('Error: plan.md not found in {0}' -f $paths.FEATURE_DIR)
    Write-Output 'Run /speckit.plan first to generate the implementation plan.'
    exit 1
}

# Check for tasks.md if required
if ($RequireTasks -and -not (Test-Path $paths.TASKS -PathType Leaf)) {
    Write-Output ('Error: tasks.md not found in {0}' -f $paths.FEATURE_DIR)
    Write-Output 'Run /speckit.tasks first to create the task list.'
    exit 1
}

# Build the list of available documents
$docs = @()

# Always check these optional documents
if (Test-Path $paths.RESEARCH) { $docs += 'research.md' }
if (Test-Path $paths.DATA_MODEL) { $docs += 'data-model.md' }

# Check the contracts directory (when present and containing files)
if ((Test-Path $paths.CONTRACTS_DIR) -and (Get-ChildItem -Path $paths.CONTRACTS_DIR -ErrorAction SilentlyContinue | Select-Object -First 1)) { 
    $docs += 'contracts/' 
}

if (Test-Path $paths.QUICKSTART) { $docs += 'quickstart.md' }

# Include tasks.md if requested and present
if ($IncludeTasks -and (Test-Path $paths.TASKS)) { 
    $docs += 'tasks.md' 
}

# Output results
if ($Json) {
    # JSON output
    [PSCustomObject]@{ 
        FEATURE_DIR = $paths.FEATURE_DIR
        AVAILABLE_DOCS = $docs 
    } | ConvertTo-Json -Compress
} else {
    # Text output
    Write-Output ('Feature directory: {0}' -f $paths.FEATURE_DIR)
    Write-Output 'Available documents:'
    
    # Show status of each potential document
    Test-FileExists -Path $paths.RESEARCH -Description "research.md" | Out-Null
    Test-FileExists -Path $paths.DATA_MODEL -Description "data-model.md" | Out-Null
    Test-DirHasFiles -Path $paths.CONTRACTS_DIR -Description "contracts/" | Out-Null
    Test-FileExists -Path $paths.QUICKSTART -Description "quickstart.md" | Out-Null
    
    if ($IncludeTasks) {
        Test-FileExists -Path $paths.TASKS -Description "tasks.md" | Out-Null
    }
}
