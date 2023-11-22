from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QApplication, QHBoxLayout, QLabel,\
     QVBoxLayout, QWidget, QPushButton, QRadioButton, QButtonGroup,\
     QMessageBox
from instr import *
from second_win import TestWin

class MainWin(QWidget):
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
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment= Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next)

        
    def next(self):
        self.hide()
        self.win2 = TestWin()


app = QApplication([])
window = MainWin()
app.exec_()