from PIL import Image
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 260, 100)
        self.setWindowTitle('Редактор фотографий')
        
        self.label1 = QLabel(self)
        self.label1.setText("Добро пожаловать в редактор фотографий!")
        self.label1.move(20, 8)
        
        self.label2 = QLabel(self)
        self.label2.setText("Для начала работы введите имя файла:")
        self.label2.move(25, 25)
        
        self.name_file_input = QLineEdit(self)
        self.name_file_input.move(60, 45)
        
        self.btn = QPushButton('Приступить к работе', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(68, 70)
        self.btn.clicked.connect(self.action)
        
        
    def action(self):
        hbox = QVBoxLayout(self)
        self.label1.deleteLater()
        self.label2.deleteLater()
        self.btn.deleteLater()
        
        self.name_file_input.deleteLater()
        file = self.name_file_input.text()
        im = Image.open(file)
        im.thumbnail([500,500],Image.ANTIALIAS)
        im.save("j.jpg")
        pixmap = QPixmap("j.jpg")
        #os.remove("j.jpg")
        
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        hbox.addWidget(self.lbl)
        self.setLayout(hbox)
        
        self.btn_black_white = QPushButton('Черно-белый', self)
        self.btn_black_white.resize(self.btn2.sizeHint())
        self.btn_black_white.clicked.connect(self.black_white)
        hbox.addWidget(self.btn_black_white)
        
        self.move(300, 200)
        self.show() 
    def black_white(self):
        im2 = Image.open("j.jpg")
        pixels = im2.load()
        x, y = im2.size   
        for i in range(x):  
            for j in range(y):
                r, g, b = pixels[i, j]
                bw = (r + g + b) // 3
                pixels[i, j] = bw, bw, bw
        im2.save("j.jpg")
        pixmap = QPixmap("j.jpg")
        self.lbl.setPixmap(pixmap)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

