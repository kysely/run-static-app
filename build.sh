#!/bin/bash
clear
rm -rf dist
command -v pyinstaller || pip3 install pyinstaller

pyinstaller -F -i assets/app-icon.ico -n Run\ App --clean run_app.py
rm -rf build *.spec