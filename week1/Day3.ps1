param(
    [Parameter(Position=0, Mandatory=$true)]
    [string]$executionPolicy, 

    [Parameter(Position=1, Mandatory=$true)]
    [string]$policyScope
)

if($executionPolicy -eq "Unrestricted" -and $policyScope -eq "Process"){
    Set-ExecutionPolicy -ExecutionPolicy $executionPolicy -Scope $policyScope 
    Write-Host "Execution Policy set to $executionPolicy for scope $policyScope."
}else{
    Write-Host "Cannot set execution policy. since parameters are Invalid"
}
