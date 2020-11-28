from threading import Thread
import subprocess

def startLoading():
    subprocess.Popen('loading.py', shell=True, creationflags=0x80000000)

loadingThread = Thread(target=startLoading)
loadingThread.daemon = True
loadingThread.start()

import socket
from packaging import version
from shutil import move as moveFile
import requests
import json
from pathlib import Path
import traceback
import versionScraper
import os
import easygui
from getpass import getuser
import webbrowser
import socket
from psutil import virtual_memory
import ctypes
import sys
import platform
import datetime
import calendar
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 359)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 72, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 72, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 72, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(415, 295, 86, 56))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/sylleris-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-70, 312, 481, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-70, 330, 481, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-70, 300, 481, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 496, 286))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(49, 52, 76);\n"
"alternate-background-color: rgb(46, 51, 80);\n"
"background-color: rgb(60, 61, 86);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(5, 5, 126, 26))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(5, 40, 221, 211))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(5, 18, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.type = QtWidgets.QComboBox(self.groupBox)
        self.type.setGeometry(QtCore.QRect(95, 15, 116, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.type.setFont(font)
        self.type.setToolTip("")
        self.type.setStatusTip("")
        self.type.setWhatsThis("")
        self.type.setObjectName("type")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/vanilla.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.type.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/bukkit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.type.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/spigot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.type.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/forge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.type.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.type.addItem(icon4, "")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(5, 40, 141, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(5, 138, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(5, 165, 206, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(167, 255, 165);")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.version = QtWidgets.QComboBox(self.groupBox)
        self.version.setGeometry(QtCore.QRect(60, 135, 156, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.version.setFont(font)
        self.version.setToolTip("")
        self.version.setStatusTip("")
        self.version.setWhatsThis("")
        self.version.setObjectName("version")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(5, 55, 141, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(5, 70, 151, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(5, 85, 141, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.label_11.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(5, 100, 141, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.label_12.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(235, 43, 246, 206))
        self.groupBox_2.setObjectName("groupBox_2")
        self.acceptEula = QtWidgets.QCheckBox(self.groupBox_2)
        self.acceptEula.setGeometry(QtCore.QRect(5, 180, 96, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.acceptEula.setFont(font)
        self.acceptEula.setChecked(True)
        self.acceptEula.setTristate(False)
        self.acceptEula.setObjectName("acceptEula")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.username = QtWidgets.QLineEdit(self.groupBox_2)
        self.username.setGeometry(QtCore.QRect(90, 20, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setMaxLength(16)
        self.username.setObjectName("username")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 55, 96, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.minimumRAM = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.minimumRAM.setGeometry(QtCore.QRect(111, 53, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.minimumRAM.setFont(font)
        self.minimumRAM.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.minimumRAM.setSpecialValueText("")
        self.minimumRAM.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.minimumRAM.setDecimals(1)
        self.minimumRAM.setMinimum(2.0)
        self.minimumRAM.setSingleStep(0.5)
        self.minimumRAM.setObjectName("minimumRAM")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(9, 90, 96, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.maximumRAM = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.maximumRAM.setGeometry(QtCore.QRect(111, 90, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.maximumRAM.setFont(font)
        self.maximumRAM.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.maximumRAM.setSpecialValueText("")
        self.maximumRAM.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.maximumRAM.setDecimals(1)
        self.maximumRAM.setMinimum(3.0)
        self.maximumRAM.setSingleStep(0.5)
        self.maximumRAM.setObjectName("maximumRAM")
        self.ramTip = QtWidgets.QLabel(self.groupBox_2)
        self.ramTip.setGeometry(QtCore.QRect(10, 120, 226, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.ramTip.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.ramTip.setFont(font)
        self.ramTip.setStyleSheet("color: rgb(167, 255, 165);")
        self.ramTip.setWordWrap(True)
        self.ramTip.setObjectName("ramTip")
        self.acceptEula_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.acceptEula_2.setGeometry(QtCore.QRect(5, 155, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.acceptEula_2.setFont(font)
        self.acceptEula_2.setChecked(True)
        self.acceptEula_2.setTristate(False)
        self.acceptEula_2.setObjectName("acceptEula_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(5, 5, 96, 26))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_16.setObjectName("label_16")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(5, 35, 486, 126))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(5, 15, 126, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(5, 45, 126, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_6.setGeometry(QtCore.QRect(325, 75, 126, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_7.setGeometry(QtCore.QRect(5, 105, 126, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(5, 75, 126, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_4.setGeometry(QtCore.QRect(325, 15, 126, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_9.setGeometry(QtCore.QRect(145, 45, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_5.setGeometry(QtCore.QRect(325, 45, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_8.setGeometry(QtCore.QRect(145, 15, 136, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setChecked(True)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_10.setGeometry(QtCore.QRect(145, 75, 166, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_11.setGeometry(QtCore.QRect(145, 105, 126, 17))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(395, 100, 41, 23))
        self.pushButton.setStyleSheet("color: rgb(255, 74, 77);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 100, 41, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 61, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 51, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.pushButton_2.setPalette(palette)
        self.pushButton_2.setStyleSheet("color: rgb(38, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(5, 165, 486, 96))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(5, 17, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gamemode = QtWidgets.QComboBox(self.groupBox_4)
        self.gamemode.setGeometry(QtCore.QRect(80, 15, 81, 22))
        self.gamemode.setObjectName("gamemode")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/survival.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gamemode.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/creative.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gamemode.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/adventure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gamemode.addItem(icon7, "")
        self.gamemode.addItem("")
        self.difficulty = QtWidgets.QComboBox(self.groupBox_4)
        self.difficulty.setGeometry(QtCore.QRect(80, 43, 81, 22))
        self.difficulty.setObjectName("difficulty")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/peaceful.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.difficulty.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources/easy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.difficulty.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resources/normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.difficulty.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("resources/hard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.difficulty.addItem(icon11, "")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(5, 45, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(5, 71, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.levelType = QtWidgets.QLineEdit(self.groupBox_4)
        self.levelType.setGeometry(QtCore.QRect(80, 70, 81, 20))
        self.levelType.setMaxLength(30)
        self.levelType.setObjectName("levelType")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(170, 15, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.playerSlots = QtWidgets.QSpinBox(self.groupBox_4)
        self.playerSlots.setGeometry(QtCore.QRect(245, 12, 76, 22))
        self.playerSlots.setPrefix("")
        self.playerSlots.setMinimum(2)
        self.playerSlots.setMaximum(150000)
        self.playerSlots.setObjectName("playerSlots")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(170, 41, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.port = QtWidgets.QLineEdit(self.groupBox_4)
        self.port.setGeometry(QtCore.QRect(245, 40, 76, 20))
        self.port.setMaxLength(30)
        self.port.setObjectName("port")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(170, 71, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.worldName = QtWidgets.QLineEdit(self.groupBox_4)
        self.worldName.setGeometry(QtCore.QRect(245, 70, 76, 20))
        self.worldName.setMaxLength(30)
        self.worldName.setObjectName("worldName")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(330, 16, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.seed = QtWidgets.QLineEdit(self.groupBox_4)
        self.seed.setGeometry(QtCore.QRect(405, 15, 76, 20))
        self.seed.setText("")
        self.seed.setMaxLength(30)
        self.seed.setObjectName("seed")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(330, 50, 146, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.motd = QtWidgets.QLineEdit(self.groupBox_4)
        self.motd.setGeometry(QtCore.QRect(330, 70, 151, 20))
        self.motd.setText("")
        self.motd.setMaxLength(30)
        self.motd.setObjectName("motd")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setGeometry(QtCore.QRect(5, 5, 126, 26))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_25.setObjectName("label_25")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(5, 35, 241, 221))
        self.groupBox_5.setObjectName("groupBox_5")
        self.whitelist = QtWidgets.QListWidget(self.groupBox_5)
        self.whitelist.setGeometry(QtCore.QRect(5, 15, 231, 151))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.whitelist.setFont(font)
        self.whitelist.setObjectName("whitelist")
        self.whitelistAdd = QtWidgets.QLineEdit(self.groupBox_5)
        self.whitelistAdd.setGeometry(QtCore.QRect(5, 170, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.whitelistAdd.setFont(font)
        self.whitelistAdd.setObjectName("whitelistAdd")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 170, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5.setGeometry(QtCore.QRect(5, 195, 126, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(255, 94, 97);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_6.setGeometry(QtCore.QRect(135, 195, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 60, 63);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(250, 35, 241, 221))
        self.groupBox_6.setObjectName("groupBox_6")
        self.ops = QtWidgets.QListWidget(self.groupBox_6)
        self.ops.setGeometry(QtCore.QRect(5, 15, 231, 151))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.ops.setFont(font)
        self.ops.setObjectName("ops")
        self.opsAdd = QtWidgets.QLineEdit(self.groupBox_6)
        self.opsAdd.setGeometry(QtCore.QRect(5, 170, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.opsAdd.setFont(font)
        self.opsAdd.setObjectName("opsAdd")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 170, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_8.setGeometry(QtCore.QRect(5, 195, 126, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(255, 94, 97);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_7.setGeometry(QtCore.QRect(135, 195, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(255, 60, 63);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(5, 5, 126, 26))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_26.setObjectName("label_26")
        self.datapacksBox = QtWidgets.QGroupBox(self.tab_4)
        self.datapacksBox.setGeometry(QtCore.QRect(5, 35, 236, 221))
        self.datapacksBox.setObjectName("datapacksBox")
        self.datapacks = QtWidgets.QListWidget(self.datapacksBox)
        self.datapacks.setGeometry(QtCore.QRect(5, 15, 226, 126))
        self.datapacks.setObjectName("datapacks")
        self.pushButton_10 = QtWidgets.QPushButton(self.datapacksBox)
        self.pushButton_10.setGeometry(QtCore.QRect(5, 170, 146, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("color: rgb(255, 94, 97);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.datapacksBox)
        self.pushButton_9.setGeometry(QtCore.QRect(5, 195, 146, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(255, 60, 63);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.datapacksBox)
        self.pushButton_11.setGeometry(QtCore.QRect(5, 145, 146, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color: rgb(25, 255, 0);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_30 = QtWidgets.QLabel(self.datapacksBox)
        self.label_30.setGeometry(QtCore.QRect(155, 150, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(255, 185, 186);")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_30.setWordWrap(True)
        self.label_30.setObjectName("label_30")
        self.label_27 = QtWidgets.QLabel(self.datapacksBox)
        self.label_27.setGeometry(QtCore.QRect(196, 190, 31, 26))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("resources/vanilla.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.pluginsBox = QtWidgets.QGroupBox(self.tab_4)
        self.pluginsBox.setEnabled(False)
        self.pluginsBox.setGeometry(QtCore.QRect(245, 35, 246, 221))
        self.pluginsBox.setObjectName("pluginsBox")
        self.plugins = QtWidgets.QListWidget(self.pluginsBox)
        self.plugins.setGeometry(QtCore.QRect(5, 15, 236, 126))
        self.plugins.setObjectName("plugins")
        self.pushButton_17 = QtWidgets.QPushButton(self.pluginsBox)
        self.pushButton_17.setGeometry(QtCore.QRect(5, 195, 146, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("color: rgb(255, 60, 63);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_15 = QtWidgets.QPushButton(self.pluginsBox)
        self.pushButton_15.setGeometry(QtCore.QRect(5, 145, 146, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("color: rgb(25, 255, 0);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.pluginsBox)
        self.pushButton_16.setGeometry(QtCore.QRect(5, 170, 146, 23))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("color: rgb(255, 94, 97);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_28 = QtWidgets.QLabel(self.pluginsBox)
        self.label_28.setGeometry(QtCore.QRect(160, 145, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(255, 185, 186);")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_28.setWordWrap(True)
        self.label_28.setObjectName("label_28")
        self.label_31 = QtWidgets.QLabel(self.pluginsBox)
        self.label_31.setGeometry(QtCore.QRect(213, 190, 31, 26))
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("resources/vanilla.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.pluginsBox)
        self.label_32.setGeometry(QtCore.QRect(179, 190, 31, 26))
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("resources/bukkit.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.pluginsBox)
        self.label_33.setGeometry(QtCore.QRect(150, 190, 31, 26))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("resources/spigot.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_34 = QtWidgets.QLabel(self.tab_5)
        self.label_34.setGeometry(QtCore.QRect(5, 5, 126, 26))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(14)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab_5)
        self.label_35.setGeometry(QtCore.QRect(5, 40, 481, 36))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(255, 67, 70);")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_5)
        self.label_36.setGeometry(QtCore.QRect(5, 80, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(255, 170, 0);")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName("label_36")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setGeometry(QtCore.QRect(165, 80, 121, 23))
        self.pushButton_12.setStyleSheet("color: rgb(136, 255, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.line_2 = QtWidgets.QFrame(self.tab_5)
        self.line_2.setGeometry(QtCore.QRect(5, 105, 486, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.readyText = QtWidgets.QLabel(self.tab_5)
        self.readyText.setGeometry(QtCore.QRect(5, 125, 436, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.readyText.setFont(font)
        self.readyText.setObjectName("readyText")
        self.readyText_2 = QtWidgets.QLabel(self.tab_5)
        self.readyText_2.setGeometry(QtCore.QRect(5, 182, 56, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.readyText_2.setFont(font)
        self.readyText_2.setObjectName("readyText_2")
        self.directory = QtWidgets.QLineEdit(self.tab_5)
        self.directory.setGeometry(QtCore.QRect(60, 180, 306, 20))
        self.directory.setReadOnly(False)
        self.directory.setObjectName("directory")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_13.setGeometry(QtCore.QRect(370, 180, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.create = QtWidgets.QPushButton(self.tab_5)
        self.create.setEnabled(False)
        self.create.setGeometry(QtCore.QRect(5, 220, 111, 36))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(12)
        self.create.setFont(font)
        self.create.setStyleSheet("color: rgb(0, 255, 72);")
        self.create.setObjectName("create")
        self.warning = QtWidgets.QLabel(self.tab_5)
        self.warning.setGeometry(QtCore.QRect(5, 150, 486, 26))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.warning.setFont(font)
        self.warning.setStyleSheet("color: rgb(255, 65, 65);")
        self.warning.setText("")
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")
        self.progress = QtWidgets.QLabel(self.tab_5)
        self.progress.setGeometry(QtCore.QRect(120, 220, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.progress.setFont(font)
        self.progress.setStyleSheet("color: rgb(36, 8, 255);\n"
"color: rgb(255, 131, 6);")
        self.progress.setObjectName("progress")
        self.currentAction = QtWidgets.QLabel(self.tab_5)
        self.currentAction.setGeometry(QtCore.QRect(120, 240, 186, 16))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.currentAction.setFont(font)
        self.currentAction.setStyleSheet("color: rgb(234, 255, 0);")
        self.currentAction.setText("")
        self.currentAction.setObjectName("currentAction")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(5, 340, 91, 16))
        self.label_29.setObjectName("label_29")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.difficulty.setCurrentIndex(2)
        self.type.currentTextChanged['QString'].connect(wrapperChange)
        self.username.textChanged['QString'].connect(usernameChange)
        self.minimumRAM.valueChanged['double'].connect(minimumRAMChange)
        self.pushButton.clicked.connect(checkboxesOff)
        self.pushButton_2.clicked.connect(checkboxesOn)
        self.pushButton_3.clicked.connect(whitelistAdd)
        self.pushButton_5.clicked.connect(whitelistDelete)
        self.pushButton_6.clicked.connect(whitelistClear)
        self.pushButton_4.clicked.connect(OPsAdd)
        self.pushButton_8.clicked.connect(OPsDelete)
        self.pushButton_7.clicked.connect(OPsClear)
        self.pushButton_11.clicked.connect(datapacksAdd)
        self.pushButton_9.clicked.connect(datapacksClear)
        self.pushButton_10.clicked.connect(datapacksDelete)
        self.pushButton_15.clicked.connect(pluginsAdd)
        self.pushButton_16.clicked.connect(pluginsDelete)
        self.pushButton_17.clicked.connect(pluginsClear)
        self.pushButton_12.clicked.connect(portforward)
        self.pushButton_13.clicked.connect(selectFolder)
        self.create.clicked.connect(createServer)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server Creator - Sylleris"))
        self.label_2.setText(_translate("MainWindow", "Not affiliated with Mojang or any other company"))
        self.label_3.setText(_translate("MainWindow", "Created by Cyclip"))
        self.label_4.setText(_translate("MainWindow", "Main settings"))
        self.groupBox.setTitle(_translate("MainWindow", "Version"))
        self.label_5.setText(_translate("MainWindow", "Wrapper:"))
        self.type.setItemText(0, _translate("MainWindow", "Vanilla"))
        self.type.setItemText(1, _translate("MainWindow", "CraftBukkit"))
        self.type.setItemText(2, _translate("MainWindow", "Spigot"))
        self.type.setItemText(3, _translate("MainWindow", "Forge"))
        self.type.setItemText(4, _translate("MainWindow", "PaperMC"))
        self.label_6.setText(_translate("MainWindow", "Vanilla: Pure MC"))
        self.label_7.setText(_translate("MainWindow", "Version:"))
        self.label_8.setText(_translate("MainWindow", "You should use the latest build for that wrapper."))
        self.label_9.setText(_translate("MainWindow", "CraftBukkit: Use plugins"))
        self.label_10.setText(_translate("MainWindow", "Spigot: Plugins + Optimisation"))
        self.label_11.setText(_translate("MainWindow", "Forge: Mods"))
        self.label_12.setText(_translate("MainWindow", "PaperMC: Very fast"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Other settings"))
        self.acceptEula.setText(_translate("MainWindow", "Accept EULA"))
        self.label_13.setText(_translate("MainWindow", "Username:"))
        self.username.setPlaceholderText(_translate("MainWindow", "Enter your username here"))
        self.label_14.setText(_translate("MainWindow", "Minimum RAM:"))
        self.minimumRAM.setSuffix(_translate("MainWindow", " GB"))
        self.label_15.setText(_translate("MainWindow", "Maximum RAM:"))
        self.maximumRAM.setSuffix(_translate("MainWindow", " GB"))
        self.ramTip.setText(_translate("MainWindow", "Tip: You have [unknown] amount of RAM."))
        self.acceptEula_2.setText(_translate("MainWindow", "Generate Batch file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main settings"))
        self.label_16.setText(_translate("MainWindow", "Properties"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Checkboxes"))
        self.checkBox.setText(_translate("MainWindow", "Allow nether"))
        self.checkBox_2.setText(_translate("MainWindow", "Enforce whitelist"))
        self.checkBox_6.setText(_translate("MainWindow", "Spawn NPCs"))
        self.checkBox_7.setText(_translate("MainWindow", "Allow flight"))
        self.checkBox_3.setText(_translate("MainWindow", "Spawn monsters"))
        self.checkBox_4.setText(_translate("MainWindow", "Player PvP"))
        self.checkBox_9.setText(_translate("MainWindow", "Generate structures"))
        self.checkBox_5.setText(_translate("MainWindow", "Command Blocks"))
        self.checkBox_8.setText(_translate("MainWindow", "Spawn animals"))
        self.checkBox_10.setText(_translate("MainWindow", "Premium accounts only"))
        self.checkBox_11.setText(_translate("MainWindow", "Snooper"))
        self.pushButton.setText(_translate("MainWindow", "All off"))
        self.pushButton_2.setText(_translate("MainWindow", "All on"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Other properties"))
        self.label_17.setText(_translate("MainWindow", "Gamemode:"))
        self.gamemode.setItemText(0, _translate("MainWindow", "Survival"))
        self.gamemode.setItemText(1, _translate("MainWindow", "Creative"))
        self.gamemode.setItemText(2, _translate("MainWindow", "Adventure"))
        self.gamemode.setItemText(3, _translate("MainWindow", "Spectator"))
        self.difficulty.setItemText(0, _translate("MainWindow", "Peaceful"))
        self.difficulty.setItemText(1, _translate("MainWindow", "Easy"))
        self.difficulty.setItemText(2, _translate("MainWindow", "Normal"))
        self.difficulty.setItemText(3, _translate("MainWindow", "Hard"))
        self.label_18.setText(_translate("MainWindow", "Difficulty:"))
        self.label_19.setText(_translate("MainWindow", "Level type:"))
        self.levelType.setText(_translate("MainWindow", "default"))
        self.levelType.setPlaceholderText(_translate("MainWindow", "default"))
        self.label_20.setText(_translate("MainWindow", "Player slots:"))
        self.playerSlots.setSuffix(_translate("MainWindow", " players"))
        self.label_21.setText(_translate("MainWindow", "Port:"))
        self.port.setText(_translate("MainWindow", "25565"))
        self.port.setPlaceholderText(_translate("MainWindow", "25565"))
        self.label_22.setText(_translate("MainWindow", "World name:"))
        self.worldName.setText(_translate("MainWindow", "world"))
        self.worldName.setPlaceholderText(_translate("MainWindow", "world"))
        self.label_23.setText(_translate("MainWindow", "World seed:"))
        self.seed.setPlaceholderText(_translate("MainWindow", "Empty"))
        self.label_24.setText(_translate("MainWindow", "MOTD:"))
        self.motd.setPlaceholderText(_translate("MainWindow", "Empty"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Properties"))
        self.label_25.setText(_translate("MainWindow", "Whitelist/OPs"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Whitelist"))
        __sortingEnabled = self.whitelist.isSortingEnabled()
        self.whitelist.setSortingEnabled(False)
        self.whitelist.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("MainWindow", "Add player"))
        self.pushButton_5.setText(_translate("MainWindow", "Delete selected"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete all"))
        self.groupBox_6.setTitle(_translate("MainWindow", "OPs"))
        __sortingEnabled = self.ops.isSortingEnabled()
        self.ops.setSortingEnabled(False)
        self.ops.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("MainWindow", "Add player"))
        self.pushButton_8.setText(_translate("MainWindow", "Delete selected"))
        self.pushButton_7.setText(_translate("MainWindow", "Delete all"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Whitelist/OPs"))
        self.label_26.setText(_translate("MainWindow", "Additions"))
        self.datapacksBox.setTitle(_translate("MainWindow", "[Vanilla] Datapacks"))
        self.pushButton_10.setText(_translate("MainWindow", "Delete selected"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete all"))
        self.pushButton_11.setText(_translate("MainWindow", "Add datapack(s)"))
        self.label_30.setText(_translate("MainWindow", "Enabled only for Vanilla servers"))
        self.pluginsBox.setTitle(_translate("MainWindow", "Plugins"))
        self.pushButton_17.setText(_translate("MainWindow", "Delete all"))
        self.pushButton_15.setText(_translate("MainWindow", "Add plugin(s)"))
        self.pushButton_16.setText(_translate("MainWindow", "Delete selected"))
        self.label_28.setText(_translate("MainWindow", "Enabled only for CraftBukkit/Spigot/PaperMC servers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Additions"))
        self.label_34.setText(_translate("MainWindow", "Create Server"))
        self.label_35.setText(_translate("MainWindow", "Keep in mind that if you would like to allow people outside of your network to play on your server, you should portforward with your internal IP."))
        self.label_36.setText(_translate("MainWindow", "Your internal IP: [unknown]"))
        self.pushButton_12.setToolTip(_translate("MainWindow", "https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/"))
        self.pushButton_12.setText(_translate("MainWindow", "How to portforward"))
        self.readyText.setText(_translate("MainWindow", "Ready to make your Vanilla server? Select a folder and click \'Create server\'."))
        self.readyText_2.setText(_translate("MainWindow", "Folder:"))
        self.directory.setPlaceholderText(_translate("MainWindow", "Select a directory to install in"))
        self.pushButton_13.setText(_translate("MainWindow", "Select folder"))
        self.create.setText(_translate("MainWindow", "Create server"))
        self.progress.setText(_translate("MainWindow", "Progress: Inactive"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Create Server"))
        self.label_29.setText(_translate("MainWindow", "Server Creator"))


@QtCore.pyqtSlot()
def wrapperChange(self):
    global wrapper
    wrapper = str(ui.type.currentText())
    if wrapper == 'Vanilla':
        ui.pluginsBox.setEnabled(False)
        ui.datapacksBox.setEnabled(True)
    elif wrapper == 'Forge':
        if ctypes.windll.user32.MessageBoxW(0, 'Forge is already automated and has an installer. Would you like to go to the download page?', 'Forge', 4) == 6:
            webbrowser.open('https://files.minecraftforge.net/')
            ctypes.windll.user32.MessageBoxW(0, 'Make sure you select server in the installer.', 'Help', 0)
            sys.exit()
    else:
        ui.pluginsBox.setEnabled(True)
        ui.datapacksBox.setEnabled(False)
    ui.readyText.setText(f"Ready to make your {wrapper} server? Select a folder and click 'Create server'.")
    changeVersions(wrapper)

@QtCore.pyqtSlot()
def usernameChange(self):
    pass


@QtCore.pyqtSlot()
def minimumRAMChange(self):
    ui.maximumRAM.setMinimum(ui.minimumRAM.value())


@QtCore.pyqtSlot()
def checkboxesOff(self):
    ui.checkBox.setChecked(False)
    ui.checkBox_2.setChecked(False)
    ui.checkBox_3.setChecked(False)
    ui.checkBox_4.setChecked(False)
    ui.checkBox_5.setChecked(False)
    ui.checkBox_6.setChecked(False)
    ui.checkBox_7.setChecked(False)
    ui.checkBox_8.setChecked(False)
    ui.checkBox_9.setChecked(False)
    ui.checkBox_10.setChecked(False)
    ui.checkBox_11.setChecked(False)


@QtCore.pyqtSlot()
def checkboxesOn(self):
    ui.checkBox.setChecked(True)
    ui.checkBox_2.setChecked(True)
    ui.checkBox_3.setChecked(True)
    ui.checkBox_4.setChecked(True)
    ui.checkBox_5.setChecked(True)
    ui.checkBox_6.setChecked(True)
    ui.checkBox_7.setChecked(True)
    ui.checkBox_8.setChecked(True)
    ui.checkBox_9.setChecked(True)
    ui.checkBox_10.setChecked(True)
    ui.checkBox_11.setChecked(True)


@QtCore.pyqtSlot()
def whitelistAdd(self):
    global whitelist
    if 3 <= len(ui.whitelistAdd.text()) <= 16:
        ui.whitelist.addItem(ui.whitelistAdd.text())
        whitelist.append(ui.whitelistAdd.text())
        ui.whitelistAdd.setText('')
    elif not ui.whitelistAdd.text() == '':
        ctypes.windll.user32.MessageBoxW(0, 'Invalid username: Too long/short', 'Invalid username', 16)


@QtCore.pyqtSlot()
def whitelistDelete(self):
    global whitelist
    selected = ui.whitelist.selectedItems()
    if len(selected) >= 1:
        for item in selected:
            whitelist.remove(ui.whitelist.currentItem().text())
            ui.whitelist.takeItem(ui.whitelist.row(item))


@QtCore.pyqtSlot()
def whitelistClear(self):
    global whitelist
    if len(whitelist) > 0:
        if ctypes.windll.user32.MessageBoxW(0, f'Are you sure? You will delete {len(whitelist)} player(s) from the whitelist.', 'Confirm deletion', 4) == 6:
            whitelist = []
            ui.whitelist.clear()


@QtCore.pyqtSlot()
def OPsAdd(self):
    global ops
    if 3 <= len(ui.opsAdd.text()) <= 16:
        ui.ops.addItem(ui.opsAdd.text())
        ops.append(ui.opsAdd.text())
        ui.opsAdd.setText('')
    elif not ui.opsAdd.text() == '':
        ctypes.windll.user32.MessageBoxW(0, 'Invalid username: Too long/short', 'Invalid username', 16)


@QtCore.pyqtSlot()
def OPsDelete(self):
    global ops
    selected = ui.ops.selectedItems()
    if len(selected) >= 1:
        for item in selected:
            ops.remove(ui.ops.currentItem().text())
            ui.ops.takeItem(ui.ops.row(item))


@QtCore.pyqtSlot()
def OPsClear(self):
    global ops
    if len(ops) > 0:
        if ctypes.windll.user32.MessageBoxW(0, f'Are you sure? You will delete {len(ops)} operators.', 'Confirm deletion', 4) == 6:
            ops = []
            ui.ops.clear()


@QtCore.pyqtSlot()
def datapacksAdd(self):
    global datapacks
    files = easygui.fileopenbox(msg='Select datapacks', default=f'C:/users/{getuser()}/Downloads/', filetypes=['*.zip', '*.*'], title='Sylleris Datapacks', multiple=True)
    if files:
        for datapack in files:
            datapacks.append(datapack)
            ui.datapacks.addItem(datapack)


@QtCore.pyqtSlot()
def datapacksClear(self):
    global datapacks
    if len(datapacks) > 0:
        if ctypes.windll.user32.MessageBoxW(0, f'Are you sure? You will delete {len(datapacks)} datapacks.', 'Confirm deletion', 4) == 6:
            datapacks = []
            ui.datapacks.clear()


@QtCore.pyqtSlot()
def datapacksDelete(self):
    global datapacks
    selected = ui.datapacks.selectedItems()
    if len(selected) >= 1:
        for item in selected:
            datapacks.remove(ui.datapacks.currentItem().text())
            ui.datapacks.takeItem(ui.datapacks.row(item))


@QtCore.pyqtSlot()
def pluginsAdd(self):
    global plugins
    files = easygui.fileopenbox(msg='Select plugins', default=f'C:/users/{getuser()}/Downloads/', filetypes=['*.jar', '*.*'], title='Sylleris plugins', multiple=True)
    if files:
        for datapack in files:
            plugins.append(datapack)
            ui.plugins.addItem(datapack)


@QtCore.pyqtSlot()
def pluginsDelete(self):
    global plugins
    selected = ui.plugins.selectedItems()
    if len(selected) >= 1:
        for item in selected:
            plugins.remove(ui.plugins.currentItem().text())
            ui.plugins.takeItem(ui.plugins.row(item))


@QtCore.pyqtSlot()
def pluginsClear(self):
    global plugins
    if len(plugins) > 0:
        if ctypes.windll.user32.MessageBoxW(0, f'Are you sure? You will delete {len(plugins)} plugins.', 'Confirm deletion', 4) == 6:
            plugins = []
            ui.plugins.clear()


@QtCore.pyqtSlot()
def portforward(self):
    webbrowser.open_new_tab("https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/")


@QtCore.pyqtSlot()
def selectFolder(self):
    global serverDir
    serverDir = easygui.diropenbox(msg='Open server folder', title='Sylleris', default=f'c:/users/{getuser()}/Desktop/')
    if serverDir is None:
        serverDir = ''
        return
    if len(os.listdir(serverDir)) > 0:
        if ctypes.windll.user32.MessageBoxW(0, f'This directory already has folders/items in it. Are you sure?\n(You chose {serverDir})', 'Contents exist', 4) != 6:
            serverDir = ''
            return
    ui.directory.setText(serverDir)


@QtCore.pyqtSlot()
def createServer(self):
    global installStatus
    ui.warning.setText('')
    warnings = getProblems()
    if len(warnings) > 0:
        warningsStr = "\n".join(warnings)
        ui.warning.setText(f"Warnings ({len(warnings)}): " + ', '.join(warnings))
        ctypes.windll.user32.MessageBoxW(0, f'There are some problems:\n{warningsStr}', 'Warnings', 16)
        return

    ui.tabWidget.setEnabled(False)
    now = datetime.datetime.now()
    timestamp = f'{calendar.day_name[now.today().weekday()][:3]} {calendar.month_name[now.month][:3]} {now.hour}:{now.minute}:{now.second} GMT {now.year}'
    try:
        data = getData()
        print(data)
        data['timestamp'] = timestamp
        ui.progress.setText(f'Progress: Starting {data["wrapper"]} server setup..')
        installStatus = 'installing'
        installThread = Thread(target=globals()[f'install{data["wrapper"]}'], args=(data,))
        installThread.start()
        while not installStatus == 'finished':
            time.sleep(0.1)
        installStatus = 'inactive'
        ctypes.windll.user32.MessageBoxW(0, 'Server successfully created!', 'Success', 64)
    except:
        ctypes.windll.user32.MessageBoxW(0, f'Critical error while creating server: {traceback.format_exc()}', 'Error', 16)

    ui.tabWidget.setEnabled(True)
    ui.progress.setText('Progress: Inactive')
    ui.currentAction.setText('')


def createFile(path):
    Path(path).touch()


def installSpigot(data):
    global installStatus
    installStatus = 'installing'

    def createSpigotFiles(data):
        try:
            os.mkdir(f'{data["directory"]}/plugins')
        except:
            pass

    def downloadServerJar(data):
        url = next(item for item in versions['Spigot'] if item["id"] == data['version'])['url']
        with open(data['directory'] + '/server.jar', 'wb') as f:
            f.write(requests.get(url).content)

    currentDir = '/'.join(sys.argv[0].split('\\')[:-1])

    actions = [
        {'name': 'Creating items..', 'run': createItems},
        {'name': 'Creating Spigot items..', 'run': createSpigotFiles},
        {'name': 'Editing items..', 'run': editItems},
        {'name': f'Downloading {data["wrapper"]} {data["version"]} server..', 'run': downloadServerJar},
        {'name': 'Configuring server files..', 'run': settingsEditFiles},
        {'name': 'Setting up main server files..', 'run': establishServerFiles},
        {'name': 'Installing plugins..', 'run': installPlugins}
        ]

    c = 0
    for action in actions:
        c += 1
        ui.progress.setText(f'Progress: Active ({c}/{len(actions)})')
        print(f'Progress: Active ({c}/{len(actions)})', action['name'])
        ui.currentAction.setText(action['name'])
        ui.progress.repaint()
        ui.currentAction.repaint()
        action['run'](data)
        time.sleep(0.2)
        os.chdir(currentDir)

    ui.currentAction.setText('Completed setup.')
    ui.currentAction.repaint()
    installStatus = 'finished'

def installCraftBukkit(data):
    global installStatus
    installStatus = 'installing'

    def createCraftBukkitFiles(data):
        try:
            os.mkdir(f'{data["directory"]}/plugins')
        except:
            pass

    def downloadServerJar(data):
        url = next(item for item in versions['CraftBukkit'] if item["id"] == data['version'])['url']
        with open(data['directory'] + '/server.jar', 'wb') as f:
            f.write(requests.get(url).content)

    currentDir = '/'.join(sys.argv[0].split('\\')[:-1])

    actions = [
        {'name': 'Creating items..', 'run': createItems},
        {'name': 'Creating CraftBukkit items..', 'run': createCraftBukkitFiles},
        {'name': 'Editing items..', 'run': editItems},
        {'name': f'Downloading {data["wrapper"]} {data["version"]} server..', 'run': downloadServerJar},
        {'name': 'Configuring server files..', 'run': settingsEditFiles},
        {'name': 'Setting up main server files..', 'run': establishServerFiles},
        {'name': 'Installing plugins..', 'run': installPlugins}
        ]

    c = 0
    for action in actions:
        c += 1
        ui.progress.setText(f'Progress: Active ({c}/{len(actions)})')
        print(f'Progress: Active ({c}/{len(actions)})', action['name'])
        ui.currentAction.setText(action['name'])
        ui.progress.repaint()
        ui.currentAction.repaint()
        action['run'](data)
        time.sleep(0.2)
        os.chdir(currentDir)

    ui.currentAction.setText('Completed setup.')
    ui.currentAction.repaint()
    installStatus = 'finished'

def installPaperMC(data):
    global installStatus
    installStatus = 'installing'

    def createPaperFiles(data):
        try:
            os.mkdir(f'{data["directory"]}/plugins')
        except:
            pass

    def downloadServerJar(data):
        url = next(item for item in versions['PaperMC'] if item["id"] == data['version'])['url']
        with open(data['directory'] + '/server.jar', 'wb') as f:
            f.write(requests.get(url).content)

    currentDir = '/'.join(sys.argv[0].split('\\')[:-1])

    actions = [
        {'name': 'Creating items..', 'run': createItems},
        {'name': 'Creating Paper items..', 'run': createPaperFiles},
        {'name': 'Editing items..', 'run': editItems},
        {'name': f'Downloading {data["wrapper"]} {data["version"]} server..', 'run': downloadServerJar},
        {'name': 'Configuring server files..', 'run': settingsEditFiles},
        {'name': 'Setting up main server files..', 'run': establishServerFiles},
        {'name': 'Installing plugins..', 'run': installPlugins}
        ]

    c = 0
    for action in actions:
        c += 1
        ui.progress.setText(f'Progress: Active ({c}/{len(actions)})')
        print(f'Progress: Active ({c}/{len(actions)})', action['name'])
        ui.currentAction.setText(action['name'])
        ui.progress.repaint()
        ui.currentAction.repaint()
        action['run'](data)
        time.sleep(0.2)
        os.chdir(currentDir)

    ui.currentAction.setText('Completed setup.')
    ui.currentAction.repaint()
    installStatus = 'finished'


def establishServerFiles(data, eulaMade = False):
    stopPhrases = ['Timings reset',
    'Stopping server',
    'You need to agree to the EULA in order to run the server.',
    'Time elapsed: ',
    'For help, type "help"']
    if eulaMade:
        ui.currentAction.setText('Setting up Bukkit/Spigot server files..')
        ui.currentAction.repaint()
    os.chdir(data["directory"])
    executable = f'java -XX:+UseG1GC -Xmx2G -Xms2G -jar "{data["directory"]}/server.jar" nogui'
    server = subprocess.Popen(executable, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    while True:
        output = server.stdout.readline().decode()
        if len(output) > 3 and True:
            print(output.strip('\n'))
        for ph in stopPhrases:
            if ph in output:
                server.stdin.write(bytes('stop' + "\r\n", "ascii"))
                server.stdin.flush()
                time.sleep(3)
                break
    if not eulaMade:
        with open(f'{data["directory"]}/eula.txt', 'r') as f:
            tmp = f.read().replace('false', 'true')
        with open(f'{data["directory"]}/eula.txt', 'w') as f:
            f.write(tmp)
        establishServerFiles(data, eulaMade=True)
    else:
        return

def installPlugins(data):
    if len(data['plugins']) > 0:
        for plugin in data['plugs']:
            name = plugin.split('\\')[-1]
            moveFile(plugin, f'{data["directory"]}/plugins/{name}')

def settingsEditFiles(data):
    whitelist = []
    for player in data['whitelist']:
        try:
            link = 'https://api.mojang.com/users/profiles/minecraft/' + player
            dataL = requests.get(link).text()
            whitelist.append({'uuid': dataL['id'], 'name': player})
        except:
            pass

    ops = []
    for player in data['ops']:
        try:
            link = 'https://api.mojang.com/users/profiles/minecraft/' + player
            dataL = requests.get(link).text()
            whitelist.append({'uuid': dataL['id'], 'name': player, 'level': 4, 'bypassesPlayerLimit': False})
        except:
            pass

    with open(data['directory'] + '/whitelist.json', 'w') as f:
        f.write(json.dumps(whitelist, indent=4))
    with open(data['directory'] + '/ops.json', 'w') as f:
        f.write(json.dumps(ops, indent=4))

def createItems(data):
    try:
        os.mkdir(f'{data["directory"]}/logs')
    except:
        pass
    try:
        os.mkdir(f'{data["directory"]}/{data["worldName"]}')
    except:
        pass
    try:
        os.mkdir(f'{data["directory"]}/{data["worldName"]}/datapacks')
    except:
        pass
    createFile(f'{data["directory"]}/server.properties')
    createFile('banned-ips.json')
    createFile('banned-players.json')
    createFile('ops.json')
    createFile('whitelist.json')

    if data['generateBatchFile']:
        createFile(f'{data["directory"]}/start.bat')
        with open(f'{data["directory"]}/start.bat', 'w') as f:
            f.write(f'''@echo off
java -XX:+UseG1GC -Xmx{data["ram"][1]}G -Xms{data["ram"][0]}G -jar server.jar nogui''')

def editItems(data):
    with open(data['directory'] + '/usercache.json', 'w') as f:
        f.write('[]')
    with open(data['directory'] + '/banned-players.json', 'w') as f:
        f.write('[]')
    with open(data['directory'] + '/banned-ips', 'w') as f:
        f.write('[]')

    with open(data['directory'] + '/server.properties', 'w') as f:
        f.write(f'''#Minecraft server properties
#{data['timestamp']}
spawn-protection=16
max-tick-time=60000
query.port={data["port"]}
generator-settings=
force-gamemode=false
allow-nether={data["allowNether"]}
enforce-whitelist={data["enforceWhitelist"]}
gamemode={data["gamemode"]}
broadcast-console-to-ops=true
enable-query=false
player-idle-timeout=0
difficulty={data["difficulty"]}
broadcast-rcon-to-ops=true
spawn-monsters={data["spawnMonsters"]}
op-permission-level=4
pvp={data["playerPvP"]}
snooper-enabled={data["snooper"]}
level-type={data["levelType"]}
hardcore=false
enable-command-block={data["commandBlocks"]}
network-compression-threshold=256
max-players={data["slots"]}
max-world-size=29999984
resource-pack-sha1=
function-permission-level=2
rcon.port=25575
server-port={data["port"]}
server-ip={internalIP}
spawn-npcs={data["spawnNPCs"]}
allow-flight={data["allowFlight"]}
level-name={data["worldName"]}
view-distance=8
resource-pack=
spawn-animals={data["spawnAnimals"]}
white-list={data["enforceWhitelist"]}
rcon.password=
generate-structures={data["generateStructures"]}
online-mode={data["onlineMode"]}
max-build-height=256
level-seed={data["worldSeed"]}
prevent-proxy-connections=false
use-native-transport=true
motd={data["MOTD"]}
enable-rcon=false
''')


def installVanilla(data):
    global installStatus
    installStatus = 'installing'

    def downloadServerJar(data):
        url = next(item for item in versions['Vanilla'] if item["id"] == data['version'])['url']
        v = json.loads(requests.get(url).text)['downloads']['server']['url']
        with open(data['directory'] + '/server.jar', 'wb') as f:
            f.write(requests.get(v).content)


    def doAdditions(data):
        for datapack in data['datapacks']:
            tmpDatapackName = datapack.split('\\')[-1]
            moveFile(datapack, f'{data["directory"]}/{data["worldName"]}/datapacks/{tmpDatapackName}')


    def testServerConnection(data):
        # global data
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((data['ip'], int(data['port'])))
            s.close()
            return True
        except OverflowError:
            ctypes.windll.user32.MessageBoxW(0, f'Port {data["port"]} is not usable. Using port 25565 instead.', 'Port modified', 16)
            data['port'] = 25565
            return False
        except OSError as e:
            if str(e) == '[WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted':
                newPort = 0
                msg = f'Port {data["port"]} is already used, select another one between 1-65535'
                while newPort == 0 or not (not 1 <= newPort <= 65535):
                    try:
                        newPort = int(easygui.enterbox(msg=msg, title='Sylleris', default='25565'))
                        msg = f'Port {data["port"]} is already used, select another one between 1-65535'
                    except:
                        msg = f'Invalid port.\n\nPort {data["port"]} is already used, select another one between 1-65535'
                data['port'] = newPort
            else:
                ctypes.windll.user32.MessageBoxW(0, f'Port {data["port"]} is not usable. Using port 25565 instead.', 'Port modified', 16)
                data['port'] = 25565
            return False


    actions = [
        {'name': 'Creating items..', 'run': createItems},
        {'name': 'Editing items..', 'run': editItems},
        {'name': f'Downloading {data["wrapper"]} {data["version"]} server..', 'run': downloadServerJar},
        {'name': 'Configuring server..', 'run': settingsEditFiles},
        {'name': 'Adding datapacks..', 'run': doAdditions}
    ]

    timestamp = data['timestamp']

    c = 0
    for action in actions:
        c += 1
        ui.progress.setText(f'Progress: Active ({c}/{len(actions)})')
        print(f'Progress: Active ({c}/{len(actions)})', action['name'])
        ui.currentAction.setText(action['name'])
        ui.progress.repaint()
        ui.currentAction.repaint()
        action['run'](data)
        time.sleep(0.2)

    connectionWorks = False
    while not connectionWorks:
        connectionWorks = testServerConnection(data)

    ui.currentAction.setText('Completed setup.')
    ui.currentAction.repaint()
    installStatus = 'finished'


def getData():
    data = {}
    data['wrapper'] = ui.type.currentText()
    data['version'] = ui.version.currentText()
    data['username'] = ui.username.text()
    data['ram'] = (int(ui.minimumRAM.value()), int(ui.maximumRAM.value()))
    data['acceptEULA'] = ui.acceptEula.isChecked()
    data['generateBatchFile'] = ui.acceptEula_2.isChecked()

    data['allowNether'] = ui.checkBox.isChecked()
    data['enforceWhitelist'] = ui.checkBox_2.isChecked()
    data['spawnMonsters'] = ui.checkBox_3.isChecked()
    data['allowFlight'] = ui.checkBox_7.isChecked()
    data['spawnAnimals'] = ui.checkBox_8.isChecked()
    data['generateStructures'] = ui.checkBox_9.isChecked()
    data['onlineMode'] = ui.checkBox_10.isChecked()
    data['snooper'] = ui.checkBox_11.isChecked()
    data['playerPvP'] = ui.checkBox_4.isChecked()
    data['commandBlocks'] = ui.checkBox_5.isChecked()
    data['spawnNPCs'] = ui.checkBox_6.isChecked()

    data['gamemode'] = ui.gamemode.currentText().lower()
    data['difficulty'] = ui.difficulty.currentText().lower()
    data['levelType'] = ui.levelType.text()
    data['slots'] = ui.playerSlots.value()
    data['ip'] = internalIP
    data['port'] = ui.port.text()
    data['worldName'] = ui.worldName.text()
    if data['worldName'] == '':
        data['worldName'] = 'world'
    data['worldSeed'] = ui.seed.text()
    data['MOTD'] = ui.motd.text()

    data['whitelist'] = whitelist
    data['ops'] = ops
    data['datapacks'] = datapacks
    data['plugins'] = plugins

    data['directory'] = ui.directory.text()

    return data


def getProblems():
    print(datapacks)
    print(plugins)
    warnings = []
    if wrapper == 'Forge':
        warnings.append('Forge already has an installer you can use.')
        return warnings

    if not (3 <= len(ui.username.text()) <= 16):
        warnings.append(f'Username {ui.username.text()} is too short/long')

    if ui.minimumRAM.value() == totalRAM:
        warnings.append('Allocating 100% of your memory leaves no memory for the Operating System - Not suggested.')

    for datapack in datapacks:
        if not datapack.endswith('.zip'):
            warnings.append(f'{datapack} is not a ZIP file.')

    for plugin in plugins:
        if not plugin.endswith('.jar'):
            if plugin.endswith('.zip') or plugin.endswith('.rar'):
                warnings.append(f'({plugin}) Is an archive, take the .JAR files out.')
            else:
                warnings.append(f'{plugin} is not a .jar file')

    if not os.path.isdir(ui.directory.text()):
        if serverDir.replace(' ', '') == '':
            warnings.append('No selected folder to install the server in.')
        else:
            warnings.append(f'{serverDir} does not exist')

    return warnings


def changeVersions(wrapper):
    ui.version.clear()
    for ver in versions[wrapper]:
        ui.version.addItem(ver['id'])


# global
wrapper = 'Vanilla'
whitelist = []
ops = []
datapacks = []
plugins = []
serverDir = ''
installStatus = 'inactive'

eula = '''#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).
#{}
eula={}
'''

if platform.system() != 'Windows':
    sys.exit(ctypes.windll.user32.MessageBoxW(0, f'This program is not compatible with {platform.system()}. Please use Windows.', 'Incompatible OS', 16))

currentVersion = '1.0.0'

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

totalRAM = round(virtual_memory().total / 1000000000)
ui.ramTip.setText(f'Tip: You have {totalRAM} GB of RAM.')
ui.minimumRAM.setMaximum(totalRAM)
ui.maximumRAM.setMaximum(totalRAM)

internalIP = socket.gethostbyname(socket.gethostname())
ui.label_36.setText(f'Your internal IP: {internalIP}')
ui.create.setEnabled(True)

update = requests.get('https://pastebin.com/raw/hqd6a35e').text
if not update == 'ignore':
    updateVersion, updateURL = update.split(';;')
    if version.parse(updateVersion) > version.parse(currentVersion):
        if ctypes.windll.user32.MessageBoxW(0, f'A newer version ({updateVersion}) is available. You are using {currentVersion}.\nDo you want to install it?', 'Update available', 68) == 6:
            webbrowser.open(updateURL)
            sys.exit()

versions = versionScraper.getVersions()
changeVersions('Vanilla')

subprocess.run('taskkill /fi "WINDOWTITLE eq SYLLERIS-LOADING"', shell=True, creationflags=0x80000000)

MainWindow.show()
returnCode = app.exec_()
sys.exit(returnCode)
