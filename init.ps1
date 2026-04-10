# init.ps1 — Initialize the local development environment for Solus Prerelease.
#
# Usage:
#   .\init.ps1
#
# This script creates a Python virtual environment in .venv, then installs
# project dependencies from requirements.txt.  Run it once after cloning.

param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$VenvDir   = Join-Path $ScriptDir '.venv'

# Locate a Python 3 interpreter.
$PythonExe = $null
foreach ($candidate in @('python', 'python3', 'py')) {
    try {
        $ver = & $candidate --version 2>&1
        if ($ver -match 'Python 3') {
            $PythonExe = $candidate
            break
        }
    } catch {
        # candidate not found — try the next one
    }
}

if (-not $PythonExe) {
    Write-Error 'Python 3 was not found on PATH.  Install Python 3.12 or later and try again.'
    exit 1
}

# Create the virtual environment if it does not already exist.
if (-not (Test-Path $VenvDir)) {
    Write-Host "Creating virtual environment at $VenvDir ..."
    & $PythonExe -m venv $VenvDir
}

# Determine paths inside the venv.
$VenvPython = Join-Path $VenvDir 'Scripts' 'python.exe'
$VenvPip    = Join-Path $VenvDir 'Scripts' 'pip.exe'

# Install / refresh dependencies.
$ReqFile = Join-Path $ScriptDir 'requirements.txt'
if (Test-Path $ReqFile) {
    Write-Host 'Installing dependencies from requirements.txt ...'
    & $VenvPip install --upgrade pip --quiet
    & $VenvPip install -r $ReqFile --quiet
}

Write-Host ''
Write-Host 'Environment ready.  Activate it with:'
Write-Host "  $VenvDir\Scripts\Activate.ps1"
