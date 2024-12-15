import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QLabel,QPushButton,QGridLayout,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt 
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 300)
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

        buttons = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9, self.button0, self.buttonMinus, self.buttonPlus, self.buttonMultiply, self.buttonDivide]
        
        for button in buttons:
            button.clicked.connect(self.buttonClicked)

        self.buttonClear.clicked.connect(self.buttonClearClicked)
        self.buttonEqual.clicked.connect(self.buttonEqualClicked)
        self.buttonDot.clicked.connect(self.buttonDotClicked)
        self.buttonDEL.clicked.connect(self.buttonDELClicked)

        self.initUI()

    def buttonClicked(self):
        clicked_button = self.sender()
        self.label.setText(self.label.text()+clicked_button.text())
    
    def buttonClearClicked(self):
        self.label.setText("")

    def buttonEqualClicked(self):
        try:
            result = eval(self.label.text())
            self.label.setText(str(result))
        except ZeroDivisionError:
            self.label.setText("Cannot divide by zero")
        except SyntaxError:
            self.label.setText("Invalid syntax")
        except Exception:
            self.label.setText("Error!")

    def buttonDotClicked(self):
        if self.label.text() and self.label.text()[-1] != ".":
            self.label.setText(self.label.text() + ".")

    def buttonDELClicked(self):
        if self.label.text():
            self.label.setText(self.label.text()[:-1])

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        glayout = QGridLayout()
        glayout.addWidget(self.button7, 0, 0)
        glayout.addWidget(self.button8, 0, 1)
        glayout.addWidget(self.button9, 0, 2)
        glayout.addWidget(self.buttonClear, 0, 3)
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
        hbox.addWidget(self.buttonDEL)
        hbox.addWidget(self.buttonEqual)

        
        main_layout = QVBoxLayout() 
        main_layout.addWidget(self.label)
        main_layout.addLayout(glayout)
        main_layout.addLayout(hbox)

        central_widget.setLayout(main_layout)

        self.setStyleSheet("""
        QPushButton {
            font-size: 30px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #e0e0e0;
        }

        QPushButton:pressed {
            background-color: #d0d0d0;
        }

        QLabel {
            font-size: 30px;
            font-weight: bold;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        """)

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()