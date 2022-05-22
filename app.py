import os

from PySide6.QtGui import QFontDatabase, QIcon
from PySide6.QtWidgets import QApplication

import UI.primarywindow

app = QApplication([])

# Sets base size font to be same on all platforms (Required for cross-platform)
# Also setting Ubuntu font
home = os.path.dirname(__file__)
app.setWindowIcon(QIcon(home + "/Assets/icon.png"))
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-Italic.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-Black.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-BlackItalic.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-Bold.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-BoldItalic.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-Light.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-LightItalic.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-Medium.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-MediumItalic.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-Regular.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-Thin.ttf")
QFontDatabase.addApplicationFont(home + "/Assets/Roboto-ThinItalic.ttf")

font = app.font()
font.setFamily("Roboto")
font.setPixelSize(13)
app.setFont(font)

window = UI.primarywindow.MainWindow()
window.show()

app.exec()
