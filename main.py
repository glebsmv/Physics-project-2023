import sys
import math

from PyQt5 import QtWidgets as qw
from united_in_grief import Ui_MainWindow
from graph import Ui_Form


class Graph(qw.QMainWindow, Ui_Form):
    def __init__(self, h0, l0, v0, a0, vet, type):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('График')
        self.setFixedSize(500, 500)
        self.widget.clear()
        a = a0 * math.pi / 180
        g = 9.8
        vx = v0 * math.cos(a) + vet
        v0y = v0 * math.sin(a)
        vy = v0y
        y = 1
        x = l0
        m = 0.1 ** 5
        X = []
        Y = []
        while y > 0:
            if m == 0:
                continue
            y = h0 + (v0y * m) - (g * (m ** 2) / 2)
            x = l0 + vx * m
            l = vx * m
            vy = v0 * math.sin(a) - g * m
            if type == 1:
                X.append(x)
                Y.append(y)
            elif type == 2:
                X.append(m)
                Y.append(vx)
            elif type == 3:
                X.append(m)
                Y.append(vy)
            elif type == 4:
                X.append(m)
                Y.append(x)
            elif type == 5:
                X.append(m)
                Y.append(y)
            elif type == 6:
                X.append(m)
                Y.append(l)
            m += 0.1 ** 5

        self.widget.plot(X, Y, pen='g')


class Project(qw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Моделирование баллистического движения')
        self.setFixedSize(850, 600)
        self.vet.setDisabled(True)
        self.da.clicked.connect(self.da_net)
        self.net.clicked.connect(self.da_net)
        self.traect.clicked.connect(self.boom)
        self.paceOX.clicked.connect(self.boom)
        self.paceOY.clicked.connect(self.boom)
        self.traectOX.clicked.connect(self.boom)
        self.traectOY.clicked.connect(self.boom)
        self.flight.clicked.connect(self.boom)

    def da_net(self):
        if self.sender() == self.da:
            self.vet.setDisabled(False)
            self.label.setText('Скорость ветра')
        else:
            self.label.setText('Ветра нет')
            self.vet.setDisabled(True)
            self.vet.setValue(0)

    def boom(self):
        a = 1
        if self.v0.value() == 0:
            msg = qw.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Начальная скорость равна 0")
            msg.setIcon(qw.QMessageBox.Warning)
            msg.exec_()
        elif self.a0.value() > 90:
            msg = qw.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Угол больше 90 градусов")
            msg.setIcon(qw.QMessageBox.Warning)
            msg.exec_()
        elif self.a0.value() == 90:
            msg = qw.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Угол равен 90 градусам")
            msg.setIcon(qw.QMessageBox.Warning)
            msg.exec_()
        elif self.a0.value() == 0:
            msg = qw.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Угол равен 0 градусов")
            msg.setIcon(qw.QMessageBox.Warning)
            msg.exec_()
        elif self.da.isChecked() == False and self.net.isChecked() == False:
            msg = qw.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Вы не выбрали, есть ли ветер")
            msg.setIcon(qw.QMessageBox.Warning)
            msg.exec_()
        elif self.da.isChecked() == True and self.vet.value() == 0:
            msg = qw.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Скорость ветра равен 0 градусов")
            msg.setIcon(qw.QMessageBox.Warning)
            msg.exec_()
        else:
            h0 = self.h0.value()
            l0 = self.l0.value()
            v0 = self.v0.value()
            a0 = self.a0.value()
            vet = self.vet.value()
            types = {self.traect: 1, self.paceOX: 2, self.paceOY: 3, self.traectOX: 4, self.traectOY: 5, self.flight: 6}
            type = types[self.sender()]
            self.gr = Graph(h0, l0, v0, a0, vet, type)
            self.gr.show()


if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec_())
