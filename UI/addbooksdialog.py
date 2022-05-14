# Form implementation generated from reading ui file 'UI/uifiles/addbooks.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_addbookdialog(object):
    def setupUi(self, addbookdialog):
        addbookdialog.setObjectName("addbookdialog")
        addbookdialog.resize(450, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(addbookdialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(addbookdialog)
        self.tabWidget.setObjectName("tabWidget")
        self.manual = QtWidgets.QWidget()
        self.manual.setObjectName("manual")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.manual)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputform = QtWidgets.QFormLayout()
        self.inputform.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.inputform.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputform.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputform.setContentsMargins(10, -1, 10, -1)
        self.inputform.setHorizontalSpacing(40)
        self.inputform.setVerticalSpacing(25)
        self.inputform.setObjectName("inputform")
        self.titlefield = QtWidgets.QLabel(self.manual)
        font = QtGui.QFont()
        font.setBold(True)
        self.titlefield.setFont(font)
        self.titlefield.setObjectName("titlefield")
        self.inputform.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.titlefield)
        self.authorfield = QtWidgets.QLabel(self.manual)
        font = QtGui.QFont()
        font.setBold(True)
        self.authorfield.setFont(font)
        self.authorfield.setObjectName("authorfield")
        self.inputform.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.authorfield)
        self.inputtitle = QtWidgets.QLineEdit(self.manual)
        self.inputtitle.setMinimumSize(QtCore.QSize(0, 30))
        self.inputtitle.setObjectName("inputtitle")
        self.inputform.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputtitle)
        self.inputauthor = QtWidgets.QLineEdit(self.manual)
        self.inputauthor.setMinimumSize(QtCore.QSize(0, 30))
        self.inputauthor.setObjectName("inputauthor")
        self.inputform.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputauthor)
        self.genrefield = QtWidgets.QLabel(self.manual)
        font = QtGui.QFont()
        font.setBold(True)
        self.genrefield.setFont(font)
        self.genrefield.setObjectName("genrefield")
        self.inputform.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.genrefield)
        self.totalfield = QtWidgets.QLabel(self.manual)
        font = QtGui.QFont()
        font.setBold(True)
        self.totalfield.setFont(font)
        self.totalfield.setObjectName("totalfield")
        self.inputform.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.totalfield)
        self.inputgenre = QtWidgets.QLineEdit(self.manual)
        self.inputgenre.setMinimumSize(QtCore.QSize(0, 30))
        self.inputgenre.setObjectName("inputgenre")
        self.inputform.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputgenre)
        self.inputtotal = QtWidgets.QLineEdit(self.manual)
        self.inputtotal.setMinimumSize(QtCore.QSize(0, 30))
        self.inputtotal.setObjectName("inputtotal")
        self.inputform.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputtotal)
        self.verticalLayout_2.addLayout(self.inputform)
        self.error = QtWidgets.QLabel(self.manual)
        font = QtGui.QFont()
        font.setBold(True)
        self.error.setFont(font)
        self.error.setStyleSheet("color: orange")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error.setObjectName("error")
        self.verticalLayout_2.addWidget(self.error)
        self.buttonlayout = QtWidgets.QHBoxLayout()
        self.buttonlayout.setObjectName("buttonlayout")
        self.clearbutton = QtWidgets.QPushButton(self.manual)
        self.clearbutton.setMinimumSize(QtCore.QSize(0, 25))
        self.clearbutton.setStyleSheet("QPushButton#clearbutton{\n"
"    background-color: cornflowerblue;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#clearbutton:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.clearbutton.setObjectName("clearbutton")
        self.buttonlayout.addWidget(self.clearbutton)
        self.submitbutton = QtWidgets.QPushButton(self.manual)
        self.submitbutton.setMinimumSize(QtCore.QSize(0, 25))
        self.submitbutton.setStyleSheet("QPushButton#submitbutton{\n"
"    background-color: green;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#submitbutton:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.submitbutton.setObjectName("submitbutton")
        self.buttonlayout.addWidget(self.submitbutton)
        self.closebutton = QtWidgets.QPushButton(self.manual)
        self.closebutton.setMinimumSize(QtCore.QSize(0, 25))
        self.closebutton.setStyleSheet("QPushButton#closebutton{\n"
"    background-color: #656565;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#closebutton:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.closebutton.setObjectName("closebutton")
        self.buttonlayout.addWidget(self.closebutton)
        self.verticalLayout_2.addLayout(self.buttonlayout)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.tabWidget.addTab(self.manual, "")
        self.isbn = QtWidgets.QWidget()
        self.isbn.setObjectName("isbn")
        self.tabWidget.addTab(self.isbn, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(addbookdialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(addbookdialog)

    def retranslateUi(self, addbookdialog):
        _translate = QtCore.QCoreApplication.translate
        addbookdialog.setWindowTitle(_translate("addbookdialog", "Add Members"))
        self.titlefield.setText(_translate("addbookdialog", "Title:"))
        self.authorfield.setText(_translate("addbookdialog", "Author:"))
        self.genrefield.setText(_translate("addbookdialog", "Genre:"))
        self.totalfield.setText(_translate("addbookdialog", "Total:"))
        self.clearbutton.setText(_translate("addbookdialog", "Clear"))
        self.submitbutton.setText(_translate("addbookdialog", "Submit"))
        self.closebutton.setText(_translate("addbookdialog", "Close"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manual), _translate("addbookdialog", "Manual Entry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.isbn), _translate("addbookdialog", "Search using ISBN"))
