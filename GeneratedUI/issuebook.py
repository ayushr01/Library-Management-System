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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_issuebookdialog(object):
    def setupUi(self, issuebookdialog):
        if not issuebookdialog.objectName():
            issuebookdialog.setObjectName(u"issuebookdialog")
        issuebookdialog.resize(500, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(issuebookdialog.sizePolicy().hasHeightForWidth())
        issuebookdialog.setSizePolicy(sizePolicy)
        issuebookdialog.setMinimumSize(QSize(500, 230))
        issuebookdialog.setMaximumSize(QSize(500, 230))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        issuebookdialog.setFont(font)
        self.memlist = QListWidget(issuebookdialog)
        self.memlist.setObjectName(u"memlist")
        self.memlist.setGeometry(QRect(10, 10, 341, 181))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.memlist.setFont(font1)
        self.memlist.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.issuelabel = QLabel(issuebookdialog)
        self.issuelabel.setObjectName(u"issuelabel")
        self.issuelabel.setGeometry(QRect(10, 200, 481, 22))
        self.issuelabel.setFont(font)
        self.issuelabel.setStyleSheet(u"color: blue")
        self.layoutWidget = QWidget(issuebookdialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(360, 10, 132, 181))
        self.layoutWidget.setFont(font)
        self.buttons = QVBoxLayout(self.layoutWidget)
        self.buttons.setSpacing(10)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.issuebutton = QPushButton(self.layoutWidget)
        self.issuebutton.setObjectName(u"issuebutton")
        self.issuebutton.setMinimumSize(QSize(130, 50))
        self.issuebutton.setFont(font)
        self.issuebutton.setStyleSheet(u"background-color : #be8846;\n"
"color: white;")

        self.buttons.addWidget(self.issuebutton)

        self.closebutton = QPushButton(self.layoutWidget)
        self.closebutton.setObjectName(u"closebutton")
        self.closebutton.setMinimumSize(QSize(130, 50))
        self.closebutton.setFont(font)
        self.closebutton.setStyleSheet(u"background-color: #333333;\n"
"color: white;")

        self.buttons.addWidget(self.closebutton)


        self.retranslateUi(issuebookdialog)

        QMetaObject.connectSlotsByName(issuebookdialog)
    # setupUi

    def retranslateUi(self, issuebookdialog):
        issuebookdialog.setWindowTitle(QCoreApplication.translate("issuebookdialog", u"Issue Book", None))
        self.issuelabel.setText("")
        self.issuebutton.setText(QCoreApplication.translate("issuebookdialog", u"Issue", None))
        self.closebutton.setText(QCoreApplication.translate("issuebookdialog", u"Close", None))
    # retranslateUi

