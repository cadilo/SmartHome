from PyQt5 import QtWidgets, uic
import sys
import design
from port import serial_ports
import serial

#app = QtWidgets.QApplication([])
#win = uic.loadUi("design.ui")  # расположение вашего файла .ui
rooms = ["Все", "Гостинная", "Кухня", "Ванная", "Спальня", "Мансарда(прав.)", "Мансарда(лев.)"]

#win.show()
#sys.exit(app.exec())

class LedApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.Port.addItems(serial_ports())
        #self.horizontalSlider.setValue(sl)
        self.Room.addItems(rooms)
        self.realport = None
        #sl = self.horizontalSlider.value()
        self.ConnectButton.clicked.connect(self.connect)
        self.Send.clicked.connect(self.send)





    def connect(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(),1200)
            #if self.realport == True:
            self.ConnectButton.setStyleSheet("background-color: green")
            self.ConnectButton.setText('Подключено')
        except Exception as e:
            print(e)

    def send(self):
        print("Уровень освещения: ",str(self.horizontalSlider.value()))
        print("Уровень фона: ", str(self.horizontalSlider_3.value()))
        print("Отправлено: \n" + "XL" + str(rooms.index(self.Room.currentText())) + str(self.horizontalSlider.value()))
        print("XD0"+ str(self.horizontalSlider_2.value()))
        print("XB"+str(rooms.index(self.Room.currentText()))+str(self.horizontalSlider_3.value()))
        print(rooms.index(self.Room.currentText()), "\n")
        print(self.Room.currentText())

        if self.realport:
            self.realport.write(bytes("XL"+str(rooms.index(self.Room.currentText())) + str(self.horizontalSlider.value())+"\r\n",'ascii'))
            self.realport.write(bytes("XD0"+ str(self.horizontalSlider_2.value()) + "\r\n", 'ascii'))
            self.realport.write(bytes("XB"+str(rooms.index(self.Room.currentText()))+str(self.horizontalSlider_3.value())+ "\r\n", 'ascii'))




def main():
    app = QtWidgets.QApplication(sys.argv)
    #window = uic.loadUi("design.ui")
    window = LedApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()