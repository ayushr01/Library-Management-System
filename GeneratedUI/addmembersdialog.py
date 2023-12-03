# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addmembers.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_addmemdialog(object):
    def setupUi(self, addmemdialog):
        if not addmemdialog.objectName():
            addmemdialog.setObjectName(u"addmemdialog")
        addmemdialog.resize(400, 200)
        addmemdialog.setMinimumSize(QSize(400, 200))
        addmemdialog.setMaximumSize(QSize(400, 200))
        self.verticalLayout = QVBoxLayout(addmemdialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inputform = QFormLayout()
        self.inputform.setObjectName(u"inputform")
        self.inputform.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.inputform.setLabelAlignment(Qt.AlignCenter)
        self.inputform.setFormAlignment(Qt.AlignCenter)
        self.inputform.setHorizontalSpacing(40)
        self.inputform.setVerticalSpacing(25)
        self.inputform.setContentsMargins(10, -1, 10, -1)
        self.name = QLabel(addmemdialog)
        self.name.setObjectName(u"name")
        font = QFont()
        font.setBold(True)
        self.name.setFont(font)

        self.inputform.setWidget(0, QFormLayout.LabelRole, self.name)

        self.dob = QLabel(addmemdialog)
        self.dob.setObjectName(u"dob")
        self.dob.setFont(font)

        self.inputform.setWidget(1, QFormLayout.LabelRole, self.dob)

        self.inputname = QLineEdit(addmemdialog)
        self.inputname.setObjectName(u"inputname")
        self.inputname.setMinimumSize(QSize(0, 30))

        self.inputform.setWidget(0, QFormLayout.FieldRole, self.inputname)

        self.datepicker = QDateEdit(addmemdialog)
        self.datepicker.setObjectName(u"datepicker")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datepicker.sizePolicy().hasHeightForWidth())
        self.datepicker.setSizePolicy(sizePolicy)
        self.datepicker.setMinimumSize(QSize(0, 30))
        self.datepicker.setAlignment(Qt.AlignCenter)
        self.datepicker.setCalendarPopup(False)

        self.inputform.setWidget(1, QFormLayout.FieldRole, self.datepicker)


        self.verticalLayout.addLayout(self.inputform)

        self.error = QLabel(addmemdialog)
        self.error.setObjectName(u"error")
        self.error.setFont(font)
        self.error.setStyleSheet(u"color: orange")
        self.error.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.error)

        self.buttonlayout = QHBoxLayout()
        self.buttonlayout.setObjectName(u"buttonlayout")
        self.clearbutton = QPushButton(addmemdialog)
        self.clearbutton.setObjectName(u"clearbutton")
        self.clearbutton.setMinimumSize(QSize(0, 25))
        self.clearbutton.setStyleSheet(u"QPushButton#clearbutton{\n"
"	background-color: #f2a240;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#clearbutton:hover{\n"
"	border: 2px solid teal;\n"
"}")
        self.clearbutton.setAutoDefault(False)

        self.buttonlayout.addWidget(self.clearbutton)

        self.submitbutton = QPushButton(addmemdialog)
        self.submitbutton.setObjectName(u"submitbutton")
        self.submitbutton.setMinimumSize(QSize(0, 25))
        self.submitbutton.setStyleSheet(u"QPushButton#submitbutton{\n"
"	background-color: MediumSeaGreen;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#submitbutton:hover{\n"
"	border: 2px solid teal;\n"
"}")
        self.submitbutton.setAutoDefault(False)

        self.buttonlayout.addWidget(self.submitbutton)

        self.closebutton = QPushButton(addmemdialog)
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
        self.closebutton.setAutoDefault(False)

        self.buttonlayout.addWidget(self.closebutton)


        self.verticalLayout.addLayout(self.buttonlayout)


        self.retranslateUi(addmemdialog)

        QMetaObject.connectSlotsByName(addmemdialog)
    # setupUi

    def retranslateUi(self, addmemdialog):
        addmemdialog.setWindowTitle(QCoreApplication.translate("addmemdialog", u"Add Members", None))
        self.name.setText(QCoreApplication.translate("addmemdialog", u"Name:", None))
        self.dob.setText(QCoreApplication.translate("addmemdialog", u"DOB:", None))
        self.datepicker.setDisplayFormat(QCoreApplication.translate("addmemdialog", u"dd/MM/yyyy", None))
        self.error.setText("")
        self.clearbutton.setText(QCoreApplication.translate("addmemdialog", u"Clear", None))
        self.submitbutton.setText(QCoreApplication.translate("addmemdialog", u"Submit", None))
        self.closebutton.setText(QCoreApplication.translate("addmemdialog", u"Close", None))
    # retranslateUi

