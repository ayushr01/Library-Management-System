from PySide6.QtWidgets import QApplication

import UI.primarywindow

app = QApplication([])

# Sets base size font to be same on all platforms (Required for cross-platform)
font = app.font()
font.setPixelSize(13)
app.setFont(font)

window = UI.primarywindow.MainWindow()
window.show()

app.exec()
