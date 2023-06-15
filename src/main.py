import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot as slot
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import processing as proc

from Interdase import Ui_MainWindow as Design  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, Design):
    # Основное поведение класса наследуется из Qt, а виджеты - из design.ui
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Этот метод из класса Design, он инициализирует виджеты
        #self.file = None
        self.image = None
        self.image_gray = None
        self.thresh = None
        self.thresh_n = None
        self.open_file_action.triggered.connect(self.open_file)
        self.pre_processing_button.clicked.connect(self.pre_processing)
        self.noise_button_resart.clicked.connect(self.noise_restarn)
        self.noise_button.clicked.connect(self.noise)
        self.dilate_button_resart.clicked.connect(self.dilate_restarn)
        self.dilate_button.clicked.connect(self.dilate)
        self.all_button_resart.clicked.connect(self.all_restart)
        self.conturs_button.clicked.connect(self.conturs)

    def all_restart(self):
        self.pre_processing()
        self.noise_restarn()
        self.dilate_restarn()
    def pre_processing(self):
        if(self.image_gray is None):
            return
        self.thresh = proc.pre_processing(self.image_gray,self.filter.currentText())
        self.print_image(self.thresh)
    def noise_restarn(self):
        self.noise_w.setValue(3)
        self.noise_h.setValue(3)
        self.noise_iter.setValue(1)
        self.noise_check.setChecked(False)
        self.noise()
    def noise(self):
        if (self.thresh is None):
            self.pre_processing()
            if (self.thresh is None):
                return

        if (self.noise_check.isChecked() and (self.thresh_n is not None)):
            thresh = self.thresh_n

        else: thresh = self.thresh
        self.thresh_n = proc.noise(thresh,self.noise_w.value(),\
                                   self.noise_h.value(),self.noise_iter.value())
        self.print_image(self.thresh_n)
        self.thresh_d = None

    def dilate_restarn(self):
        self.dilate_w.setValue(3)
        self.dilate_h.setValue(3)
        self.dilate_iter.setValue(1)
        self.dilate_check.setChecked(False)
        self.dilate()
    def dilate(self):
        if (self.thresh_n is None):
            self.noise()
            if (self.thresh_n is None):
                return

        if (self.dilate_check.isChecked() and (self.thresh_d is not None)):
            thresh = self.thresh_d

        else: thresh = self.thresh_n
        self.thresh_d = proc.dilate(thresh,self.dilate_w.value(),\
                                   self.dilate_h.value(),self.dilate_iter.value())
        self.print_image(self.thresh_d)

    def open_file(self):
        dirlist = QFileDialog.getOpenFileName(self,"Выбрать файл",".")
        file = dirlist[0]
        if (file == ""):
            self.menu_2.setTitle("Файл не выбран")
            return
        self.menu_2.setTitle(file)
        self.image ,self.image_gray = proc.load_image(file)
        self.print_image(self.image)
        self.thresh = None
        self.thresh_n = None
        self.thresh_d = None

    def print_image(self, image):
        if (len(image.shape) ==3 ):
            temp_imgSrc = QImage(image[:], image.shape[1], image.shape[0], image.shape[1] * 3, QImage.Format_RGB888)
        else:
            temp_imgSrc = QImage(image[:], image.shape[1], image.shape[0], QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(temp_imgSrc).scaled(720, 720)
        #pixmap = pixmap.scaled(720, 720)
        self.label.clear()
        self.label.setPixmap(pixmap)

    def conturs(self):
        if self.image is None:
            return
        if self.mask_check.isChecked():
            if self.thresh is None:
                self.pre_processing()
            if self.thresh_n is None:
               self.noise()
            if self.thresh_d is None:
               self.dilate()
        else:
            self.pre_processing()
            self.noise()
            self.dilate()
        thresh = self.thresh_d
        image,area = proc.contur(self.image.copy(),thresh)
        self.print_image(image)
        print(area)
        area = 2.54 * (area/self.dpi.value())
        self.area.setText(str(area))
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))  # Более современная тема оформления
    app.setPalette(QtWidgets.QApplication.style().standardPalette())  # Берём цвета из темы оформления

    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
