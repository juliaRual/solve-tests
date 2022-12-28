# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(527, 678)
        Form.setStyleSheet(u"background-color: rgb(126, 89, 199);")
        self.pushButton_a1 = QPushButton(Form)
        self.pushButton_a1.setObjectName(u"pushButton_a1")
        self.pushButton_a1.setGeometry(QRect(70, 210, 381, 71))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(13)
        self.pushButton_a1.setFont(font)
        self.pushButton_a1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(241, 154, 117);\n"
"border-radius: 25;")
        self.pushButton_a2 = QPushButton(Form)
        self.pushButton_a2.setObjectName(u"pushButton_a2")
        self.pushButton_a2.setGeometry(QRect(70, 290, 381, 71))
        self.pushButton_a2.setFont(font)
        self.pushButton_a2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(241, 154, 117);\n"
"border-radius: 25;\n"
"padding: 0px 15px 0px 15px;")
        self.pushButton_a3 = QPushButton(Form)
        self.pushButton_a3.setObjectName(u"pushButton_a3")
        self.pushButton_a3.setGeometry(QRect(70, 370, 381, 71))
        self.pushButton_a3.setFont(font)
        self.pushButton_a3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_a3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(241, 154, 117);\n"
"border-radius: 25;")
        self.pushButton_a3.setAutoRepeat(False)
        self.pushButton_a3.setAutoExclusive(False)
        self.pushButton_a4 = QPushButton(Form)
        self.pushButton_a4.setObjectName(u"pushButton_a4")
        self.pushButton_a4.setGeometry(QRect(70, 450, 381, 71))
        self.pushButton_a4.setFont(font)
        self.pushButton_a4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(241, 154, 117);\n"
"border-radius: 25;")
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(320, 540, 131, 51))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 250, 252);\n"
"background-color: rgb(241, 172, 134);\n"
"border-radius: 25;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 570, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 591, 181))
        self.frame.setStyleSheet(u"background-color: rgb(234, 151, 116);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.textEdit_question = QTextEdit(self.frame)
        self.textEdit_question.setObjectName(u"textEdit_question")
        self.textEdit_question.setGeometry(QRect(70, 40, 421, 111))
        self.textEdit_question.setFont(font2)
        self.textEdit_question.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: null;\n"
"text-align: center;")
        self.textEdit_question.setUndoRedoEnabled(False)
        self.textEdit_question.setReadOnly(True)
        self.textEdit_question.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 540, 141, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 530, 51, 51))
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        font3.setPointSize(20)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(218, 255, 222);")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 570, 41, 31))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color:rgb(255, 242, 251);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 650, 511, 20))
        font4 = QFont()
        font4.setFamilies([u"Tahoma"])
        font4.setPointSize(11)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setOpenExternalLinks(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SPMI exams ", None))
        self.pushButton_a1.setText("")
        self.pushButton_a2.setText("")
        self.pushButton_a3.setText("")
        self.pushButton_a4.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043b\u044c\u0448\u0435", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435\u0433\u043e:", None))
        self.textEdit_question.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'.AppleSystemUIFont'; font-size:13pt;\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a href=\"https://github.com/juliaRual/solve-tests\"><span style=\" text-decoration: underline; color:#ffffff;\">github.com/juliaRual/solve-tests</span></a></p><p><br/></p></body></html>", None))
    # retranslateUi

