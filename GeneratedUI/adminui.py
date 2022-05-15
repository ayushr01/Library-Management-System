# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading GeneratedUI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling GeneratedUI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(650, 450)
        AdminWindow.setMinimumSize(QSize(650, 450))
        AdminWindow.setMaximumSize(QSize(800, 600))
        self.verticalLayout = QVBoxLayout(AdminWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(AdminWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.memtab = QWidget()
        self.memtab.setObjectName(u"memtab")
        self.verticalLayout_2 = QVBoxLayout(self.memtab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.memtable = QTableWidget(self.memtab)
        if (self.memtable.columnCount() < 4):
            self.memtable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.memtable.setObjectName(u"memtable")
        self.memtable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.memtable.setSelectionMode(QAbstractItemView.NoSelection)
        self.memtable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.memtable.horizontalHeader().setVisible(True)
        self.memtable.horizontalHeader().setStretchLastSection(True)
        self.memtable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.memtable)

        self.membuttons = QHBoxLayout()
        self.membuttons.setObjectName(u"membuttons")
        self.addmem = QPushButton(self.memtab)
        self.addmem.setObjectName(u"addmem")
        self.addmem.setMinimumSize(QSize(0, 25))
        self.addmem.setStyleSheet(u"QPushButton#addmem{\n"
"	background-color: green;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#addmem:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.membuttons.addWidget(self.addmem)

        self.refreshmem = QPushButton(self.memtab)
        self.refreshmem.setObjectName(u"refreshmem")
        self.refreshmem.setMinimumSize(QSize(0, 25))
        self.refreshmem.setStyleSheet(u"QPushButton#refreshmem{\n"
"	background-color: cornflowerblue;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#refreshmem:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.membuttons.addWidget(self.refreshmem)

        self.deletemem = QPushButton(self.memtab)
        self.deletemem.setObjectName(u"deletemem")
        self.deletemem.setMinimumSize(QSize(0, 25))
        self.deletemem.setStyleSheet(u"QPushButton#deletemem{\n"
"	background-color: red;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#deletemem:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.membuttons.addWidget(self.deletemem)


        self.verticalLayout_2.addLayout(self.membuttons)

        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(1, 1)
        self.tabWidget.addTab(self.memtab, "")
        self.booktab = QWidget()
        self.booktab.setObjectName(u"booktab")
        self.verticalLayout_3 = QVBoxLayout(self.booktab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.booktable = QTableWidget(self.booktab)
        if (self.booktable.columnCount() < 6):
            self.booktable.setColumnCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        self.booktable.setObjectName(u"booktable")
        self.booktable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.booktable.setSelectionMode(QAbstractItemView.NoSelection)
        self.booktable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.booktable.horizontalHeader().setStretchLastSection(True)
        self.booktable.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.booktable)

        self.bookbuttons = QHBoxLayout()
        self.bookbuttons.setObjectName(u"bookbuttons")
        self.addbook = QPushButton(self.booktab)
        self.addbook.setObjectName(u"addbook")
        self.addbook.setMinimumSize(QSize(0, 25))
        self.addbook.setStyleSheet(u"QPushButton#addbook{\n"
"	background-color: green;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#addbook:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.bookbuttons.addWidget(self.addbook)

        self.refreshbook = QPushButton(self.booktab)
        self.refreshbook.setObjectName(u"refreshbook")
        self.refreshbook.setMinimumSize(QSize(0, 25))
        self.refreshbook.setStyleSheet(u"QPushButton#refreshbook{\n"
"	background-color: cornflowerblue;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#refreshbook:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.bookbuttons.addWidget(self.refreshbook)

        self.deletebook = QPushButton(self.booktab)
        self.deletebook.setObjectName(u"deletebook")
        self.deletebook.setMinimumSize(QSize(0, 25))
        self.deletebook.setStyleSheet(u"QPushButton#deletebook{\n"
"	background-color: red;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#deletebook:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.bookbuttons.addWidget(self.deletebook)


        self.verticalLayout_3.addLayout(self.bookbuttons)

        self.verticalLayout_3.setStretch(0, 8)
        self.verticalLayout_3.setStretch(1, 1)
        self.tabWidget.addTab(self.booktab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(AdminWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Admin", None))
        ___qtablewidgetitem = self.memtable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminWindow", u"ID", None));
        ___qtablewidgetitem1 = self.memtable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminWindow", u"Name", None));
        ___qtablewidgetitem2 = self.memtable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminWindow", u"DOB", None));
        ___qtablewidgetitem3 = self.memtable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminWindow", u"DOR", None));
        self.addmem.setText(QCoreApplication.translate("AdminWindow", u"Add", None))
        self.refreshmem.setText(QCoreApplication.translate("AdminWindow", u"Refresh", None))
        self.deletemem.setText(QCoreApplication.translate("AdminWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.memtab), QCoreApplication.translate("AdminWindow", u"Members", None))
        ___qtablewidgetitem4 = self.booktable.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdminWindow", u"ID", None));
        ___qtablewidgetitem5 = self.booktable.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdminWindow", u"Title", None));
        ___qtablewidgetitem6 = self.booktable.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AdminWindow", u"Author", None));
        ___qtablewidgetitem7 = self.booktable.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AdminWindow", u"Genre", None));
        ___qtablewidgetitem8 = self.booktable.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AdminWindow", u"Total", None));
        ___qtablewidgetitem9 = self.booktable.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AdminWindow", u"Issued", None));
        self.addbook.setText(QCoreApplication.translate("AdminWindow", u"Add", None))
        self.refreshbook.setText(QCoreApplication.translate("AdminWindow", u"Refresh", None))
        self.deletebook.setText(QCoreApplication.translate("AdminWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.booktab), QCoreApplication.translate("AdminWindow", u"Books", None))
    # retranslateUi

