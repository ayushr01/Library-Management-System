# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading GeneratedUI file 'deletebooks.ui'
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
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_deletebookdialog(object):
    def setupUi(self, deletebookdialog):
        if not deletebookdialog.objectName():
            deletebookdialog.setObjectName(u"deletebookdialog")
        deletebookdialog.resize(400, 200)
        deletebookdialog.setMinimumSize(QSize(400, 200))
        deletebookdialog.setMaximumSize(QSize(400, 200))
        self.verticalLayout_2 = QVBoxLayout(deletebookdialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.booklist = QListWidget(deletebookdialog)
        self.booklist.setObjectName(u"booklist")
        font = QFont()
        font.setPointSize(13)
        self.booklist.setFont(font)
        self.booklist.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.booklist.setSpacing(2)

        self.horizontalLayout.addWidget(self.booklist)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deletebutton = QPushButton(deletebookdialog)
        self.deletebutton.setObjectName(u"deletebutton")
        self.deletebutton.setMinimumSize(QSize(0, 35))
        self.deletebutton.setStyleSheet(u"QPushButton#deletebutton{\n"
"	background-color: red;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#deletebutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.verticalLayout.addWidget(self.deletebutton)

        self.closebutton = QPushButton(deletebookdialog)
        self.closebutton.setObjectName(u"closebutton")
        self.closebutton.setMinimumSize(QSize(0, 35))
        self.closebutton.setStyleSheet(u"QPushButton#closebutton{\n"
"	background-color: #656565;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#closebutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.verticalLayout.addWidget(self.closebutton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.errorlabel = QLabel(deletebookdialog)
        self.errorlabel.setObjectName(u"errorlabel")
        font1 = QFont()
        font1.setBold(True)
        self.errorlabel.setFont(font1)
        self.errorlabel.setStyleSheet(u"color: orange;")

        self.verticalLayout_2.addWidget(self.errorlabel)

        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(deletebookdialog)

        QMetaObject.connectSlotsByName(deletebookdialog)
    # setupUi

    def retranslateUi(self, deletebookdialog):
        deletebookdialog.setWindowTitle(QCoreApplication.translate("deletebookdialog", u"Delete Books", None))
        self.deletebutton.setText(QCoreApplication.translate("deletebookdialog", u"Delete", None))
        self.closebutton.setText(QCoreApplication.translate("deletebookdialog", u"Close", None))
        self.errorlabel.setText("")
    # retranslateUi

