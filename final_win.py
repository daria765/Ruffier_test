from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QApplication, QLabel, QVBoxLayout, QWidget
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.conclusion = QLabel(txt_workheart + self.calculate_index())
        self.index_ = QLabel(txt_index + str(self.index))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.conclusion, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def calculate_index(self):
        if self.exp.age < 7:
            self.index = 0
            return txt_fail
        
        self.index = (4*(self.exp.result1 + self.exp.result2 + self.exp.result3)-200)/10

        if 7 <= self.exp.age <= 8:
            if self.index >= 21:
                return txt_res1
            elif 17 <= self.index < 21:
                return txt_res2
            elif 12 <= self.index < 17:
                return txt_res3
            elif 6.5 <= self.index < 12:
                return txt_res4
            else:
                return txt_res5

        elif 9 <= self.exp.age <= 10:
            if self.index >= 19.5:
                return txt_res1
            elif 15.5 <= self.index < 19.5:
                return txt_res2
            elif 10.5 <= self.index < 15.5:
                return txt_res3
            elif 5 <= self.index < 10.5:
                return txt_res4
            else:
                return txt_res5
            
        elif 11 <= self.exp.age <= 12:
            if self.index >= 18:
                return txt_res1
            elif 14 <= self.index < 18:
                return txt_res2
            elif 9 <= self.index < 14:
                return txt_res3
            elif 3.5 <= self.index < 9:
                return txt_res4
            else:
                return txt_res5    

        elif 13 <= self.exp.age <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif 12.5 <= self.index < 16.5:
                return txt_res2
            elif 7.5 <= self.index < 12.5:
                return txt_res3
            elif 2 <= self.index < 7.5:
                return txt_res4
            else:
                return txt_res5       

        else:
            if self.index >= 15:
                return txt_res1
            elif 11 <= self.index < 15:
                return txt_res2
            elif 6 <= self.index < 11:
                return txt_res3
            elif 0.5 <= self.index < 6:
                return txt_res4
            else:
                return txt_res5                    