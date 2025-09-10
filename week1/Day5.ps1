$cred= Get-Credential

$remoteComputer="54.152.228.24"

Enable-PSRemoting -Force

$winrmService = Get-Service -Name winrm

if ($winrmService.Status -ne 'Running') {
    Write-Host "WinRM service is not running. Starting the service..."
    Start-Service -Name winrm
    Write-Host "WinRM service started successfully."
} else {
    Write-Host "WinRM service is already running."
}

Set-Item WSMan:\localhost\Client\TrustedHosts -Value $remoteComputer -Force

Enter-PSSession -ComputerName $remoteComputer -Credential $cred

Invoke-Command -ComputerName $remoteComputer -ScriptBlock { Get-Process } -Credential $cred
