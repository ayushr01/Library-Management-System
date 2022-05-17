# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addbooks.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_addbookdialog(object):
    def setupUi(self, addbookdialog):
        if not addbookdialog.objectName():
            addbookdialog.setObjectName(u"addbookdialog")
        addbookdialog.resize(450, 400)
        addbookdialog.setMinimumSize(QSize(450, 400))
        addbookdialog.setMaximumSize(QSize(450, 400))
        self.verticalLayout = QVBoxLayout(addbookdialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(addbookdialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.manual = QWidget()
        self.manual.setObjectName(u"manual")
        self.verticalLayout_2 = QVBoxLayout(self.manual)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.inputform = QFormLayout()
        self.inputform.setObjectName(u"inputform")
        self.inputform.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.inputform.setLabelAlignment(Qt.AlignCenter)
        self.inputform.setFormAlignment(Qt.AlignCenter)
        self.inputform.setHorizontalSpacing(40)
        self.inputform.setVerticalSpacing(25)
        self.inputform.setContentsMargins(10, -1, 10, -1)
        self.titlefield = QLabel(self.manual)
        self.titlefield.setObjectName(u"titlefield")
        font = QFont()
        font.setBold(True)
        self.titlefield.setFont(font)

        self.inputform.setWidget(0, QFormLayout.LabelRole, self.titlefield)

        self.inputtitle = QLineEdit(self.manual)
        self.inputtitle.setObjectName(u"inputtitle")
        self.inputtitle.setMinimumSize(QSize(0, 30))

        self.inputform.setWidget(0, QFormLayout.FieldRole, self.inputtitle)

        self.authorfield = QLabel(self.manual)
        self.authorfield.setObjectName(u"authorfield")
        self.authorfield.setFont(font)

        self.inputform.setWidget(1, QFormLayout.LabelRole, self.authorfield)

        self.inputauthor = QLineEdit(self.manual)
        self.inputauthor.setObjectName(u"inputauthor")
        self.inputauthor.setMinimumSize(QSize(0, 30))

        self.inputform.setWidget(1, QFormLayout.FieldRole, self.inputauthor)

        self.genrefield = QLabel(self.manual)
        self.genrefield.setObjectName(u"genrefield")
        self.genrefield.setFont(font)

        self.inputform.setWidget(2, QFormLayout.LabelRole, self.genrefield)

        self.inputgenre = QLineEdit(self.manual)
        self.inputgenre.setObjectName(u"inputgenre")
        self.inputgenre.setMinimumSize(QSize(0, 30))

        self.inputform.setWidget(2, QFormLayout.FieldRole, self.inputgenre)

        self.totalfield = QLabel(self.manual)
        self.totalfield.setObjectName(u"totalfield")
        self.totalfield.setFont(font)

        self.inputform.setWidget(3, QFormLayout.LabelRole, self.totalfield)

        self.inputtotal = QLineEdit(self.manual)
        self.inputtotal.setObjectName(u"inputtotal")
        self.inputtotal.setMinimumSize(QSize(0, 30))

        self.inputform.setWidget(3, QFormLayout.FieldRole, self.inputtotal)


        self.verticalLayout_2.addLayout(self.inputform)

        self.error = QLabel(self.manual)
        self.error.setObjectName(u"error")
        self.error.setFont(font)
        self.error.setStyleSheet(u"color: orange")
        self.error.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.error)

        self.buttonlayout = QHBoxLayout()
        self.buttonlayout.setObjectName(u"buttonlayout")
        self.clearbutton = QPushButton(self.manual)
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

        self.submitbutton = QPushButton(self.manual)
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

        self.closebutton = QPushButton(self.manual)
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


        self.verticalLayout_2.addLayout(self.buttonlayout)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.tabWidget.addTab(self.manual, "")
        self.isbn = QWidget()
        self.isbn.setObjectName(u"isbn")
        self.verticalLayout_4 = QVBoxLayout(self.isbn)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.isbnentry = QHBoxLayout()
        self.isbnentry.setSpacing(15)
        self.isbnentry.setObjectName(u"isbnentry")
        self.isbnentry.setContentsMargins(10, -1, 10, -1)
        self.isbnlabel = QLabel(self.isbn)
        self.isbnlabel.setObjectName(u"isbnlabel")
        self.isbnlabel.setFont(font)

        self.isbnentry.addWidget(self.isbnlabel)

        self.isbnfield = QLineEdit(self.isbn)
        self.isbnfield.setObjectName(u"isbnfield")
        self.isbnfield.setMinimumSize(QSize(0, 30))

        self.isbnentry.addWidget(self.isbnfield)

        self.searchbuttonisbn = QPushButton(self.isbn)
        self.searchbuttonisbn.setObjectName(u"searchbuttonisbn")
        self.searchbuttonisbn.setMinimumSize(QSize(60, 30))
        self.searchbuttonisbn.setStyleSheet(u"QPushButton#searchbuttonisbn{\n"
"	background-color: BurlyWood;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#searchbuttonisbn:hover{\n"
"	border: 2px solid teal;\n"
"}")
        self.searchbuttonisbn.setAutoDefault(False)

        self.isbnentry.addWidget(self.searchbuttonisbn)

        self.isbnentry.setStretch(0, 2)
        self.isbnentry.setStretch(1, 10)
        self.isbnentry.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.isbnentry)

        self.detailslayout = QVBoxLayout()
        self.detailslayout.setObjectName(u"detailslayout")
        self.detailslayout.setContentsMargins(10, 5, 10, 5)
        self.headingisbn = QLabel(self.isbn)
        self.headingisbn.setObjectName(u"headingisbn")
        self.headingisbn.setFont(font)
        self.headingisbn.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.detailslayout.addWidget(self.headingisbn)

        self.titleisbn = QLabel(self.isbn)
        self.titleisbn.setObjectName(u"titleisbn")
        self.titleisbn.setAlignment(Qt.AlignCenter)

        self.detailslayout.addWidget(self.titleisbn)

        self.authorisbn = QLabel(self.isbn)
        self.authorisbn.setObjectName(u"authorisbn")
        self.authorisbn.setAlignment(Qt.AlignCenter)

        self.detailslayout.addWidget(self.authorisbn)

        self.publisherisbn = QLabel(self.isbn)
        self.publisherisbn.setObjectName(u"publisherisbn")
        self.publisherisbn.setAlignment(Qt.AlignCenter)

        self.detailslayout.addWidget(self.publisherisbn)


        self.verticalLayout_4.addLayout(self.detailslayout)

        self.totallayout = QHBoxLayout()
        self.totallayout.setSpacing(15)
        self.totallayout.setObjectName(u"totallayout")
        self.totallayout.setContentsMargins(10, -1, 10, -1)
        self.totallabelisbn = QLabel(self.isbn)
        self.totallabelisbn.setObjectName(u"totallabelisbn")
        self.totallabelisbn.setFont(font)

        self.totallayout.addWidget(self.totallabelisbn)

        self.totalfieldisbn = QLineEdit(self.isbn)
        self.totalfieldisbn.setObjectName(u"totalfieldisbn")
        self.totalfieldisbn.setMinimumSize(QSize(0, 30))

        self.totallayout.addWidget(self.totalfieldisbn)


        self.verticalLayout_4.addLayout(self.totallayout)

        self.errorisbn = QLabel(self.isbn)
        self.errorisbn.setObjectName(u"errorisbn")
        self.errorisbn.setFont(font)
        self.errorisbn.setStyleSheet(u"color: orange")
        self.errorisbn.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.errorisbn)

        self.buttonlayoutisn = QHBoxLayout()
        self.buttonlayoutisn.setObjectName(u"buttonlayoutisn")
        self.clearbuttonisbn = QPushButton(self.isbn)
        self.clearbuttonisbn.setObjectName(u"clearbuttonisbn")
        self.clearbuttonisbn.setMinimumSize(QSize(0, 25))
        self.clearbuttonisbn.setStyleSheet(u"QPushButton#clearbuttonisbn{\n"
"	background-color: #f2a240;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#clearbuttonisbn:hover{\n"
"	border: 2px solid teal;\n"
"}")
        self.clearbuttonisbn.setAutoDefault(False)

        self.buttonlayoutisn.addWidget(self.clearbuttonisbn)

        self.submitbuttonisbn = QPushButton(self.isbn)
        self.submitbuttonisbn.setObjectName(u"submitbuttonisbn")
        self.submitbuttonisbn.setMinimumSize(QSize(0, 25))
        self.submitbuttonisbn.setStyleSheet(u"QPushButton#submitbuttonisbn{\n"
"	background-color: MediumSeaGreen;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#submitbuttonisbn:hover{\n"
"	border: 2px solid teal;\n"
"}")
        self.submitbuttonisbn.setAutoDefault(False)

        self.buttonlayoutisn.addWidget(self.submitbuttonisbn)

        self.closebuttonisbn = QPushButton(self.isbn)
        self.closebuttonisbn.setObjectName(u"closebuttonisbn")
        self.closebuttonisbn.setMinimumSize(QSize(0, 25))
        self.closebuttonisbn.setStyleSheet(u"QPushButton#closebuttonisbn{\n"
"	background-color: #656565;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#closebuttonisbn:hover{\n"
"	border: 2px solid teal;\n"
"}")
        self.closebuttonisbn.setAutoDefault(False)

        self.buttonlayoutisn.addWidget(self.closebuttonisbn)


        self.verticalLayout_4.addLayout(self.buttonlayoutisn)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 4)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 2)
        self.tabWidget.addTab(self.isbn, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(addbookdialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(addbookdialog)
    # setupUi

    def retranslateUi(self, addbookdialog):
        addbookdialog.setWindowTitle(QCoreApplication.translate("addbookdialog", u"Add Books", None))
        self.titlefield.setText(QCoreApplication.translate("addbookdialog", u"Title:", None))
        self.authorfield.setText(QCoreApplication.translate("addbookdialog", u"Author:", None))
        self.genrefield.setText(QCoreApplication.translate("addbookdialog", u"Genre:", None))
        self.totalfield.setText(QCoreApplication.translate("addbookdialog", u"Total:", None))
        self.error.setText("")
        self.clearbutton.setText(QCoreApplication.translate("addbookdialog", u"Clear", None))
        self.submitbutton.setText(QCoreApplication.translate("addbookdialog", u"Submit", None))
        self.closebutton.setText(QCoreApplication.translate("addbookdialog", u"Close", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manual), QCoreApplication.translate("addbookdialog", u"Manual Entry", None))
        self.isbnlabel.setText(QCoreApplication.translate("addbookdialog", u"ISBN:", None))
        self.searchbuttonisbn.setText(QCoreApplication.translate("addbookdialog", u"Search", None))
        self.headingisbn.setText(QCoreApplication.translate("addbookdialog", u"Book Details:", None))
        self.titleisbn.setText(QCoreApplication.translate("addbookdialog", u"-", None))
        self.authorisbn.setText(QCoreApplication.translate("addbookdialog", u"-", None))
        self.publisherisbn.setText(QCoreApplication.translate("addbookdialog", u"-", None))
        self.totallabelisbn.setText(QCoreApplication.translate("addbookdialog", u"Total:", None))
        self.errorisbn.setText("")
        self.clearbuttonisbn.setText(QCoreApplication.translate("addbookdialog", u"Clear", None))
        self.submitbuttonisbn.setText(QCoreApplication.translate("addbookdialog", u"Submit", None))
        self.closebuttonisbn.setText(QCoreApplication.translate("addbookdialog", u"Close", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.isbn), QCoreApplication.translate("addbookdialog", u"Search using ISBN", None))
    # retranslateUi

