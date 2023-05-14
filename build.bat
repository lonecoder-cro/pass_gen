@echo off
cls
rem mode con cols=60 lines=10
title "building CroKeyGen"
set name="crokeygen.spec"
pyinstaller  --noconfirm --clean %name%
rmdir /s /q build
pause
exit
