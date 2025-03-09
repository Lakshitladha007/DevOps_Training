Write-Host "Enter input string"
$inputString=Read-Host
Write-Host "Enter character"
$character=Read-Host

$start=0
$end=$inputString.Length
$countOccurence=0

while($start -lt $end){
    if($inputString[$start] -eq $character){
       $countOccurence++
    }
    $start++;
}

Write-Host "The occurences of $character is: $countOccurence"
