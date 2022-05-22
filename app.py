import os

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication

import UI.primarywindow

app = QApplication([])

# Sets base size font to be same on all platforms (Required for cross-platform)
# Also setting Ubuntu font
home = os.path.dirname(__file__)
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-Italic.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-Black.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-BlackItalic.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-Bold.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-BoldItalic.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-Light.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-LightItalic.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-Medium.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-MediumItalic.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-Regular.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-Thin.ttf")
QFontDatabase.addApplicationFont(home + "/Fonts/Roboto-ThinItalic.ttf")

font = app.font()
font.setFamily("Roboto")
font.setPixelSize(13)
app.setFont(font)

window = UI.primarywindow.MainWindow()
window.show()

app.exec()
