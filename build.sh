#!/bin/bash
rm -rfv build
rm -rfv dist
pyinstaller app.py -y --windowed --clean --name "LM System" --icon "icon.icns"
