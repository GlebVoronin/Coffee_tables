import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(275, 490, 250, 30))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "создать окружности"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.values = 0, 0, 0
        self.color = QColor(0, 0, 0)
        self.pushButton.clicked.connect(self.flag_activate)

    def draw_yellow_circles(self):
        if self.flag:
            x, y, size = randint(40, 760), randint(40, 560), randint(3, 60)
            self.values = x, y, size
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            self.color = QColor(r, g, b)
        self.qp.setBrush(self.color)
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
