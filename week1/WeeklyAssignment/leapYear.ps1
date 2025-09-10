$year = Read-Host "Enter a year"

if ($year % 4 -eq 0) {
    if ($year % 100 -eq 0) {
        if ($year % 400 -eq 0) {
            Write-Output "$year is a Leap Year."
        } else {
            Write-Output "$year is NOT a Leap Year."
        }
    } else {
        Write-Output "$year is a Leap Year."
    }
} else {
    Write-Output "$year is NOT a Leap Year."
}
