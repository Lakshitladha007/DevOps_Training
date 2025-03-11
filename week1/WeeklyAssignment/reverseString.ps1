[string]$String
$String = Read-Host "Please enter input string"
$String.GetType().Name
$length= $String.Length
$inputString=$String.ToCharArray()

$start=0
$end=$length-1

while($start -lt $end){

   $temporaryCharacter=$inputString[$start]
   $inputString[$start]= $inputString[$end]
   $inputString[$end]=$temporaryCharacter
   
   $start++
   $end--
}

$String = [string]::new($inputString)
Write-Host "String after reversing is: $String"
