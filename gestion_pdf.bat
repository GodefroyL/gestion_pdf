@echo off
call "./venv\Scripts\activate.bat"
echo Environnement virtuel actif
call "./venv/Scripts/python.exe" main.py
echo Programme terminé
