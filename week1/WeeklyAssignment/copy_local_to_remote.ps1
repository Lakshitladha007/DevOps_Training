$sourceFile = "D:\text.txt"
$destinationPath = "C:\Users\Administrator\NewFile.txt"
$remoteComputer = "54.152.228.24"  
$cred=Get-Credential  

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

$session = New-PSSession -ComputerName $remoteComputer -Credential $cred

if($session){
Write-Host "Session created"
}else{
Write-Host "Session not created"
}

Copy-Item -Path $sourceFile -Destination $destinationPath -ToSession $session

Remove-PSSession -Session $session
