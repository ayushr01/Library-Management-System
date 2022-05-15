from PySide6.QtWidgets import QApplication

from Utils.primarywindow import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
