from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mwidget = QtWidgets.QMainWindow()
        self.mwidget.setObjectName("MainWindow")
        self.resize(330, 295)
        self.setFixedSize(330, 296) # Use
        self.center() # Use
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Use
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(170, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(55, 140, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.mwidget.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.mwidget)
        QtCore.QMetaObject.connectSlotsByName(self.mwidget)
        self.oldPos = self.mwidget.pos() # Use

        self.show()

    def center(self):
        qr = self.mwidget.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.mwidget.move(qr.topLeft())

    def mousePressEvent(self, event):
        print('[PRESS]')
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        print('[MOVE]')
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.mwidget.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())
