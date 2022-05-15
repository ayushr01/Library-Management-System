from PySide6.QtWidgets import QApplication

import UI.primarywindow

app = QApplication([])

window = UI.primarywindow.MainWindow()
window.show()

app.exec()
