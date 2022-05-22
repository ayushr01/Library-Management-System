# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bookdetails.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_bookdetaildialog(object):
    def setupUi(self, bookdetaildialog):
        if not bookdetaildialog.objectName():
            bookdetaildialog.setObjectName(u"bookdetaildialog")
        bookdetaildialog.resize(400, 300)
        bookdetaildialog.setMinimumSize(QSize(400, 300))
        bookdetaildialog.setMaximumSize(QSize(450, 300))
        self.formLayout = QFormLayout(bookdetaildialog)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(15)
        self.idlabel = QLabel(bookdetaildialog)
        self.idlabel.setObjectName(u"idlabel")
        font = QFont()
        font.setBold(True)
        self.idlabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.idlabel)

        self.ratinglabel = QLabel(bookdetaildialog)
        self.ratinglabel.setObjectName(u"ratinglabel")
        self.ratinglabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.ratinglabel)

        self.datelabel = QLabel(bookdetaildialog)
        self.datelabel.setObjectName(u"datelabel")
        self.datelabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.datelabel)

        self.totallabel = QLabel(bookdetaildialog)
        self.totallabel.setObjectName(u"totallabel")
        self.totallabel.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.totallabel)

        self.issuedlabel = QLabel(bookdetaildialog)
        self.issuedlabel.setObjectName(u"issuedlabel")
        self.issuedlabel.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.issuedlabel)

        self.titlelabel = QLabel(bookdetaildialog)
        self.titlelabel.setObjectName(u"titlelabel")
        self.titlelabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.titlelabel)

        self.authorlabel = QLabel(bookdetaildialog)
        self.authorlabel.setObjectName(u"authorlabel")
        self.authorlabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.authorlabel)

        self.genrelabel = QLabel(bookdetaildialog)
        self.genrelabel.setObjectName(u"genrelabel")
        self.genrelabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.genrelabel)

        self.idfield = QLabel(bookdetaildialog)
        self.idfield.setObjectName(u"idfield")
        self.idfield.setWordWrap(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idfield)

        self.ratingfield = QLabel(bookdetaildialog)
        self.ratingfield.setObjectName(u"ratingfield")
        self.ratingfield.setWordWrap(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ratingfield)

        self.titlefield = QLabel(bookdetaildialog)
        self.titlefield.setObjectName(u"titlefield")
        self.titlefield.setWordWrap(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.titlefield)

        self.authorfield = QLabel(bookdetaildialog)
        self.authorfield.setObjectName(u"authorfield")
        self.authorfield.setWordWrap(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.authorfield)

        self.genrefield = QLabel(bookdetaildialog)
        self.genrefield.setObjectName(u"genrefield")
        self.genrefield.setWordWrap(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.genrefield)

        self.datefield = QLabel(bookdetaildialog)
        self.datefield.setObjectName(u"datefield")
        self.datefield.setWordWrap(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.datefield)

        self.totalfield = QLabel(bookdetaildialog)
        self.totalfield.setObjectName(u"totalfield")
        self.totalfield.setWordWrap(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.totalfield)

        self.issuedfield = QLabel(bookdetaildialog)
        self.issuedfield.setObjectName(u"issuedfield")
        self.issuedfield.setWordWrap(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.issuedfield)


        self.retranslateUi(bookdetaildialog)

        QMetaObject.connectSlotsByName(bookdetaildialog)
    # setupUi

    def retranslateUi(self, bookdetaildialog):
        bookdetaildialog.setWindowTitle(QCoreApplication.translate("bookdetaildialog", u"Book Details", None))
        self.idlabel.setText(QCoreApplication.translate("bookdetaildialog", u"ID:", None))
        self.ratinglabel.setText(QCoreApplication.translate("bookdetaildialog", u"Rating:", None))
        self.datelabel.setText(QCoreApplication.translate("bookdetaildialog", u"Date Added:", None))
        self.totallabel.setText(QCoreApplication.translate("bookdetaildialog", u"Total Copies:", None))
        self.issuedlabel.setText(QCoreApplication.translate("bookdetaildialog", u"Copies Issued:", None))
        self.titlelabel.setText(QCoreApplication.translate("bookdetaildialog", u"Title:", None))
        self.authorlabel.setText(QCoreApplication.translate("bookdetaildialog", u"Author:", None))
        self.genrelabel.setText(QCoreApplication.translate("bookdetaildialog", u"Genre:", None))
        self.idfield.setText("")
        self.ratingfield.setText("")
        self.titlefield.setText("")
        self.authorfield.setText("")
        self.genrefield.setText("")
        self.datefield.setText("")
        self.totalfield.setText("")
        self.issuedfield.setText("")
    # retranslateUi

