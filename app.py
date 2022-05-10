from PyQt6.QtWidgets import QApplication

from Utils.primarywindow import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()

# TODO: Revamp all ui files to support responsive design
# TODO: Add ability to search for book details online
# TODO: Find better alternative for password storing
# TODO: Fix MacOS bundling

#######################
# Wriiten by: Ayush Rao
#######################
