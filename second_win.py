# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import  QApplication, QHBoxLayout, QLabel,\
    QVBoxLayout, QWidget, QPushButton, QRadioButton, QButtonGroup,\
    QMessageBox, QLineEdit, QLCDNumber
from instr import *
from final_win import FinalWin
from PyQt5.QtGui import QColor

class Experiment():
    def __init__(self, age, result1, result2, result3):
        self.age = age
        self.result1 = result1
        self.result2 = result2
        self.result3 = result3


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.name = QLabel(txt_name)
        self.age = QLabel(txt_age)
        self.test1 = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)
        self.input_name = QLineEdit(txt_hintname)
        self.input_age = QLineEdit(txt_hintage)
        self.input_test1 = QLineEdit(txt_hinttest1)
        self.input_test2 = QLineEdit(txt_hinttest2)
        self.input_test3 = QLineEdit(txt_hinttest3)
        self.start1 = QPushButton(txt_starttest1)
        self.start2 = QPushButton(txt_starttest2)
        self.start3 = QPushButton(txt_starttest3)
        self.results = QPushButton(txt_sendresults)
        # self.timer = QLabel('...')
        self.lcd = QLCDNumber() # !
        self.V1 = QVBoxLayout()
        self.V2 = QVBoxLayout()
        self.H = QHBoxLayout()
        self.V1.addWidget(self.name, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.input_name, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.age, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.input_age, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.test1, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.start1, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.input_test1, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.start2, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.start3, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.input_test2, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.input_test3, alignment = Qt.AlignLeft)
        self.V1.addWidget(self.results, alignment = Qt.AlignCenter)
        # self.V2.addWidget(self.lcd, alignment = Qt.AlignRight)
        self.H.addLayout(self.V1)
        self.H.addWidget(self.lcd)
        self.setLayout(self.H)

    def connects(self):
        self.results.clicked.connect(self.next)
        self.start1.clicked.connect(self.timer1)
        self.start2.clicked.connect(self.timer2)
        self.start3.clicked.connect(self.timer3)

    def next(self):
        self.hide()
        self.exp = Experiment(int(self.input_age.text()),
                              int(self.input_test1.text()), 
                              int(self.input_test2.text()), 
                              int(self.input_test3.text()))
        self.win3 = FinalWin(self.exp)

    def timer1(self):
        self.timer = QTimer()
        self.time = 15
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        self.time -= 1  
        self.lcd.display(self.time) 
        if self.time < 0:
            self.timer.stop()

    def timer2(self):
        self.timer = QTimer()
        self.time = 30
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1500)
    
    def timer3(self):
        self.timer = QTimer()
        self.time = 60
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        self.time -= 1  
        self.lcd.display(self.time)
        if self.time >= 45:
            self.lcd.setStyleSheet('color: rgb(150, 220, 35)')
        elif self.time <= 15:
            self.lcd.setStyleSheet('color: rgb(150, 220, 35)')
        else:
            self.lcd.setStyleSheet('color: rgb(0,0,0)')
        if self.time == 0:
            self.timer.stop()