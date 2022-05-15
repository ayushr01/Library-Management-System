# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading GeneratedUI file 'pwdnew.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_passworddialog(object):
    def setupUi(self, passworddialog):
        if not passworddialog.objectName():
            passworddialog.setObjectName(u"passworddialog")
        passworddialog.resize(400, 350)
        passworddialog.setMinimumSize(QSize(400, 350))
        passworddialog.setMaximumSize(QSize(400, 350))
        self.verticalLayout = QVBoxLayout(passworddialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info = QLabel(passworddialog)
        self.info.setObjectName(u"info")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.info.setFont(font)
        self.info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info)

        self.inputform = QFormLayout()
        self.inputform.setObjectName(u"inputform")
        self.inputform.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.inputform.setLabelAlignment(Qt.AlignCenter)
        self.inputform.setFormAlignment(Qt.AlignCenter)
        self.inputform.setHorizontalSpacing(40)
        self.inputform.setVerticalSpacing(25)
        self.inputform.setContentsMargins(10, -1, 10, -1)
        self.username = QLabel(passworddialog)
        self.username.setObjectName(u"username")
        font1 = QFont()
        font1.setBold(True)
        self.username.setFont(font1)

        self.inputform.setWidget(0, QFormLayout.LabelRole, self.username)

        self.password = QLabel(passworddialog)
        self.password.setObjectName(u"password")
        self.password.setFont(font1)

        self.inputform.setWidget(1, QFormLayout.LabelRole, self.password)

        self.userfield = QLineEdit(passworddialog)
        self.userfield.setObjectName(u"userfield")
        self.userfield.setMinimumSize(QSize(0, 30))

        self.inputform.setWidget(0, QFormLayout.FieldRole, self.userfield)

        self.pwdfield = QLineEdit(passworddialog)
        self.pwdfield.setObjectName(u"pwdfield")
        self.pwdfield.setMinimumSize(QSize(0, 30))
        self.pwdfield.setEchoMode(QLineEdit.Password)

        self.inputform.setWidget(1, QFormLayout.FieldRole, self.pwdfield)

        self.confirm = QLabel(passworddialog)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setFont(font1)

        self.inputform.setWidget(2, QFormLayout.LabelRole, self.confirm)

        self.pwdfieldconfirm = QLineEdit(passworddialog)
        self.pwdfieldconfirm.setObjectName(u"pwdfieldconfirm")
        self.pwdfieldconfirm.setMinimumSize(QSize(0, 30))
        self.pwdfieldconfirm.setEchoMode(QLineEdit.Password)

        self.inputform.setWidget(2, QFormLayout.FieldRole, self.pwdfieldconfirm)


        self.verticalLayout.addLayout(self.inputform)

        self.error = QLabel(passworddialog)
        self.error.setObjectName(u"error")
        self.error.setFont(font1)
        self.error.setStyleSheet(u"color: orange")
        self.error.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.error)

        self.buttonlayout = QHBoxLayout()
        self.buttonlayout.setObjectName(u"buttonlayout")
        self.clearbutton = QPushButton(passworddialog)
        self.clearbutton.setObjectName(u"clearbutton")
        self.clearbutton.setMinimumSize(QSize(0, 25))
        self.clearbutton.setStyleSheet(u"QPushButton#clearbutton{\n"
"	background-color: cornflowerblue;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#clearbutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.buttonlayout.addWidget(self.clearbutton)

        self.submitbutton = QPushButton(passworddialog)
        self.submitbutton.setObjectName(u"submitbutton")
        self.submitbutton.setMinimumSize(QSize(0, 25))
        self.submitbutton.setStyleSheet(u"QPushButton#submitbutton{\n"
"	background-color: green;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#submitbutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.buttonlayout.addWidget(self.submitbutton)

        self.closebutton = QPushButton(passworddialog)
        self.closebutton.setObjectName(u"closebutton")
        self.closebutton.setMinimumSize(QSize(0, 25))
        self.closebutton.setStyleSheet(u"QPushButton#closebutton{\n"
"	background-color: #656565;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#closebutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.buttonlayout.addWidget(self.closebutton)


        self.verticalLayout.addLayout(self.buttonlayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)

        self.retranslateUi(passworddialog)

        QMetaObject.connectSlotsByName(passworddialog)
    # setupUi

    def retranslateUi(self, passworddialog):
        passworddialog.setWindowTitle(QCoreApplication.translate("passworddialog", u"Admin Login", None))
        self.info.setText(QCoreApplication.translate("passworddialog", u"Admin account needs to be created", None))
        self.username.setText(QCoreApplication.translate("passworddialog", u"Username:", None))
        self.password.setText(QCoreApplication.translate("passworddialog", u"Password:", None))
        self.confirm.setText(QCoreApplication.translate("passworddialog", u"Confirm:", None))
        self.error.setText("")
        self.clearbutton.setText(QCoreApplication.translate("passworddialog", u"Clear", None))
        self.submitbutton.setText(QCoreApplication.translate("passworddialog", u"Submit", None))
        self.closebutton.setText(QCoreApplication.translate("passworddialog", u"Close", None))
    # retranslateUi

