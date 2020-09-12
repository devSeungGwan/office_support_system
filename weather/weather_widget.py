# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from input_locate import Input_Location
import weather


class Ui_Weather_widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent = parent)
        self.setObjectName("Form")
        self.resize(650, 520)
        self.setMinimumSize(QtCore.QSize(650, 520))
        self.setMaximumSize(QtCore.QSize(650, 520))

        self.location_title = QtWidgets.QLabel(self)
        self.location_title.setGeometry(QtCore.QRect(450,30,90,30))
        self.location_title.setStyleSheet("background-color: #FF7700; color: white;border-style: outset; border-radius: 5px; border-color: #E07626; border-width: 2px")
        self.location_title.setAlignment(QtCore.Qt.AlignCenter)
        self.location_title.setText("지역")
        location_title = self.location_title.font()
        location_title.setPointSize(16)
        location_title.setBold(True)
        self.location_title.setFont(location_title)

        self.location_logo = QtWidgets.QLabel(self)
        self.location_logo.setGeometry(QtCore.QRect(450,60,90,60))
        self.location_logo.setStyleSheet("background-color: #FFE3CC; color: black;border-style: outset; border-radius: 5px; border-color: #E07626; border-width: 2px")
        self.location_logo.setAlignment(QtCore.Qt.AlignCenter)
        location_font = self.location_logo.font()
        location_font.setPointSize(20)
        location_font.setBold(True)
        self.location_logo.setFont(location_font)

        self.temperature_logo = QtWidgets.QLabel(self)
        self.temperature_logo.setGeometry(QtCore.QRect(50, 50, 90, 90))
        self.temperature_logo.setPixmap(QtGui.QPixmap(os.getcwd()+'/img/temperature.jpg'))

        self.humidity_logo = QtWidgets.QLabel(self)
        self.humidity_logo.setGeometry(QtCore.QRect(60, 150, 90, 90))
        self.humidity_logo.setPixmap(QtGui.QPixmap(os.getcwd()+'/img/humidity.jpg'))


        self.windspeed_logo = QtWidgets.QLabel(self)
        self.windspeed_logo.setGeometry(QtCore.QRect(70, 250, 90, 90))
        self.windspeed_logo.setPixmap(QtGui.QPixmap(os.getcwd()+'/img/windspeed.jpg'))


        self.condition_logo = QtWidgets.QLabel(self)
        self.condition_logo.setGeometry(QtCore.QRect(80, 350, 90, 90))
        self.condition_logo.setPixmap(QtGui.QPixmap(os.getcwd()+'/img/condition.jpg'))

        self.temperature_view = QtWidgets.QLabel(self)
        self.temperature_view.setGeometry(QtCore.QRect(180, 50, 250, 90))
        self.temperature_view.setStyleSheet("background-color: white; color: black;border-style: outset; border-radius: 5px; border-color: #E07626; border-width: 2px")


        self.humidity_view = QtWidgets.QLabel(self)
        self.humidity_view.setGeometry(QtCore.QRect(190, 150, 250, 90))
        self.humidity_view.setStyleSheet("background-color: white; color: black;border-style: outset; border-radius: 5px; border-color: #E07626; border-width: 2px")


        self.windspeed_view = QtWidgets.QLabel(self)
        self.windspeed_view.setGeometry(QtCore.QRect(200, 250, 250, 90))
        self.windspeed_view.setStyleSheet("background-color: white; color: black;border-style: outset; border-radius: 5px; border-color: #E07626; border-width: 2px")


        self.condition_view = QtWidgets.QLabel(self)
        self.condition_view.setGeometry(QtCore.QRect(210, 350, 250, 90))
        self.condition_view.setStyleSheet("background-color: white; color: black;border-style: outset; border-radius: 5px; border-color: #E07626; border-width: 2px")


        self.view_list = []
        self.view_list.append(self.temperature_view)
        self.view_list.append(self.humidity_view)
        self.view_list.append(self.windspeed_view)
        self.view_list.append(self.condition_view)

        for view in self.view_list:
            view.setFont(location_font)

        self.control_location_btn = QtWidgets.QPushButton(self)
        self.control_location_btn.setGeometry(QtCore.QRect(475, 460, 80, 40))
        self.control_location_btn.setObjectName("pushButton")
        self.control_location_btn.setStyleSheet("background-color: #404040; color: white;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")

        self.control_location_btn.clicked.connect(lambda: self.control_location())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.control_location_btn.setText(_translate("Form", "지역 설정"))

    def control_location(self):
        self.input_location = Input_Location(self)
        self.input_location.show()

        self.input_location.new_signal.connect(self.view_weather)

    def view_weather(self):
        location = self.input_location.send_location()

        self.location_logo.setText(location)
        
        weather_infos = weather.weather(location)
            
        for i in range(0, len(weather_infos)):
            weather_infos[i] = str(weather_infos[i])
            if i == 0:
                weather_infos[i] = weather_infos[i] + ' ℃'
            if i == 1:
                weather_infos[i] = weather_infos[i] + ' %'
            if i == 2:
                weather_infos[i] = weather_infos[i] + ' m/s'
                
            self.view_list[i].setText(weather_infos[i])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Weather_widget()
    #Form.show()
    sys.exit(app.exec_())

