from SecondWindowUI import Ui_LoginWindow
from MainWindowUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Main_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    logged2 = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Main_Window, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switch)

    @QtCore.pyqtSlot()
    def switch(self):
        self.logged2.emit()
        self.close()


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    logged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.authenticate)

    @QtCore.pyqtSlot()
    def authenticate(self):
        self.logged.emit()
        self.close()

def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    w = Main_Window()
    login.logged.connect(w.show)
    w.logged2.connect(login.show)
    login.show()
    sys.exit(app.exec_())


if __name__ == '__main__': main()
