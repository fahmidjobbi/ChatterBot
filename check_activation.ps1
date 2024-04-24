if ($env:VIRTUAL_ENV) {
    Write-Host "Virtual environment is activated: $($env:VIRTUAL_ENV)"
} else {
    Write-Host "Virtual environment is not activated"
}

#activate my virtual env windows 
#virtualenv -p  C:/Users/dell/Desktop/Deeper_ChatBot/python3.8/python.exe myenv
#.\myenv\Scripts\Activate
#.\check_activation.ps1  
