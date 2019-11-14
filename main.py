import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database_way = 'coffee.sqlite'
        uic.loadUi('main.ui', self)
        data = self.get_data()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)
        self.titles = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                       'описание вкуса', 'цена', 'объем упаковки']
        for i, elem in enumerate(data):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def get_data(self):
        database = sqlite3.connect(self.database_way)
        cursor = database.cursor()
        new_data = []
        data = cursor.execute("""SELECT id, title, degree_of_roasting,
        type, description, price, volume FROM Coffee""").fetchall()
        for element in data:
            cursor = database.cursor()
            degree = cursor.execute(f"""SELECT title FROM Degree_of_roasting
            WHERE id = {element[2]}""").fetchone()[0]
            cursor = database.cursor()
            type_of_coffee = cursor.execute(f"""SELECT title FROM Types_of_coffee
            WHERE id = {element[3]}""").fetchone()[0]
            new_element = [element[0], element[1], degree, type_of_coffee,
                           element[4], element[5], element[6]]
            new_data.append(new_element)
        return new_data


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
