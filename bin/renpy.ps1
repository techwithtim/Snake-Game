param(
    [string] $Command = "run"
)
$RenPy = Get-Content (Resolve-Path ".renpy-sdk")
$RenPy = [string]::join("", ($RenPy.Split("`n")))

if ($IsWindows -or $IsLinux -or $IsMacOS) {
    if ($IsWindows) {
        Write-Output "Renpy will run on a Windows system"
        Write-Output "Using Ren'Py SDK: $RenPy\renpy.exe"
        Start-Process -FilePath "$RenPy\renpy.exe" -ArgumentList ". $Command" -Wait
    }
    if ($IsLinux) {
        Write-Output "Renpy will run on a Linux system"
        Write-Output "Using Ren'Py SDK: $RenPy/renpy.sh"
        Start-Process -FilePath "$RenPy/renpy.sh" -ArgumentList ". $Command" -Wait
    }
    if ($IsMacOS) {
        Write-Output "Renpy will run on a MacOS system"
        Write-Output "Using Ren'Py SDK: $RenPy/renpy.sh"
        Start-Process -FilePath "$RenPy/renpy.sh" -ArgumentList ". $Command" -Wait
    }
} 
else {
    Write-Output "Renpy will run on an unknown system, may not work"
    Write-Output "Using Ren'Py SDK: $RenPy/renpy.sh"
    Start-Process -FilePath "$RenPy/renpy.sh" -ArgumentList ". $Command" -Wait
}

