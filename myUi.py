# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myUi.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(QSize(326, 0))
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.cpu = QLabel(self.centralwidget)
        self.cpu.setObjectName(u"cpu")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        self.cpu.setFont(font)
        self.cpu.setCursor(QCursor(Qt.ArrowCursor))
        self.cpu.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.cpu.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.cpu, 0, 0, 1, 1)

        self.gpu = QLabel(self.centralwidget)
        self.gpu.setObjectName(u"gpu")
        self.gpu.setFont(font)
        self.gpu.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.gpu.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.gpu, 4, 0, 1, 1)

        self.memory = QLabel(self.centralwidget)
        self.memory.setObjectName(u"memory")
        self.memory.setFont(font)
        self.memory.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.memory.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.memory, 0, 1, 1, 1)

        self.disk = QLabel(self.centralwidget)
        self.disk.setObjectName(u"disk")
        self.disk.setFont(font)
        self.disk.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.disk.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.disk, 4, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7", None))
        self.cpu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">cpu</p></body></html>", None))
        self.gpu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">gpu</p></body></html>", None))
        self.memory.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">memory</p></body></html>", None))
        self.disk.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">disk</p></body></html>", None))
    # retranslateUi

