[string]$inputString
$inputString = Read-Host "Please enter input string"
$inputstring.GetType().Name
$length= $inputString.Length

$start=0
$end=$length-1
$flag=$true

while($start -lt $end){
   if($inputString[$start] -ne $inputString[$end]){
   $flag=$false
   break
   }else{
   $start++
   $end--
   }
}

if($flag){
Write-Host "Given String is a palindrome"
}else{
Write-Host "Given String is not a palindrome"
}
