# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/uifiles/deletemembers.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deletememdialog(object):
    def setupUi(self, deletememdialog):
        deletememdialog.setObjectName("deletememdialog")
        deletememdialog.resize(500, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deletememdialog.sizePolicy().hasHeightForWidth())
        deletememdialog.setSizePolicy(sizePolicy)
        deletememdialog.setMinimumSize(QtCore.QSize(500, 230))
        deletememdialog.setMaximumSize(QtCore.QSize(500, 230))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        deletememdialog.setFont(font)
        self.memlist = QtWidgets.QListWidget(deletememdialog)
        self.memlist.setGeometry(QtCore.QRect(10, 10, 341, 181))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.memlist.setFont(font)
        self.memlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.memlist.setObjectName("memlist")
        self.errorlabel = QtWidgets.QLabel(deletememdialog)
        self.errorlabel.setGeometry(QtCore.QRect(10, 200, 481, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.errorlabel.setFont(font)
        self.errorlabel.setStyleSheet("color: red")
        self.errorlabel.setText("")
        self.errorlabel.setObjectName("errorlabel")
        self.layoutWidget = QtWidgets.QWidget(deletememdialog)
        self.layoutWidget.setGeometry(QtCore.QRect(360, 10, 132, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.buttons = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setSpacing(10)
        self.buttons.setObjectName("buttons")
        self.deletebutton = QtWidgets.QPushButton(self.layoutWidget)
        self.deletebutton.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deletebutton.setFont(font)
        self.deletebutton.setStyleSheet("background-color : red;\n"
"color: white;")
        self.deletebutton.setObjectName("deletebutton")
        self.buttons.addWidget(self.deletebutton)
        self.closebutton = QtWidgets.QPushButton(self.layoutWidget)
        self.closebutton.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.closebutton.setFont(font)
        self.closebutton.setStyleSheet("")
        self.closebutton.setObjectName("closebutton")
        self.buttons.addWidget(self.closebutton)

        self.retranslateUi(deletememdialog)
        QtCore.QMetaObject.connectSlotsByName(deletememdialog)

    def retranslateUi(self, deletememdialog):
        _translate = QtCore.QCoreApplication.translate
        deletememdialog.setWindowTitle(_translate("deletememdialog", "Delete Members"))
        self.deletebutton.setText(_translate("deletememdialog", "Delete"))
        self.closebutton.setText(_translate("deletememdialog", "Close"))
