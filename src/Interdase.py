# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interdase.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1120, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1120, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1120, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 720, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(740, 10, 371, 681))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.dpi = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.dpi.setMinimum(1)
        self.dpi.setMaximum(1000)
        self.dpi.setProperty("value", 300)
        self.dpi.setObjectName("dpi")
        self.horizontalLayout_7.addWidget(self.dpi)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.area = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.area.setFocusPolicy(QtCore.Qt.NoFocus)
        self.area.setObjectName("area")
        self.horizontalLayout_8.addWidget(self.area)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.filter = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.filter.setObjectName("filter")
        self.filter.addItem("")
        self.filter.addItem("")
        self.verticalLayout_2.addWidget(self.filter)
        self.pre_processing_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pre_processing_button.setObjectName("pre_processing_button")
        self.verticalLayout_2.addWidget(self.pre_processing_button)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.noise_check = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.noise_check.setObjectName("noise_check")
        self.verticalLayout_3.addWidget(self.noise_check)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.noise_w = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_w.sizePolicy().hasHeightForWidth())
        self.noise_w.setSizePolicy(sizePolicy)
        self.noise_w.setMinimum(1)
        self.noise_w.setProperty("value", 3)
        self.noise_w.setObjectName("noise_w")
        self.horizontalLayout_3.addWidget(self.noise_w)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.noise_h = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_h.sizePolicy().hasHeightForWidth())
        self.noise_h.setSizePolicy(sizePolicy)
        self.noise_h.setMinimum(1)
        self.noise_h.setProperty("value", 3)
        self.noise_h.setObjectName("noise_h")
        self.horizontalLayout_3.addWidget(self.noise_h)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.noise_iter = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_iter.sizePolicy().hasHeightForWidth())
        self.noise_iter.setSizePolicy(sizePolicy)
        self.noise_iter.setMinimum(1)
        self.noise_iter.setProperty("value", 1)
        self.noise_iter.setObjectName("noise_iter")
        self.horizontalLayout_5.addWidget(self.noise_iter)
        spacerItem5 = QtWidgets.QSpacerItem(165, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.noise_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.noise_button.setObjectName("noise_button")
        self.horizontalLayout.addWidget(self.noise_button)
        self.noise_button_resart = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.noise_button_resart.setObjectName("noise_button_resart")
        self.horizontalLayout.addWidget(self.noise_button_resart)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.dilate_check = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.dilate_check.setObjectName("dilate_check")
        self.verticalLayout_4.addWidget(self.dilate_check)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.dilate_w = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dilate_w.sizePolicy().hasHeightForWidth())
        self.dilate_w.setSizePolicy(sizePolicy)
        self.dilate_w.setMinimum(1)
        self.dilate_w.setProperty("value", 3)
        self.dilate_w.setObjectName("dilate_w")
        self.horizontalLayout_4.addWidget(self.dilate_w)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.dilate_h = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dilate_h.sizePolicy().hasHeightForWidth())
        self.dilate_h.setSizePolicy(sizePolicy)
        self.dilate_h.setMinimum(1)
        self.dilate_h.setObjectName("dilate_h")
        self.horizontalLayout_4.addWidget(self.dilate_h)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.dilate_iter = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dilate_iter.sizePolicy().hasHeightForWidth())
        self.dilate_iter.setSizePolicy(sizePolicy)
        self.dilate_iter.setMinimum(1)
        self.dilate_iter.setProperty("value", 2)
        self.dilate_iter.setObjectName("dilate_iter")
        self.horizontalLayout_6.addWidget(self.dilate_iter)
        spacerItem7 = QtWidgets.QSpacerItem(165, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dilate_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.dilate_button.setObjectName("dilate_button")
        self.horizontalLayout_2.addWidget(self.dilate_button)
        self.dilate_button_resart = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.dilate_button_resart.setObjectName("dilate_button_resart")
        self.horizontalLayout_2.addWidget(self.dilate_button_resart)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem8)
        self.all_button_resart = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.all_button_resart.setObjectName("all_button_resart")
        self.verticalLayout_5.addWidget(self.all_button_resart)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem9)
        self.mask_check = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.mask_check.setObjectName("mask_check")
        self.verticalLayout_5.addWidget(self.mask_check)
        self.conturs_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.conturs_button.setObjectName("conturs_button")
        self.verticalLayout_5.addWidget(self.conturs_button)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setEnabled(False)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_file_action = QtWidgets.QAction(MainWindow)
        self.open_file_action.setObjectName("open_file_action")
        self.menu.addAction(self.open_file_action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "DPI:"))
        self.label_14.setText(_translate("MainWindow", "Площадь капель в см^2:"))
        self.area.setText(_translate("MainWindow", "Нет контура"))
        self.label_2.setText(_translate("MainWindow", "Метод адаптивного порога"))
        self.filter.setItemText(0, _translate("MainWindow", "Adaptive Threshold"))
        self.filter.setItemText(1, _translate("MainWindow", "Gaussian Blur"))
        self.pre_processing_button.setText(_translate("MainWindow", "Применить"))
        self.label_3.setText(_translate("MainWindow", "Удалить Шум"))
        self.noise_check.setText(_translate("MainWindow", "Применить к текущему"))
        self.label_4.setText(_translate("MainWindow", "Размер ядра:"))
        self.label_5.setText(_translate("MainWindow", "Width:"))
        self.label_6.setText(_translate("MainWindow", "Height:"))
        self.label_11.setText(_translate("MainWindow", "Количество итераций"))
        self.noise_button.setText(_translate("MainWindow", "Применить"))
        self.noise_button_resart.setText(_translate("MainWindow", "Сбросить"))
        self.label_7.setText(_translate("MainWindow", "Увеличить площадь обьектов"))
        self.dilate_check.setText(_translate("MainWindow", "Применить к текущему"))
        self.label_8.setText(_translate("MainWindow", "Размер ядра"))
        self.label_9.setText(_translate("MainWindow", "Width:"))
        self.label_10.setText(_translate("MainWindow", "Height:"))
        self.label_12.setText(_translate("MainWindow", "Количество итераций"))
        self.dilate_button.setText(_translate("MainWindow", "Применить"))
        self.dilate_button_resart.setText(_translate("MainWindow", "Сбросить"))
        self.all_button_resart.setText(_translate("MainWindow", "Сбросить все настройки"))
        self.mask_check.setText(_translate("MainWindow", "Граница по текщей маске"))
        self.conturs_button.setText(_translate("MainWindow", "Выделить границы"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Отсутствует"))
        self.open_file_action.setText(_translate("MainWindow", "Открыть"))