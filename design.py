# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 178)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label.setObjectName("label")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(270, 30, 161, 22))
        self.horizontalSlider.setMouseTracking(True)
        self.horizontalSlider.setTabletTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMaximum(9)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 71, 21))
        self.label_2.setObjectName("label_2")

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(270, 70, 160, 22))
        self.horizontalSlider_2.setTabletTracking(True)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setMaximum(9)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 50, 71, 21))
        self.label_3.setObjectName("label_3")

        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(270, 110, 160, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setMaximum(9)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 90, 21, 21))
        self.label_4.setObjectName("label_4")

        self.ConnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectButton.setGeometry(QtCore.QRect(10, 60, 91, 23))
        self.ConnectButton.setObjectName("pushButton")

        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.Send.setObjectName("send")

        self.Port = QtWidgets.QComboBox(self.centralwidget)
        self.Port.setGeometry(QtCore.QRect(10, 30, 69, 22))
        self.Port.setObjectName("Port")

        self.Room = QtWidgets.QComboBox(self.centralwidget)
        self.Room.setGeometry(QtCore.QRect(140, 30, 91, 22))
        self.Room.setObjectName("Room")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 30, 16, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 70, 16, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 110, 16, 16))
        self.label_7.setObjectName("label_6")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 10, 51, 20))
        self.label_8.setObjectName("label_8")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSlider.sliderMoved.connect(self.label_5.setNum)
        self.horizontalSlider_2.sliderMoved.connect(self.label_6.setNum)
        self.horizontalSlider_3.sliderMoved.connect(self.label_7.setNum)




        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Порт"))
        self.label_2.setText(_translate("MainWindow", "Освещение"))
        self.label_3.setText(_translate("MainWindow", "Дверь"))
        self.label_4.setText(_translate("MainWindow", "Фон"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Комнаты"))
        self.ConnectButton.setText(_translate("MainWindow", "Подключиться"))
        self.Send.setText(_translate("MainWindow", "Отправить"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))