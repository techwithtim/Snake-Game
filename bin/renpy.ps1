param(
    [string] $Command = "run"
)
$RenPy = Get-Content (Resolve-Path ".renpy-sdk")
$RenPy = [string]::join("", ($RenPy.Split("`n")))

Write-Output "Using Ren'Py SDK: $RenPy"
Start-Process -FilePath "$RenPy\renpy.exe" -ArgumentList ". $Command"
