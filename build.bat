@echo off
cls
title "Building PassGen"
set name="pass_gen.spec"
pyinstaller  --noconfirm --clean %name%
rmdir /s /q build
pause
exit
