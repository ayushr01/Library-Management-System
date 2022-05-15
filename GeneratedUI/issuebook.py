# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'issuebook.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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

class Ui_issuebookdialog(object):
    def setupUi(self, issuebookdialog):
        if not issuebookdialog.objectName():
            issuebookdialog.setObjectName(u"issuebookdialog")
        issuebookdialog.resize(500, 250)
        issuebookdialog.setMinimumSize(QSize(500, 250))
        issuebookdialog.setMaximumSize(QSize(500, 250))
        self.verticalLayout_2 = QVBoxLayout(issuebookdialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.memlist = QListWidget(issuebookdialog)
        self.memlist.setObjectName(u"memlist")
        font = QFont()
        font.setPointSize(13)
        self.memlist.setFont(font)
        self.memlist.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.memlist.setSpacing(2)

        self.horizontalLayout.addWidget(self.memlist)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.issuebutton = QPushButton(issuebookdialog)
        self.issuebutton.setObjectName(u"issuebutton")
        self.issuebutton.setMinimumSize(QSize(0, 45))
        self.issuebutton.setStyleSheet(u"QPushButton#issuebutton{\n"
"	background-color: FireBrick;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#issuebutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.verticalLayout.addWidget(self.issuebutton)

        self.closebutton = QPushButton(issuebookdialog)
        self.closebutton.setObjectName(u"closebutton")
        self.closebutton.setMinimumSize(QSize(0, 45))
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

        self.issuelabel = QLabel(issuebookdialog)
        self.issuelabel.setObjectName(u"issuelabel")
        font1 = QFont()
        font1.setBold(True)
        self.issuelabel.setFont(font1)
        self.issuelabel.setStyleSheet(u"color: orange;")

        self.verticalLayout_2.addWidget(self.issuelabel)

        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(issuebookdialog)

        QMetaObject.connectSlotsByName(issuebookdialog)
    # setupUi

    def retranslateUi(self, issuebookdialog):
        issuebookdialog.setWindowTitle(QCoreApplication.translate("issuebookdialog", u"Issue Book", None))
        self.issuebutton.setText(QCoreApplication.translate("issuebookdialog", u"Issue", None))
        self.closebutton.setText(QCoreApplication.translate("issuebookdialog", u"Close", None))
        self.issuelabel.setText("")
    # retranslateUi

