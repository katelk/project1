from PIL import Image, ImageEnhance
import os
import sys
import random
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow, QInputDialog, QFileDialog, QHBoxLayout, QVBoxLayout, QColorDialog, QErrorMessage
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QColor, QFont, QBrush

def showPicture(image):
    im = image.copy()
    im.thumbnail([500,500],Image.ANTIALIAS)
    im.save("j.jpg")
    pixmap = QPixmap("j.jpg") 
    os.remove("j.jpg")
    return pixmap 

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.resize(1000, 640)
        self.setWindowTitle('Редактор фотографий')
        
        self.label1 = QLabel(self)
        self.label1.setText("Добро пожаловать в редактор ")
        self.label1.setFont(QFont("Calibri", 35, QFont.Bold))
        self.label1.move(185, 40)
        
        self.label2 = QLabel(self)
        self.label2.setText("фотографий RESHEL!")
        self.label2.setFont(QFont("Calibri", 35, QFont.Bold))
        self.label2.move(265, 100)
        
        self.btn = QPushButton('Приступить к работе', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(68, 70)
        self.btn.clicked.connect(self.action)        
        
    def action(self):
        main_vbox = QVBoxLayout()
        
        self.label1.deleteLater()
        self.label2.deleteLater()
        self.btn.deleteLater() 
        
        self.lbl = QLabel(self)
        main_vbox.addWidget(self.lbl)
        
        first_hbox = QHBoxLayout()
        main_vbox.addLayout(first_hbox)
        
        self.btn_horizontal_reflection = QPushButton('Отразить по горизонтали', self)
        self.btn_horizontal_reflection.resize(self.btn_horizontal_reflection.sizeHint())
        self.btn_horizontal_reflection.clicked.connect(self.horizontal_reflection)
        first_hbox.addWidget(self.btn_horizontal_reflection)
        
        self.btn_vertical_reflection = QPushButton('Отразить по вертикали', self)
        self.btn_vertical_reflection.resize(self.btn_vertical_reflection.sizeHint())
        self.btn_vertical_reflection.clicked.connect(self.vertical_reflection)
        first_hbox.addWidget(self.btn_vertical_reflection)
        
        self.btn_black_white = QPushButton('Черно-белый', self)
        self.btn_black_white.resize(self.btn_black_white.sizeHint())
        self.btn_black_white.clicked.connect(self.black_white)
        first_hbox.addWidget(self.btn_black_white)
        
        second_hbox = QHBoxLayout()
        main_vbox.addLayout(second_hbox)
        
        self.btn_negative = QPushButton('Негатив', self)
        self.btn_negative.resize(self.btn_negative.sizeHint())
        self.btn_negative.clicked.connect(self.negative)
        second_hbox.addWidget(self.btn_negative)
        
        self.btn_contrast = QPushButton('Контрастность', self)
        self.btn_contrast.resize(self.btn_contrast.sizeHint())
        self.btn_contrast.clicked.connect(self.contrast)
        second_hbox.addWidget(self.btn_contrast)
        
        self.btn_saturation = QPushButton('Насыщенность', self)
        self.btn_saturation.resize(self.btn_saturation.sizeHint())
        self.btn_saturation.clicked.connect(self.saturation)
        second_hbox.addWidget(self.btn_saturation)
        
        third_hbox = QHBoxLayout()
        main_vbox.addLayout(third_hbox)
        
        self.btn_brightness = QPushButton(self)
        self.btn_brightness.setText("Яркость")
        self.btn_brightness.resize(self.btn_brightness.sizeHint())
        self.btn_brightness.clicked.connect(self.brightness)
        third_hbox.addWidget(self.btn_brightness)
        
        self.btn_noises = QPushButton('Зернистость', self)
        self.btn_noises.resize(self.btn_noises.sizeHint())
        self.btn_noises.clicked.connect(self.noises)
        third_hbox.addWidget(self.btn_noises)
        
        self.btn_color = QPushButton('Цвета', self)
        self.btn_color.resize(self.btn_color.sizeHint())
        #self.btn_color.clicked.connect(self.color)
        third_hbox.addWidget(self.btn_color)
        
        self.btn_save = QPushButton(self)
        self.btn_save.setIcon(QIcon('save.bmp'))
        self.btn_save.resize(self.btn_save.sizeHint())
        self.btn_save.setToolTip('Сохранить')
        #self.btn_save.clicked.connect(self.save)
        #self.btn_save.move(0, 0)
        
        self.setLayout(main_vbox)
        self.move(300, 200)
        self.show() 
    
    def brightness(self):
        factor, okBtnPressed = QInputDialog.getInt(self, "Яркость", "Введите желаемый показатель яркости", 0, -100, 100, 1)
        if okBtnPressed:
            im2 = self.image_first
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
            self.image_second = self.image_first.copy()
            self.lbl.setPixmap(showPicture(self.image_second))
            
    def contrast(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "Контрастность", "Введите желаемый показатель контрастности", 0, -100, 100, 1
        )
        if okBtnPressed:
            contrast = ImageEnhance.Contrast(self.image_first)
            if i < 0:
                self.image_first = contrast.enhance(1 - ((i * (-1)) / 100))
            if i > 0:
                self.image_first = contrast.enhance(1 + (i / 100))
            if i == 0:
                self.image_first = contrast.enhance(1)
            self.image_second = self.image_first.copy()
            self.lbl.setPixmap(showPicture(self.image_second))
            
    def saturation(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "Насыщенность", "Введите желаемый показатель насыщенности", 0, -100, 100, 1
        )
        if okBtnPressed:
            converter = ImageEnhance.Color(self.image_first)
            if i < 0:
                self.image_first = converter.enhance(1 - ((i * (-1)) / 100))
            if i > 0:
                self.image_first = converter.enhance(1 + (i / 100))
            if i == 0:
                self.image_first = converter.enhance(1)
            self.image_second = self.image_first.copy()
            self.lbl.setPixmap(showPicture(self.image_second))
                
    def black_white(self):
        im2 = self.image_first.copy()
        pixels = im2.load()
        x, y = im2.size   
        for i in range(x):  
            for j in range(y):
                r, g, b = pixels[i, j]
                bw = (r + g + b) // 3
                pixels[i, j] = bw, bw, bw
        self.image_second = im2
        self.lbl.setPixmap(showPicture(self.image_second))
        
    def horizontal_reflection(self):
        self.image_first = self.image_first.rotate(180)
        self.image_first = self.image_first.transpose(Image.FLIP_LEFT_RIGHT)
        self.image_second = self.image_second.rotate(180)
        self.image_second = self.image_second.transpose(Image.FLIP_LEFT_RIGHT)        
        self.lbl.setPixmap(showPicture(self.image_second))      
    
    def vertical_reflection(self):
        self.image_first = self.image_first.transpose(Image.FLIP_LEFT_RIGHT)
        self.image_second = self.image_second.transpose(Image.FLIP_LEFT_RIGHT)
        self.lbl.setPixmap(showPicture(self.image_second)) 
        
    def negative(self):
        im2 = self.image_first.copy()
        pixels = im2.load()
        x, y = im2.size   
        for i in range(x):  
            for j in range(y):
                r, g, b = pixels[i, j]
                r1 = 255 - r
                g1 = 255 - g
                b1 = 255 - b
                pixels[i, j] = r1, g1, b1
        self.image_second = im2
        self.lbl.setPixmap(showPicture(self.image_second))
    
    def noises(self):
        factor, okBtnPressed = QInputDialog.getInt(
            self, "Зернистость", "Введите желаемый показатель зернистости", 20, 0, 100, 1
        )
        if okBtnPressed:
            im2 = self.image_first
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
        self.image_second = self.image_first.copy()
        self.lbl.setPixmap(showPicture(self.image_second))  
        
class Example(QMainWindow):
        
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.MainWidget = Widget()
        self.setCentralWidget(self.MainWidget)
        self.statusBar()
        
        icon = QIcon('rl.bmp')
        self.setWindowIcon(icon)
        
        self.pal = self.palette()
        self.pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("фон.jpg")))
        self.pal.setBrush(QPalette.Disabled, QPalette.Window, QBrush(QPixmap("фон.jpg")))
        self.pal.setBrush(QPalette.Inactive, QPalette.Window, QBrush(QPixmap("фон.jpg")))
        self.setPalette(self.pal) 
        
        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showOpenDialog)
        
        saveFile = QAction(QIcon('open.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.showSaveDialog)
        
        colorAction = QAction(QIcon('exit24.png'), 'color', self)
        colorAction.setStatusTip('color application')
        colorAction.triggered.connect(self.colore)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Файл')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileSetUp = menubar.addMenu('Настройки')
        fileSetUp.addAction(colorAction)
        
        self.resize(1000, 640)
        self.setWindowTitle('Main window')
        self.show()
        
    def colore(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.pal.setColor(QPalette.Normal, QPalette.Window, col)
            self.setPalette(self.pal)
    def showOpenDialog(self):
        try:
            file = QFileDialog.getOpenFileName(self, 'Открыть файл', '/home', "Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)")[0]
            self.MainWidget.image_first = Image.open(file)
            self.MainWidget.image_second = Image.open(file)
            self.MainWidget.lbl.setPixmap(showPicture(self.MainWidget.image_first))
        except Exception:
            error = QErrorMessage(parent=self)
            error.showMessage("Сначала начните работу")

    def showSaveDialog(self):
        fileName = QFileDialog.getSaveFileName(self , "Сохранить файл"  , "6.jpg",  "*.jpg;;Text files (*.txt);;XML files (*.xml)")
        self.MainWidget.image.save(fileName[0])
 
if __name__ == '__main__':
        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  
