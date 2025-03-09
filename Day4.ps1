$moduleName = Read-Host "Enter the name of Module that you want to install"

try {
    Install-Module -Name $moduleName -Force -Scope CurrentUser
    Write-Host "Module '$moduleName' installed successfully."
} catch {
    Write-Host "Failed to install module '$moduleName'. Error: $_"
    exit 1
}

try {
    Import-Module $moduleName -ErrorAction Stop
    Write-Host "Module '$moduleName' imported successfully."
} catch {
    Write-Host "Failed to import module '$moduleName'. Error: $_"
    exit 1
}
