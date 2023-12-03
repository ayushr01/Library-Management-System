rm -rfv pyinstaller
pyinstaller app.py -y --windowed --clean --name "LM System" --icon "icon.png" --distpath "./pyinstaller/dist" --workpath "./pyinstaller/build" --add-data "Assets:Assets"