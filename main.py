import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.values = 0, 0, 0
        self.pushButton.clicked.connect(self.flag_activate)

    def draw_yellow_circles(self):
        self.qp.setBrush(QColor(255, 255, 0))
        if self.flag:
            x, y, size = randint(40, 760), randint(40, 560), randint(3, 60)
            self.values = x, y, size
        self.qp.drawEllipse(self.values[0], self.values[1], self.values[2], self.values[2])

    def flag_activate(self):
        self.flag = True

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw_yellow_circles()
        self.qp.end()
        self.flag = False
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
