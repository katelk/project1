from PIL import Image, ImageEnhance
import vk_api
import requests
import os
import sys
import random
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QMainWindow, QAction, QApplication,
                             QWidget, QPushButton, QLineEdit,
                             QLabel, QMainWindow, QInputDialog,
                             QFileDialog, QHBoxLayout, QVBoxLayout,
                             QColorDialog, QErrorMessage, QInputDialog)
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

        self.btn = QPushButton(self)
        self.btn.resize(QSize(500, 100))
        iconka = QIcon('приступить.bmp')
        self.btn.setIcon(iconka)
        self.btn.setIconSize(QSize(500, 100))
        self.btn.move(230, 300)
        self.btn.clicked.connect(self.action)

    def action(self):
        main_vbox = QVBoxLayout()

        nul_hbox = QHBoxLayout()
        nul_hbox.addStretch(1)
        main_vbox.addLayout(nul_hbox)

        self.btn_share = QPushButton(self)
        self.btn_share.setIcon(QIcon('поделится.bmp'))
        self.btn_share.resize(10, 10)
        self.btn_share.setToolTip('Поделиться в вк')
        self.btn_share.clicked.connect(self.share)
        nul_hbox.addWidget(self.btn_share)

        self.label1.deleteLater()
        self.label2.deleteLater()
        self.btn.deleteLater()

        self.lbl = QLabel(self)
        main_vbox.addWidget(self.lbl)

        first_hbox = QHBoxLayout()
        main_vbox.addLayout(first_hbox)

        self.btn_horizontal_reflection = QPushButton('Отразить по горизонтали',
                                                     self)
        self.btn_horizontal_reflection.resize(self.btn_horizontal_reflection.
                                              sizeHint())
        self.btn_horizontal_reflection.clicked.connect(self.
                                                       horizontal_reflection)
        first_hbox.addWidget(self.btn_horizontal_reflection)
        
        self.btn_vertical_reflection = QPushButton('Отразить по вертикали',
                                                   self)
        self.btn_vertical_reflection.resize(self.btn_vertical_reflection.
                                            sizeHint())
        self.btn_vertical_reflection.clicked.connect(self.vertical_reflection)
        first_hbox.addWidget(self.btn_vertical_reflection)

        second_hbox = QHBoxLayout()
        main_vbox.addLayout(second_hbox)

        self.btn_black_white = QPushButton('Черно-белый', self)
        self.btn_black_white.resize(self.btn_black_white.sizeHint())
        self.btn_black_white.clicked.connect(self.black_white)
        second_hbox.addWidget(self.btn_black_white)

        self.btn_negative = QPushButton('Негатив', self)
        self.btn_negative.resize(self.btn_negative.sizeHint())
        self.btn_negative.clicked.connect(self.negative)
        second_hbox.addWidget(self.btn_negative)

        third_hbox = QHBoxLayout()
        main_vbox.addLayout(third_hbox)

        self.btn_contrast = QPushButton('Контрастность', self)
        self.btn_contrast.resize(self.btn_contrast.sizeHint())
        self.btn_contrast.clicked.connect(self.contrast)
        third_hbox.addWidget(self.btn_contrast)

        self.btn_saturation = QPushButton('Насыщенность', self)
        self.btn_saturation.resize(self.btn_saturation.sizeHint())
        self.btn_saturation.clicked.connect(self.saturation)
        third_hbox.addWidget(self.btn_saturation)

        four_hbox = QHBoxLayout()
        main_vbox.addLayout(four_hbox)

        self.btn_brightness = QPushButton(self)
        self.btn_brightness.setText("Яркость")
        self.btn_brightness.resize(self.btn_brightness.sizeHint())
        self.btn_brightness.clicked.connect(self.brightness)
        four_hbox.addWidget(self.btn_brightness)

        self.btn_noises = QPushButton('Зернистость', self)
        self.btn_noises.resize(self.btn_noises.sizeHint())
        self.btn_noises.clicked.connect(self.noises)
        four_hbox.addWidget(self.btn_noises)

        five_hbox = QHBoxLayout()
        main_vbox.addLayout(five_hbox)

        self.btn_anaglif = QPushButton('Анаглиф', self)
        self.btn_anaglif.resize(self.btn_anaglif.sizeHint())
        self.btn_anaglif.clicked.connect(self.anaglif)
        five_hbox.addWidget(self.btn_anaglif)

        self.btn_frame = QPushButton('Рамка', self)
        self.btn_frame.resize(self.btn_frame.sizeHint())
        self.btn_frame.clicked.connect(self.frame)
        five_hbox.addWidget(self.btn_frame)

        self.setLayout(main_vbox)
        self.move(300, 200)
        self.show()

    def share(self):
        login, ok1 = QInputDialog.getText(self, 'Поделиться',
            'Введите логин:')

        if ok1:
            password, ok2 = QInputDialog.getText(self, 'Поделиться',
            'Введите пароль:')

            if ok2:
                vk_session = vk_api.VkApi(login, password)
                vk_session.auth()
                vk = vk_session.get_api()

                IMAGE_URL = vk.photos.getWallUploadServer()
                user_id = IMAGE_URL['user_id']
                upload_url = IMAGE_URL['upload_url']

                self.image.save("help.jpg")               
                request = requests.post(upload_url,
                                        files={'photo': open("help.jpg", "rb")})
                os.remove("help.jpg") 
                params = {'server': request.json()['server'],
                            'photo': request.json()['photo'],
                            'hash': request.json()['hash']}
                save = vk.photos.saveWallPhoto(**params)
                photo_id = save[0]['id']
                vk.wall.post(owner_id = user_id, message = '',attachments =
                             'photo' + str(user_id) + "_"+ str(photo_id))                    

    def anaglif(self):
        im2 = self.image
        pixels = im2.load()
        x, y = im2.size
        for i in range(y):
            for j in list(reversed(range(x))):
                r2, g, b = pixels[j, i]
                pixels[j, i] = 0, g, b
                q = j + 5
                if q < x:
                    r, g, b = pixels[q, i]
                    pixels[q, i] = r2, g, b
        self.lbl.setPixmap(showPicture(self.image)) 

    def brightness(self):
        factor, okBtnPressed = QInputDialog.getInt(self, "Яркость",
                                                   "Введите показатель яркости",
                                                   0, -100, 100, 1)
        if okBtnPressed:
            im2 = self.image
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
            self.lbl.setPixmap(showPicture(self.image))

    def contrast(self):
        text = "Введите показатель контрастности"
        i, okBtnPressed = QInputDialog.getInt(self, "Контрастность",
                                              text, 0, -100, 100, 1)
        if okBtnPressed:
            contrast = ImageEnhance.Contrast(self.image)
            if i < 0:
                self.image = contrast.enhance(1 - ((i * (-1)) / 100))
            if i > 0:
                self.image = contrast.enhance(1 + (i / 100))
            if i == 0:
                self.image = contrast.enhance(1)
            self.lbl.setPixmap(showPicture(self.image))

    def saturation(self):
        text = "Введите показатель насыщенности"
        i, okBtnPressed = QInputDialog.getInt(self, "Насыщенность", text,
                                              0, -100, 100, 1)
        if okBtnPressed:
            converter = ImageEnhance.Color(self.image)
            if i < 0:
                self.image = converter.enhance(1 - ((i * (-1)) / 100))
            if i > 0:
                self.image = converter.enhance(1 + (i / 100))
            if i == 0:
                self.image = converter.enhance(1)

            self.lbl.setPixmap(showPicture(self.image))

    def black_white(self):
        im2 = self.image
        pixels = im2.load()
        x, y = im2.size   
        for i in range(x):  
            for j in range(y):
                r, g, b = pixels[i, j]
                bw = (r + g + b) // 3
                pixels[i, j] = bw, bw, bw
        self.lbl.setPixmap(showPicture(self.image))

    def horizontal_reflection(self):
        self.image = self.image.rotate(180)
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)       
        self.lbl.setPixmap(showPicture(self.image))

    def vertical_reflection(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.lbl.setPixmap(showPicture(self.image)) 

    def negative(self):
        im2 = self.image
        pixels = im2.load()
        x, y = im2.size   
        for i in range(x):  
            for j in range(y):
                r, g, b = pixels[i, j]
                r1 = 255 - r
                g1 = 255 - g
                b1 = 255 - b
                pixels[i, j] = r1, g1, b1
        self.lbl.setPixmap(showPicture(self.image))

    def frame(self):
        text = "Введите ширину рамки, а затем ее цвет"
        i, okBtnPressed = QInputDialog.getInt(self, "Рамка", text,
                                              20, 0, 70, 1)
        if okBtnPressed:
            color = QColorDialog.getColor()
            if color.isValid():
                im2 = self.image
                im_two = im2.copy()
                old_size = im2.size
                x, y = im2.size
                new_size = (x + i, y + i)
                im2 = Image.new("RGB", new_size, color.name())
                im2.paste(im_two, (int((new_size[0] - old_size[0]) / 2),
                                   (int((new_size[1] - old_size[1]) / 2))))
                self.image = im2
        self.lbl.setPixmap(showPicture(self.image))

    def noises(self):
        text = "Введите желаемый показатель зернистости"
        factor, okBtnPressed = QInputDialog.getInt(self, "Зернистость", text,
                                                   20, 0, 100, 1)
        if okBtnPressed:
            im2 = self.image
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
        self.lbl.setPixmap(showPicture(self.image))  

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
        self.pal.setBrush(QPalette.Normal, QPalette.Window,
                          QBrush(QPixmap("фон.jpg")))
        self.pal.setBrush(QPalette.Disabled, QPalette.Window,
                          QBrush(QPixmap("фон.jpg")))
        self.pal.setBrush(QPalette.Inactive, QPalette.Window,
                          QBrush(QPixmap("фон.jpg")))
        self.setPalette(self.pal) 

        exitAction = QAction('Выйти', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openFile = QAction('Открыть', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showOpenDialog)

        saveFile = QAction('Сохранить', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.showSaveDialog)

        colorAction = QAction('Изменить цвет фона', self)
        colorAction.setStatusTip('')
        colorAction.triggered.connect(self.change_color_fon)

        fonAction = QAction('Изменить изображение фона', self)
        fonAction.setStatusTip('')
        fonAction.triggered.connect(self.change_image_fon)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Файл')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        fileSetUp = menubar.addMenu('Настройки')
        fileSetUp.addAction(colorAction)
        fileSetUp.addAction(fonAction)

        self.resize(1000, 640)
        self.setWindowTitle('Main window')
        self.show()

    def change_image_fon(self):
        file = QFileDialog.getOpenFileName(self, 'Открыть файл', '/home',
                                           "*.jpg;;*.bmp;;*.png")
        self.pal.setBrush(QPalette.Normal, QPalette.Window,
                          QBrush(QPixmap(file[0])))
        self.pal.setBrush(QPalette.Disabled, QPalette.Window,
                          QBrush(QPixmap(file[0])))
        self.pal.setBrush(QPalette.Inactive, QPalette.Window,
                          QBrush(QPixmap(file[0])))
        self.setPalette(self.pal)    

    def change_color_fon(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.pal.setColor(QPalette.Normal, QPalette.Window, col)
            self.pal.setColor(QPalette.Disabled, QPalette.Window, col)
            self.pal.setColor(QPalette.Inactive, QPalette.Window, col)
            self.setPalette(self.pal)

    def showOpenDialog(self):
        try:
            file = QFileDialog.getOpenFileName(self, 'Открыть файл', '/home',
                                               "*.jpg;;*.bmp;;*.png")[0]
            self.MainWidget.image = Image.open(file)
            self.MainWidget.lbl.setPixmap(showPicture(self.MainWidget.image))

        except Exception:
            error = QErrorMessage(parent=self)
            error.showMessage("Ошибка")

    def showSaveDialog(self):
        try:
            fileName = QFileDialog.getSaveFileName(self , "Сохранить файл",
                                                   "untitled.jpg",
                                                   "*.jpg;;*.bmp;;*.png")
            self.MainWidget.image.save(fileName[0])

        except Exception:
            error = QErrorMessage(parent=self)
            error.showMessage("Ошибка")

if __name__ == '__main__':
        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
