import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QApplication, qApp

from qroundprogressbar import QRoundProgressBar


app = QApplication(sys.argv)

progress = QRoundProgressBar()
progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)

# style accordingly via palette
palette = QPalette()
brush = QBrush(QColor(0, 0, 255))
brush.setStyle(Qt.SolidPattern)
palette.setBrush(QPalette.Active, QPalette.Highlight, brush)

progress.setPalette(palette)
progress.show()

# simulate delayed time that a process may take to execute
# from demonstration purposes only
for i in range(0, 100, 20):
    progress.setValue(i)
    qApp.processEvents()
    time.sleep(3)

sys.exit(app.exec_())
