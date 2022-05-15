#!/bin/bash
rm -rfv pyinstaller
pyinstaller app.py -y --windowed --clean --name "LM System" --icon "icon.icns" --distpath "./pyinstaller/dist" --workpath "./pyinstaller/build" --add-data "Fonts:Fonts"

