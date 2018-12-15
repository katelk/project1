from PIL import Image, ImageEnhance
import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout)
from PyQt5.QtWidgets import QInputDialog

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
        file = self.name_file_input.text()
        self.label1.deleteLater()
        self.label2.deleteLater()
        self.btn.deleteLater()  
        self.name_file_input.deleteLater()

        im = Image.open(file)
        im.thumbnail([500,500],Image.ANTIALIAS)
        im.save("j.jpg")
        pixmap = QPixmap("j.jpg")
        #os.remove("j.jpg")
        
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        hbox.addWidget(self.lbl)
        self.setLayout(hbox)
        
        self.btn_horizontal_reflection = QPushButton('Отразить по горизонтали', self)
        self.btn_horizontal_reflection.resize(self.btn_horizontal_reflection.sizeHint())
        self.btn_horizontal_reflection.clicked.connect(self.horizontal_reflection)
        hbox.addWidget(self.btn_horizontal_reflection)
        
        self.btn_vertical_reflection = QPushButton('Отразить по вертикали', self)
        self.btn_vertical_reflection.resize(self.btn_vertical_reflection.sizeHint())
        self.btn_vertical_reflection.clicked.connect(self.vertical_reflection)
        hbox.addWidget(self.btn_vertical_reflection)
        
        self.btn_black_white = QPushButton('Черно-белый', self)
        self.btn_black_white.resize(self.btn_black_white.sizeHint())
        self.btn_black_white.clicked.connect(self.black_white)
        hbox.addWidget(self.btn_black_white)
        
        self.btn_negative = QPushButton('Негатив', self)
        self.btn_negative.resize(self.btn_negative.sizeHint())
        self.btn_negative.clicked.connect(self.negative)
        hbox.addWidget(self.btn_negative)
        
        self.btn_contrast = QPushButton('Контрастность', self)
        self.btn_contrast.resize(self.btn_contrast.sizeHint())
        self.btn_contrast.clicked.connect(self.contrast)
        hbox.addWidget(self.btn_contrast)
        
        self.btn_saturation = QPushButton('Насыщенность', self)
        self.btn_saturation.resize(self.btn_saturation.sizeHint())
        self.btn_saturation.clicked.connect(self.saturation)
        hbox.addWidget(self.btn_saturation)
        
        self.btn_brightness = QPushButton(self)
        self.btn_brightness.setText("Яркость")
        self.btn_brightness.resize(self.btn_brightness.sizeHint())
        self.btn_brightness.clicked.connect(self.brightness)
        hbox.addWidget(self.btn_brightness)
        
        self.btn_noises = QPushButton('Зернистость', self)
        self.btn_noises.resize(self.btn_noises.sizeHint())
        self.btn_noises.clicked.connect(self.noises)
        hbox.addWidget(self.btn_noises)
        
        self.btn_negative = QPushButton('Цвета', self)
        self.btn_negative.resize(self.btn_negative.sizeHint())
        self.btn_negative.clicked.connect(self.negative)
        hbox.addWidget(self.btn_negative)
        
        self.btn_negative = QPushButton('Сохранить', self)
        self.btn_negative.resize(self.btn_negative.sizeHint())
        self.btn_negative.clicked.connect(self.negative)
        hbox.addWidget(self.btn_negative)
        
        self.move(300, 200)
        self.show() 
    
    def brightness(self):
        factor, okBtnPressed = QInputDialog.getInt(
            self, "Яркость", "Введите желаемый показатель яркости", 0, -100, 100, 1
        )
        if okBtnPressed:
            im2 = Image.open("j.jpg")
            pixels = im2.load()
            x, y = im2.size   
            for i in range(x):  
                for j in range(y):
                    r, g, b = pixels[i, j]
                    r1 = r + factor * 2.55
                    g1 = g + factor * 2.55
                    b1 = b + factor * 2.55
                    if r1 < 0:
                        r1 = 0
                    if g1 < 0:
                        g1 = 0
                    if b1 < 0:
                        b1 = 0
                    if r1 > 255:
                        r1 = 255
                    if g1 > 255:
                        g1 = 255
                    if b1 > 255:
                        b1 = 255
                    pixels[i, j] = int(r1), int(g1), int(b1)
            im2.save("j.jpg")
            pixmap = QPixmap("j.jpg")
            self.lbl.setPixmap(pixmap)
            
    def contrast(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "Контрастность", "Введите желаемый показатель контрастности", 0, -100, 100, 1
        )
        if okBtnPressed:
            im2 = Image.open("j.jpg")
            contrast = ImageEnhance.Contrast(im2)
            if i < 0:
                im2 = contrast.enhance(1 - ((i * (-1)) / 100))
            if i > 0:
                im2 = contrast.enhance(1 + (i / 100))
            if i == 0:
                im2 = contrast.enhance(1)
            im2.save("j.jpg")
            pixmap = QPixmap("j.jpg")
            self.lbl.setPixmap(pixmap)
            
    def saturation(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "Насыщенность", "Введите желаемый показатель насыщенности", 0, -100, 100, 1
        )
        if okBtnPressed:
            im2 = Image.open("j.jpg")
            converter = ImageEnhance.Color(im2)
            if i < 0:
                im2 = converter.enhance(1 - ((i * (-1)) / 100))
            if i > 0:
                im2 = converter.enhance(1 + (i / 100))
            if i == 0:
                im2 = converter.enhance(1)
            im2.save("j.jpg")
            pixmap = QPixmap("j.jpg")
            self.lbl.setPixmap(pixmap)
                
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
        
    def horizontal_reflection(self):
        im2 = Image.open("j.jpg")
        im2 = im2.transpose(Image.FLIP_LEFT_RIGHT)
        im2.save("j.jpg")
        pixmap = QPixmap("j.jpg")
        self.lbl.setPixmap(pixmap)
    
    def vertical_reflection(self):
        im2 = Image.open("j.jpg")
        im2 = im2.rotate(180)
        im2 = im2.transpose(Image.FLIP_LEFT_RIGHT)
        im2.save("j.jpg")
        pixmap = QPixmap("j.jpg")
        self.lbl.setPixmap(pixmap)        
        
    def negative(self):
        im2 = Image.open("j.jpg")
        pixels = im2.load()
        x, y = im2.size   
        for i in range(x):  
            for j in range(y):
                r, g, b = pixels[i, j]
                r1 = 255 - r
                g1 = 255 - g
                b1 = 255 - b
                pixels[i, j] = r1, g1, b1
        im2.save("j.jpg")
        pixmap = QPixmap("j.jpg")
        self.lbl.setPixmap(pixmap)
    
    def noises(self):
        factor, okBtnPressed = QInputDialog.getInt(
            self, "Зернистость", "Введите желвемый показатель зернистости", 20, 0, 100, 1
        )
        if okBtnPressed:
            im2 = Image.open("j.jpg")
            pixels = im2.load()
            x, y = im2.size   
            for i in range(x):  
                for j in range(y):
                    rand = random.randint(-factor, factor)
                    r, g, b = pixels[i, j]
                    r1 = r + rand
                    g1 = g + rand
                    b1 = b + rand
                    if r1 < 0:
                        r1 = 0
                    if g1 < 0:
                        g1 = 0
                    if b1 < 0:
                        b1 = 0
                    if r1 > 255:
                        r1 = 255
                    if g1 > 255:
                        g1 = 255
                    if b1 > 255:
                        b1 = 255
                    pixels[i, j] = int(r1), int(g1), int(b1)    
        im2.save("j.jpg")
        pixmap = QPixmap("j.jpg")
        self.lbl.setPixmap(pixmap)    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
