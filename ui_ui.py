# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(290, 274)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setBaseSize(QSize(0, -1))
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setAcceptDrops(False)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color:#cacaca")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_7 = QPushButton(Form)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.btn_7.setFont(font)

        self.gridLayout.addWidget(self.btn_7, 2, 0, 1, 1)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setFont(font)

        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_5 = QPushButton(Form)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_5.setFont(font)

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_9 = QPushButton(Form)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_9.setFont(font)

        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)

        self.btn_8 = QPushButton(Form)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_8.setFont(font)

        self.gridLayout.addWidget(self.btn_8, 2, 1, 1, 1)

        self.btn_3 = QPushButton(Form)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setFont(font)

        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setFont(font)

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_1 = QPushButton(Form)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setFont(font)

        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_6 = QPushButton(Form)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setFont(font)

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Tick Toc Toe", None))
        self.btn_7.setText("")
        self.btn_2.setText("")
        self.btn_5.setText("")
        self.btn_9.setText("")
        self.btn_8.setText("")
        self.btn_3.setText("")
        self.btn_4.setText("")
        self.btn_1.setText("")
        self.btn_6.setText("")
    # retranslateUi

