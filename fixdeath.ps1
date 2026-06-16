param(
    [Parameter(Mandatory=$true,HelpMessage="The user that ran the file.")][Alias("U","User","Usr")][string]$Username,
    [Parameter(Mandatory=$true,HelpMessage="The drive letter of windows.")][Alias("D")][char]$Drive = "C"
)
del "$Drive\Users\$Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\death.bat"