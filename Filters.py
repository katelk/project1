from PIL import Image
-------------------------------
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("1.bmp")
        
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        
        btn = QPushButton('Заменить картинку', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.action)
    
        hbox.addWidget(self.lbl)
        hbox.addWidget(btn)
        self.setLayout(hbox)        
        self.move(300, 200)
        self.setWindowTitle('Замена')
        self.show()        

    def action(self):
        self.lbl.setPixmap(QPixmap("2.bmp"))       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
    ------------------------------------------------
