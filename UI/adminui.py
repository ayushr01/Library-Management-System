# Form implementation generated from reading ui file 'UI/uifiles/admin.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(650, 450)
        AdminWindow.setMinimumSize(QtCore.QSize(650, 450))
        AdminWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(AdminWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(AdminWindow)
        self.tabWidget.setObjectName("tabWidget")
        self.memtab = QtWidgets.QWidget()
        self.memtab.setObjectName("memtab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.memtab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.memtable = QtWidgets.QTableWidget(self.memtab)
        self.memtable.setObjectName("memtable")
        self.memtable.setColumnCount(4)
        self.memtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(3, item)
        self.memtable.horizontalHeader().setVisible(True)
        self.memtable.horizontalHeader().setStretchLastSection(True)
        self.memtable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.memtable)
        self.membuttons = QtWidgets.QHBoxLayout()
        self.membuttons.setObjectName("membuttons")
        self.addmem = QtWidgets.QPushButton(self.memtab)
        self.addmem.setMinimumSize(QtCore.QSize(0, 25))
        self.addmem.setStyleSheet("QPushButton#addmem{\n"
"    background-color: green;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#addmem:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.addmem.setObjectName("addmem")
        self.membuttons.addWidget(self.addmem)
        self.refreshmem = QtWidgets.QPushButton(self.memtab)
        self.refreshmem.setMinimumSize(QtCore.QSize(0, 25))
        self.refreshmem.setStyleSheet("QPushButton#refreshmem{\n"
"    background-color: cornflowerblue;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#refreshmem:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.refreshmem.setObjectName("refreshmem")
        self.membuttons.addWidget(self.refreshmem)
        self.deletemem = QtWidgets.QPushButton(self.memtab)
        self.deletemem.setMinimumSize(QtCore.QSize(0, 25))
        self.deletemem.setStyleSheet("QPushButton#deletemem{\n"
"    background-color: red;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#deletemem:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.deletemem.setObjectName("deletemem")
        self.membuttons.addWidget(self.deletemem)
        self.verticalLayout_2.addLayout(self.membuttons)
        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(1, 1)
        self.tabWidget.addTab(self.memtab, "")
        self.booktab = QtWidgets.QWidget()
        self.booktab.setObjectName("booktab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.booktab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.booktable = QtWidgets.QTableWidget(self.booktab)
        self.booktable.setObjectName("booktable")
        self.booktable.setColumnCount(6)
        self.booktable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(5, item)
        self.booktable.horizontalHeader().setStretchLastSection(True)
        self.booktable.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.booktable)
        self.bookbuttons = QtWidgets.QHBoxLayout()
        self.bookbuttons.setObjectName("bookbuttons")
        self.addbook = QtWidgets.QPushButton(self.booktab)
        self.addbook.setMinimumSize(QtCore.QSize(0, 25))
        self.addbook.setStyleSheet("QPushButton#addbook{\n"
"    background-color: green;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#addbook:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.addbook.setObjectName("addbook")
        self.bookbuttons.addWidget(self.addbook)
        self.refreshbook = QtWidgets.QPushButton(self.booktab)
        self.refreshbook.setMinimumSize(QtCore.QSize(0, 25))
        self.refreshbook.setStyleSheet("QPushButton#refreshbook{\n"
"    background-color: cornflowerblue;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#refreshbook:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.refreshbook.setObjectName("refreshbook")
        self.bookbuttons.addWidget(self.refreshbook)
        self.deletebook = QtWidgets.QPushButton(self.booktab)
        self.deletebook.setMinimumSize(QtCore.QSize(0, 25))
        self.deletebook.setStyleSheet("QPushButton#deletebook{\n"
"    background-color: red;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#deletebook:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.deletebook.setObjectName("deletebook")
        self.bookbuttons.addWidget(self.deletebook)
        self.verticalLayout_3.addLayout(self.bookbuttons)
        self.verticalLayout_3.setStretch(0, 8)
        self.verticalLayout_3.setStretch(1, 1)
        self.tabWidget.addTab(self.booktab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(AdminWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Admin"))
        item = self.memtable.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "ID"))
        item = self.memtable.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Name"))
        item = self.memtable.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "DOB"))
        item = self.memtable.horizontalHeaderItem(3)
        item.setText(_translate("AdminWindow", "DOR"))
        self.addmem.setText(_translate("AdminWindow", "Add"))
        self.refreshmem.setText(_translate("AdminWindow", "Refresh"))
        self.deletemem.setText(_translate("AdminWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.memtab), _translate("AdminWindow", "Members"))
        item = self.booktable.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "ID"))
        item = self.booktable.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Title"))
        item = self.booktable.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "Author"))
        item = self.booktable.horizontalHeaderItem(3)
        item.setText(_translate("AdminWindow", "Genre"))
        item = self.booktable.horizontalHeaderItem(4)
        item.setText(_translate("AdminWindow", "Total"))
        item = self.booktable.horizontalHeaderItem(5)
        item.setText(_translate("AdminWindow", "Issued"))
        self.addbook.setText(_translate("AdminWindow", "Add"))
        self.refreshbook.setText(_translate("AdminWindow", "Refresh"))
        self.deletebook.setText(_translate("AdminWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.booktab), _translate("AdminWindow", "Books"))
