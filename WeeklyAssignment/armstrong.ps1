Write-Host "Enter the number"
[int]$number=Read-Host
[int]$len=0
[int]$temporaryNumber=$number
while($number -gt 0){
       $number=[Math]::Floor($number/10)
       $len++
}
$number=$temporaryNumber
[int]$sum=0
while($temporaryNumber -gt 0){
       $remainder= $temporaryNumber%10
       $temporaryNumber=[Math]::Floor($temporaryNumber/10)
       $product=1
       for($start=0; $start -lt ($len); $start++){
            $product*=$remainder
       }
       $sum+=$product
}

if($sum -eq $number){
  Write-Host "The number is a Armstrong number"
}else{
  Write-Host "The number is not a Armstrong number"
}
