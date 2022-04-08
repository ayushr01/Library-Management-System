from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Utils.primarywindow import MainWindow

# Adds HiDPI support to the app
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
# https://doc.qt.io/qt-5/qt.html#HighDpiScaleFactorRoundingPolicy-enum


app = QApplication([])

window = MainWindow()
window.show()

app.exec_()

#######################
# Wriiten by: Ayush Rao
#######################
