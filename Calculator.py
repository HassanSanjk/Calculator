import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QLabel,QPushButton,QGridLayout,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt 
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 500)
        self.label = QLabel("", self)
        self.button1 = QPushButton("1", self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.button4 = QPushButton("4", self)
        self.button5 = QPushButton("5", self)
        self.button6 = QPushButton("6", self)
        self.button7 = QPushButton("7", self)
        self.button8 = QPushButton("8", self)
        self.button9 = QPushButton("9", self)
        self.button0 = QPushButton("0", self)
        self.buttonMinus = QPushButton("-", self)
        self.buttonPlus = QPushButton("+", self)
        self.buttonMultiply = QPushButton("*", self)
        self.buttonDivide = QPushButton("/", self)
        self.buttonClear = QPushButton("Clear", self)
        self.buttonEqual = QPushButton("=", self)
        self.buttonDot = QPushButton(".", self)
        self.buttonDEL = QPushButton("DEL",self)

        """
        self.button1.clicked.connect(self.button1Clicked)
        self.button2.clicked.connect(self.button2Clicked)
        self.button3.clicked.connect(self.button3Clicked)
        self.button4.clicked.connect(self.button4Clicked)
        self.button5.clicked.connect(self.button5Clicked)
        self.button6.clicked.connect(self.button6Clicked)
        self.button7.clicked.connect(self.button7Clicked)
        self.button8.clicked.connect(self.button8Clicked)
        self.button9.clicked.connect(self.button9Clicked)
        self.button0.clicked.connect(self.button0Clicked)
        

        self.buttonMinus.clicked.connect(self.buttonMinusClicked)
        self.buttonPlus.clicked.connect(self.buttonPlusClicked)
        self.buttonMultiply.clicked.connect(self.buttonMultiplyClicked)
        self.buttonDivide.clicked.connect(self.buttonDivideClicked)
        self.buttonClear.clicked.connect(self.buttonClearClicked)
        self.buttonEqual.clicked.connect(self.buttonEqualClicked)
        self.buttonDot.clicked.connect(self.buttonDotClicked)
        self.buttonDEL.clicked.connect(self.buttonDELClicked)
        """
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        glayout = QGridLayout()
        glayout.addWidget(self.button7, 0, 0)
        glayout.addWidget(self.button8, 0, 1)
        glayout.addWidget(self.button9, 0, 2)
        glayout.addWidget(self.buttonDEL, 0, 3)
        glayout.addWidget(self.button4, 1, 0)
        glayout.addWidget(self.button5, 1, 1)
        glayout.addWidget(self.button6, 1, 2)
        glayout.addWidget(self.buttonPlus, 1, 3)
        glayout.addWidget(self.button1, 2, 0)
        glayout.addWidget(self.button2, 2, 1)
        glayout.addWidget(self.button3, 2, 2)
        glayout.addWidget(self.buttonMinus, 2, 3)
        glayout.addWidget(self.buttonDot, 3, 0)
        glayout.addWidget(self.button0, 3, 1)
        glayout.addWidget(self.buttonDivide, 3, 2)
        glayout.addWidget(self.buttonMultiply, 3, 3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.buttonClear)
        hbox.addWidget(self.buttonEqual)

        
        main_layout = QVBoxLayout() 
        main_layout.addWidget(self.label)
        main_layout.addLayout(glayout)
        main_layout.addLayout(hbox)

        central_widget.setLayout(main_layout)

        self.setStyleSheet("""
        
        """)

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()