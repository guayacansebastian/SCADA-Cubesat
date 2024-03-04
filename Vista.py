# -*- coding: utf-8 -*-

from PyQt5 import *

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qwt_plot import QwtPlot
from qwt_analog_clock import QwtAnalogClock
from qwt_dial import QwtDial
from qwt_thermo import QwtThermo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(649, 482)
        MainWindow.setMinimumSize(QSize(35, 35))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(False)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"QFrame { \n"
"background-color:rgb(94, 92, 100);\n"
"}\n"
"QPushButton{\n"
"background-color :rgb(220, 138, 221);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color :rgb(220, 138, 221);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(192, 97, 203);\n"
"font: 75 20pt \"Ubuntu\";")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.frame_superior)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(35, 35))
        self.pushButton.setStyleSheet(u"backgorind-color:rgb(0, 0, 0)")
        icon = QIcon()
        icon.addFile(u"../gui-python-pyqt5-main/Menu Lateral desplegable/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.frame_superior)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(35, 35))
        self.pushButton_4.setStyleSheet(u"backgorind-color:rgb(0, 0, 0)")
        icon1 = QIcon()
        icon1.addFile(u"../gui-python-pyqt5-main/Menu Lateral desplegable/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_superior)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(35, 35))
        self.pushButton_3.setStyleSheet(u"backgorind-color:rgb(0, 0, 0)")
        icon2 = QIcon()
        icon2.addFile(u"../gui-python-pyqt5-main/Menu Lateral desplegable/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_superior)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(35, 35))
        self.pushButton_2.setStyleSheet(u"backgorind-color:rgb(0, 0, 0)")
        icon3 = QIcon()
        icon3.addFile(u"../gui-python-pyqt5-main/Menu Lateral desplegable/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_left = QFrame(self.frame_contenido)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_buttons = QFrame(self.frame_left)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setStyleSheet(u"QFrame { \n"
"background-color:rgb(154, 153, 150);\n"
"}\n"
"QPushButton{\n"
"background-color :color: rgb(246, 245, 244);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color :rgb(220, 138, 221);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_buttons)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_soltar = QPushButton(self.frame_buttons)
        self.pushButton_soltar.setObjectName(u"pushButton_soltar")
        self.pushButton_soltar.setStyleSheet(u"text-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_soltar)

        self.pushButton_foto = QPushButton(self.frame_buttons)
        self.pushButton_foto.setObjectName(u"pushButton_foto")

        self.verticalLayout.addWidget(self.pushButton_foto)

        self.pushButton_abrir = QPushButton(self.frame_buttons)
        self.pushButton_abrir.setObjectName(u"pushButton_abrir")

        self.verticalLayout.addWidget(self.pushButton_abrir)

        self.pushButton_guardar = QPushButton(self.frame_buttons)
        self.pushButton_guardar.setObjectName(u"pushButton_guardar")

        self.verticalLayout.addWidget(self.pushButton_guardar)


        self.verticalLayout_3.addWidget(self.frame_buttons)

        self.frame_notifications = QFrame(self.frame_left)
        self.frame_notifications.setObjectName(u"frame_notifications")
        self.frame_notifications.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.frame_notifications.setFrameShape(QFrame.StyledPanel)
        self.frame_notifications.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_notifications)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_notifications)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(192, 97, 203);\n"
"font: 75 18pt \"Ubuntu\";\n"
"")

        self.gridLayout_8.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.listWidget = QListWidget(self.frame_notifications)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"background-color:rgb(228, 207, 233)")

        self.gridLayout_8.addWidget(self.listWidget, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.frame_notifications)

        self.verticalLayout_3.setStretch(0, 6)
        self.verticalLayout_3.setStretch(1, 5)

        self.horizontalLayout.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame_contenido)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setStyleSheet(u"background-color: rgb(154, 153, 150);")
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_right)
        self.gridLayout.setObjectName(u"gridLayout")
        self.orientacion = QWidget(self.frame_right)
        self.orientacion.setObjectName(u"orientacion")
        self.gridLayout_2 = QGridLayout(self.orientacion)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.orientacion)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.qwtPlot = QwtPlot(self.orientacion)
        self.qwtPlot.setObjectName(u"qwtPlot")
        font = QFont()
        font.setPointSize(5)
        self.qwtPlot.setFont(font)
        self.qwtPlot.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qwtPlot.setLineWidth(1)
        self.qwtPlot.setAutoReplot(True)

        self.gridLayout_2.addWidget(self.qwtPlot, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.orientacion, 0, 0, 1, 1)

        self.ubicacion = QWidget(self.frame_right)
        self.ubicacion.setObjectName(u"ubicacion")
        self.gridLayout_3 = QGridLayout(self.ubicacion)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.ubicacion)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.qwtPlot_3 = QwtPlot(self.ubicacion)
        self.qwtPlot_3.setObjectName(u"qwtPlot_3")
        self.qwtPlot_3.setFont(font)
        self.qwtPlot_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qwtPlot_3.setLineWidth(1)
        self.qwtPlot_3.setAutoReplot(True)

        self.gridLayout_3.addWidget(self.qwtPlot_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.ubicacion, 0, 1, 1, 1)

        self.altura = QWidget(self.frame_right)
        self.altura.setObjectName(u"altura")
        self.gridLayout_4 = QGridLayout(self.altura)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.altura)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.qwtPlot_2 = QwtPlot(self.altura)
        self.qwtPlot_2.setObjectName(u"qwtPlot_2")
        self.qwtPlot_2.setFont(font)
        self.qwtPlot_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qwtPlot_2.setLineWidth(1)
        self.qwtPlot_2.setAutoReplot(True)

        self.gridLayout_4.addWidget(self.qwtPlot_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.altura, 1, 0, 1, 1)

        self.velocidad = QWidget(self.frame_right)
        self.velocidad.setObjectName(u"velocidad")
        self.gridLayout_5 = QGridLayout(self.velocidad)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_6 = QLabel(self.velocidad)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.qwtPlot_4 = QwtPlot(self.velocidad)
        self.qwtPlot_4.setObjectName(u"qwtPlot_4")
        self.qwtPlot_4.setFont(font)
        self.qwtPlot_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qwtPlot_4.setLineWidth(1)
        self.qwtPlot_4.setAutoReplot(True)

        self.gridLayout_5.addWidget(self.qwtPlot_4, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.velocidad, 1, 1, 1, 1)

        self.aceleracion = QWidget(self.frame_right)
        self.aceleracion.setObjectName(u"aceleracion")
        self.gridLayout_7 = QGridLayout(self.aceleracion)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_7 = QLabel(self.aceleracion)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)

        self.qwtPlot_5 = QwtPlot(self.aceleracion)
        self.qwtPlot_5.setObjectName(u"qwtPlot_5")
        self.qwtPlot_5.setFont(font)
        self.qwtPlot_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qwtPlot_5.setLineWidth(1)
        self.qwtPlot_5.setAutoReplot(True)

        self.gridLayout_7.addWidget(self.qwtPlot_5, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.aceleracion, 2, 0, 1, 1)

        self.widget_6 = QWidget(self.frame_right)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_6 = QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.AnalogClock = QwtAnalogClock(self.widget_6)
        self.AnalogClock.setObjectName(u"AnalogClock")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnalogClock.sizePolicy().hasHeightForWidth())
        self.AnalogClock.setSizePolicy(sizePolicy)
        self.AnalogClock.setFont(font)
        self.AnalogClock.setUpperBound(43200.000000000000000)
        self.AnalogClock.setLineWidth(4)
        self.AnalogClock.setMode(QwtDial.RotateScale)
        self.AnalogClock.setOrigin(270.000000000000000)

        self.gridLayout_6.addWidget(self.AnalogClock, 0, 0, 1, 1)

        self.Thermo = QwtThermo(self.widget_6)
        self.Thermo.setObjectName(u"Thermo")
        self.Thermo.setFont(font)
        self.Thermo.setUpperBound(60.000000000000000)
        self.Thermo.setScaleMaxMinor(25)
        self.Thermo.setValue(18.000000000000000)

        self.gridLayout_6.addWidget(self.Thermo, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_6, 2, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout.addWidget(self.frame_right)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)

        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout_4.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SCADA", None))
        self.pushButton.setText("")
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton_soltar.setText(QCoreApplication.translate("MainWindow", u"Desacoplar Globo", None))
        self.pushButton_foto.setText(QCoreApplication.translate("MainWindow", u"Tomar Foto", None))
        self.pushButton_abrir.setText(QCoreApplication.translate("MainWindow", u"Guardar Reporte", None))
        self.pushButton_guardar.setText(QCoreApplication.translate("MainWindow", u"Abrir Reporte", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Alertas", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Orientacion", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ubicacion", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Altura", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Aceleracion", None))
    # retranslateUi

