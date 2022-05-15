# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading GeneratedUI file 'bookdetails.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_bookdetaildialog(object):
    def setupUi(self, bookdetaildialog):
        if not bookdetaildialog.objectName():
            bookdetaildialog.setObjectName(u"bookdetaildialog")
        bookdetaildialog.resize(500, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bookdetaildialog.sizePolicy().hasHeightForWidth())
        bookdetaildialog.setSizePolicy(sizePolicy)
        bookdetaildialog.setMinimumSize(QSize(500, 300))
        bookdetaildialog.setMaximumSize(QSize(500, 300))
        font = QFont()
        font.setFamilies([u"Trebuchet MS"])
        font.setPointSize(13)
        font.setBold(True)
        bookdetaildialog.setFont(font)
        self.layoutWidget = QWidget(bookdetaildialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(180, 10, 311, 281))
        self.layoutWidget.setFont(font)
        self.data = QVBoxLayout(self.layoutWidget)
        self.data.setObjectName(u"data")
        self.data.setContentsMargins(0, 0, 0, 0)
        self.idfield = QLabel(self.layoutWidget)
        self.idfield.setObjectName(u"idfield")
        self.idfield.setFont(font)

        self.data.addWidget(self.idfield)

        self.titlefield = QLabel(self.layoutWidget)
        self.titlefield.setObjectName(u"titlefield")
        self.titlefield.setFont(font)

        self.data.addWidget(self.titlefield)

        self.authorfield = QLabel(self.layoutWidget)
        self.authorfield.setObjectName(u"authorfield")
        self.authorfield.setFont(font)

        self.data.addWidget(self.authorfield)

        self.ratingfield = QLabel(self.layoutWidget)
        self.ratingfield.setObjectName(u"ratingfield")
        self.ratingfield.setFont(font)

        self.data.addWidget(self.ratingfield)

        self.genrefield = QLabel(self.layoutWidget)
        self.genrefield.setObjectName(u"genrefield")
        self.genrefield.setFont(font)

        self.data.addWidget(self.genrefield)

        self.datefield = QLabel(self.layoutWidget)
        self.datefield.setObjectName(u"datefield")
        self.datefield.setFont(font)

        self.data.addWidget(self.datefield)

        self.totalfield = QLabel(self.layoutWidget)
        self.totalfield.setObjectName(u"totalfield")
        self.totalfield.setFont(font)

        self.data.addWidget(self.totalfield)

        self.issuedfield = QLabel(self.layoutWidget)
        self.issuedfield.setObjectName(u"issuedfield")
        self.issuedfield.setFont(font)

        self.data.addWidget(self.issuedfield)

        self.line = QFrame(bookdetaildialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(129, 0, 61, 301))
        self.line.setFont(font)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.layoutWidget1 = QWidget(bookdetaildialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 12, 121, 281))
        self.layoutWidget1.setFont(font)
        self.labels = QVBoxLayout(self.layoutWidget1)
        self.labels.setObjectName(u"labels")
        self.labels.setContentsMargins(0, 0, 0, 0)
        self.idlabel = QLabel(self.layoutWidget1)
        self.idlabel.setObjectName(u"idlabel")
        self.idlabel.setFont(font)

        self.labels.addWidget(self.idlabel)

        self.titlelabel = QLabel(self.layoutWidget1)
        self.titlelabel.setObjectName(u"titlelabel")
        self.titlelabel.setFont(font)

        self.labels.addWidget(self.titlelabel)

        self.authorlabel = QLabel(self.layoutWidget1)
        self.authorlabel.setObjectName(u"authorlabel")
        self.authorlabel.setFont(font)

        self.labels.addWidget(self.authorlabel)

        self.ratinglabel = QLabel(self.layoutWidget1)
        self.ratinglabel.setObjectName(u"ratinglabel")
        self.ratinglabel.setFont(font)

        self.labels.addWidget(self.ratinglabel)

        self.genrelabel = QLabel(self.layoutWidget1)
        self.genrelabel.setObjectName(u"genrelabel")
        self.genrelabel.setFont(font)

        self.labels.addWidget(self.genrelabel)

        self.datelabel = QLabel(self.layoutWidget1)
        self.datelabel.setObjectName(u"datelabel")
        self.datelabel.setFont(font)

        self.labels.addWidget(self.datelabel)

        self.totallabel = QLabel(self.layoutWidget1)
        self.totallabel.setObjectName(u"totallabel")
        self.totallabel.setFont(font)

        self.labels.addWidget(self.totallabel)

        self.issuedlabel = QLabel(self.layoutWidget1)
        self.issuedlabel.setObjectName(u"issuedlabel")
        self.issuedlabel.setFont(font)

        self.labels.addWidget(self.issuedlabel)


        self.retranslateUi(bookdetaildialog)

        QMetaObject.connectSlotsByName(bookdetaildialog)
    # setupUi

    def retranslateUi(self, bookdetaildialog):
        bookdetaildialog.setWindowTitle(QCoreApplication.translate("bookdetaildialog", u"Delete Members", None))
        self.idfield.setText("")
        self.titlefield.setText("")
        self.authorfield.setText("")
        self.ratingfield.setText("")
        self.genrefield.setText("")
        self.datefield.setText("")
        self.totalfield.setText("")
        self.issuedfield.setText("")
        self.idlabel.setText(QCoreApplication.translate("bookdetaildialog", u"ID:", None))
        self.titlelabel.setText(QCoreApplication.translate("bookdetaildialog", u"Title:", None))
        self.authorlabel.setText(QCoreApplication.translate("bookdetaildialog", u"Author:", None))
        self.ratinglabel.setText(QCoreApplication.translate("bookdetaildialog", u"Rating:", None))
        self.genrelabel.setText(QCoreApplication.translate("bookdetaildialog", u"Genre:", None))
        self.datelabel.setText(QCoreApplication.translate("bookdetaildialog", u"Date added:", None))
        self.totallabel.setText(QCoreApplication.translate("bookdetaildialog", u"Total copies:", None))
        self.issuedlabel.setText(QCoreApplication.translate("bookdetaildialog", u"Copies issued:", None))
    # retranslateUi

