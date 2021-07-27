# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/uifiles/myapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.issuetab = QtWidgets.QWidget()
        self.issuetab.setObjectName("issuetab")
        self.line = QtWidgets.QFrame(self.issuetab)
        self.line.setGeometry(QtCore.QRect(650, -40, 20, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.genrebox = QtWidgets.QComboBox(self.issuetab)
        self.genrebox.setGeometry(QtCore.QRect(680, 290, 291, 41))
        self.genrebox.setObjectName("genrebox")
        self.genrelabel = QtWidgets.QLabel(self.issuetab)
        self.genrelabel.setGeometry(QtCore.QRect(680, 250, 261, 31))
        self.genrelabel.setObjectName("genrelabel")
        self.viewmode = QtWidgets.QGroupBox(self.issuetab)
        self.viewmode.setGeometry(QtCore.QRect(670, 10, 271, 101))
        self.viewmode.setObjectName("viewmode")
        self.avaiablebooksbutton = QtWidgets.QRadioButton(self.viewmode)
        self.avaiablebooksbutton.setGeometry(QtCore.QRect(10, 30, 251, 28))
        self.avaiablebooksbutton.setObjectName("avaiablebooksbutton")
        self.allbooksbutton = QtWidgets.QRadioButton(self.viewmode)
        self.allbooksbutton.setGeometry(QtCore.QRect(10, 60, 251, 28))
        self.allbooksbutton.setObjectName("allbooksbutton")
        self.sortby = QtWidgets.QGroupBox(self.issuetab)
        self.sortby.setGeometry(QtCore.QRect(670, 110, 271, 131))
        self.sortby.setObjectName("sortby")
        self.titlebutton = QtWidgets.QRadioButton(self.sortby)
        self.titlebutton.setGeometry(QtCore.QRect(10, 30, 251, 28))
        self.titlebutton.setObjectName("titlebutton")
        self.authorbutton = QtWidgets.QRadioButton(self.sortby)
        self.authorbutton.setGeometry(QtCore.QRect(10, 60, 251, 28))
        self.authorbutton.setObjectName("authorbutton")
        self.ratingbutton = QtWidgets.QRadioButton(self.sortby)
        self.ratingbutton.setGeometry(QtCore.QRect(10, 90, 251, 28))
        self.ratingbutton.setObjectName("ratingbutton")
        self.layoutWidget = QtWidgets.QWidget(self.issuetab)
        self.layoutWidget.setGeometry(QtCore.QRect(687, 348, 271, 183))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.buttons = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setObjectName("buttons")
        self.refreshbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.refreshbutton.setMinimumSize(QtCore.QSize(0, 40))
        self.refreshbutton.setStyleSheet("background-color : purple;\n"
"color: white;")
        self.refreshbutton.setObjectName("refreshbutton")
        self.buttons.addWidget(self.refreshbutton)
        self.detailsbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.detailsbutton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailsbutton.setFont(font)
        self.detailsbutton.setStyleSheet("background-color : blue;\n"
"color: white;")
        self.detailsbutton.setObjectName("detailsbutton")
        self.buttons.addWidget(self.detailsbutton)
        self.issuebutton = QtWidgets.QPushButton(self.layoutWidget)
        self.issuebutton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.issuebutton.setFont(font)
        self.issuebutton.setStyleSheet("background-color : green;\n"
"color: white;")
        self.issuebutton.setObjectName("issuebutton")
        self.buttons.addWidget(self.issuebutton)
        self.adminbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.adminbutton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adminbutton.setFont(font)
        self.adminbutton.setStyleSheet("background-color : red;\n"
"color: white;")
        self.adminbutton.setObjectName("adminbutton")
        self.buttons.addWidget(self.adminbutton)
        self.booklist = QtWidgets.QListWidget(self.issuetab)
        self.booklist.setGeometry(QtCore.QRect(15, 11, 631, 491))
        self.booklist.setObjectName("booklist")
        self.errorlabel = QtWidgets.QLabel(self.issuetab)
        self.errorlabel.setGeometry(QtCore.QRect(14, 510, 631, 21))
        self.errorlabel.setStyleSheet("color: red")
        self.errorlabel.setText("")
        self.errorlabel.setObjectName("errorlabel")
        self.tabWidget.addTab(self.issuetab, "")
        self.deposittab = QtWidgets.QWidget()
        self.deposittab.setObjectName("deposittab")
        self.memberlabel = QtWidgets.QLabel(self.deposittab)
        self.memberlabel.setGeometry(QtCore.QRect(590, 10, 149, 41))
        self.memberlabel.setObjectName("memberlabel")
        self.idfield = QtWidgets.QLineEdit(self.deposittab)
        self.idfield.setGeometry(QtCore.QRect(750, 10, 211, 41))
        self.idfield.setObjectName("idfield")
        self.viewbookbutton = QtWidgets.QPushButton(self.deposittab)
        self.viewbookbutton.setGeometry(QtCore.QRect(590, 110, 371, 29))
        self.viewbookbutton.setObjectName("viewbookbutton")
        self.memlist = QtWidgets.QListWidget(self.deposittab)
        self.memlist.setGeometry(QtCore.QRect(10, 10, 551, 511))
        self.memlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.memlist.setObjectName("memlist")
        self.errorlabel_2 = QtWidgets.QLabel(self.deposittab)
        self.errorlabel_2.setGeometry(QtCore.QRect(590, 70, 371, 22))
        self.errorlabel_2.setStyleSheet("color: red\n"
"")
        self.errorlabel_2.setText("")
        self.errorlabel_2.setObjectName("errorlabel_2")
        self.line_2 = QtWidgets.QFrame(self.deposittab)
        self.line_2.setGeometry(QtCore.QRect(560, 200, 421, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.returnbutton = QtWidgets.QPushButton(self.deposittab)
        self.returnbutton.setGeometry(QtCore.QRect(690, 450, 171, 61))
        self.returnbutton.setObjectName("returnbutton")
        self.viewbookhistorybutton = QtWidgets.QPushButton(self.deposittab)
        self.viewbookhistorybutton.setGeometry(QtCore.QRect(590, 160, 371, 29))
        self.viewbookhistorybutton.setObjectName("viewbookhistorybutton")
        self.onestar = QtWidgets.QRadioButton(self.deposittab)
        self.onestar.setGeometry(QtCore.QRect(590, 270, 140, 28))
        self.onestar.setObjectName("onestar")
        self.twostar = QtWidgets.QRadioButton(self.deposittab)
        self.twostar.setGeometry(QtCore.QRect(590, 300, 140, 28))
        self.twostar.setObjectName("twostar")
        self.threestar = QtWidgets.QRadioButton(self.deposittab)
        self.threestar.setGeometry(QtCore.QRect(590, 330, 140, 28))
        self.threestar.setObjectName("threestar")
        self.fourstar = QtWidgets.QRadioButton(self.deposittab)
        self.fourstar.setGeometry(QtCore.QRect(590, 360, 140, 28))
        self.fourstar.setObjectName("fourstar")
        self.fivestar = QtWidgets.QRadioButton(self.deposittab)
        self.fivestar.setGeometry(QtCore.QRect(590, 390, 140, 28))
        self.fivestar.setObjectName("fivestar")
        self.ratinglabel = QtWidgets.QLabel(self.deposittab)
        self.ratinglabel.setGeometry(QtCore.QRect(590, 230, 371, 31))
        self.ratinglabel.setObjectName("ratinglabel")
        self.tabWidget.addTab(self.deposittab, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Management System"))
        self.genrelabel.setText(_translate("MainWindow", "Genre:"))
        self.viewmode.setTitle(_translate("MainWindow", "View mode:"))
        self.avaiablebooksbutton.setText(_translate("MainWindow", "Books available"))
        self.allbooksbutton.setText(_translate("MainWindow", "All books"))
        self.sortby.setTitle(_translate("MainWindow", "Sort by:"))
        self.titlebutton.setText(_translate("MainWindow", "Title"))
        self.authorbutton.setText(_translate("MainWindow", "Author"))
        self.ratingbutton.setText(_translate("MainWindow", "Rating"))
        self.refreshbutton.setText(_translate("MainWindow", "Refresh"))
        self.detailsbutton.setText(_translate("MainWindow", "Details"))
        self.issuebutton.setText(_translate("MainWindow", "Issue"))
        self.adminbutton.setText(_translate("MainWindow", "Admin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.issuetab), _translate("MainWindow", "Issue Book"))
        self.memberlabel.setText(_translate("MainWindow", "Enter Member ID:"))
        self.viewbookbutton.setText(_translate("MainWindow", "View books issued"))
        self.returnbutton.setText(_translate("MainWindow", "Return Book"))
        self.viewbookhistorybutton.setText(_translate("MainWindow", "View history of books issued"))
        self.onestar.setText(_translate("MainWindow", "⭐"))
        self.twostar.setText(_translate("MainWindow", "⭐⭐"))
        self.threestar.setText(_translate("MainWindow", "⭐⭐⭐"))
        self.fourstar.setText(_translate("MainWindow", "⭐⭐⭐⭐"))
        self.fivestar.setText(_translate("MainWindow", "⭐⭐⭐⭐⭐"))
        self.ratinglabel.setText(_translate("MainWindow", "Leave a rating for the book:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deposittab), _translate("MainWindow", "Deposit Book"))
