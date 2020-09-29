from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import threading
import sys
import cv2
import imutils
import time
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 1850)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 1850))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 1480, 311, 251))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 291, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 4, 0, 1, 1)
        self.dato_velocidadVehiculo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dato_velocidadVehiculo.setObjectName("dato_velocidadVehiculo")
        self.gridLayout.addWidget(self.dato_velocidadVehiculo, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.dato_volante = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dato_volante.setObjectName("dato_volante")
        self.gridLayout.addWidget(self.dato_volante, 4, 1, 1, 1)
        self.dato_atencionConductor = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dato_atencionConductor.setObjectName("dato_atencionConductor")
        self.gridLayout.addWidget(self.dato_atencionConductor, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)
        self.dato_interseccion = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dato_interseccion.setObjectName("dato_interseccion")
        self.gridLayout.addWidget(self.dato_interseccion, 6, 1, 1, 1)
        self.dato_aceleracionVehiculo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dato_aceleracionVehiculo.setObjectName("dato_aceleracionVehiculo")
        self.gridLayout.addWidget(self.dato_aceleracionVehiculo, 1, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 3, 0, 1, 1)
        self.dato_Acelerador = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dato_Acelerador.setObjectName("dato_Acelerador")
        self.gridLayout.addWidget(self.dato_Acelerador, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.dato_interseccion_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dato_interseccion_2.setObjectName("dato_interseccion_2")
        self.gridLayout.addWidget(self.dato_interseccion_2, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.dato_freno = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dato_freno.setObjectName("dato_freno")
        self.gridLayout.addWidget(self.dato_freno, 3, 1, 1, 1)
        self.Camaras = QtWidgets.QGroupBox(self.centralwidget)
        self.Camaras.setGeometry(QtCore.QRect(320, 0, 681, 771))
        self.Camaras.setObjectName("Camaras")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.Camaras)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 30, 671, 732))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CamaraCentral = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CamaraCentral.sizePolicy().hasHeightForWidth())
        self.CamaraCentral.setSizePolicy(sizePolicy)
        self.CamaraCentral.setMinimumSize(QtCore.QSize(640, 480))
        self.CamaraCentral.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CamaraCentral.setFont(font)
        self.CamaraCentral.setFrameShape(QtWidgets.QFrame.Box)
        self.CamaraCentral.setObjectName("CamaraCentral")
        self.horizontalLayout_5.addWidget(self.CamaraCentral)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.CamaraLat1 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.CamaraLat1.setMinimumSize(QtCore.QSize(320, 240))
        self.CamaraLat1.setMaximumSize(QtCore.QSize(320, 240))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CamaraLat1.setFont(font)
        self.CamaraLat1.setFrameShape(QtWidgets.QFrame.Box)
        self.CamaraLat1.setObjectName("CamaraLat1")
        self.horizontalLayout_6.addWidget(self.CamaraLat1)
        self.CamaraLat2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.CamaraLat2.setMinimumSize(QtCore.QSize(320, 240))
        self.CamaraLat2.setMaximumSize(QtCore.QSize(320, 240))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.CamaraLat2.setFont(font)
        self.CamaraLat2.setFrameShape(QtWidgets.QFrame.Box)
        self.CamaraLat2.setObjectName("CamaraLat2")
        self.horizontalLayout_6.addWidget(self.CamaraLat2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 1740, 1001, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 1023, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 8, 1, 1)
        self.metricas_numSemaforos = QtWidgets.QLabel(
            self.horizontalLayoutWidget)
        self.metricas_numSemaforos.setObjectName("metricas_numSemaforos")
        self.gridLayout_2.addWidget(self.metricas_numSemaforos, 1, 7, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 6, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 6, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 8, 1, 1)
        self.metricas_fpsVision = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.metricas_fpsVision.setObjectName("metricas_fpsVision")
        self.gridLayout_2.addWidget(self.metricas_fpsVision, 0, 1, 1, 1)
        self.fpsVision_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fpsVision_2.setObjectName("fpsVision_2")
        self.gridLayout_2.addWidget(self.fpsVision_2, 1, 5, 1, 1)
        self.metricas_fpsDetect = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.metricas_fpsDetect.setObjectName("metricas_fpsDetect")
        self.gridLayout_2.addWidget(self.metricas_fpsDetect, 0, 3, 1, 1)
        self.metricas_fpsInterseccion = QtWidgets.QLabel(
            self.horizontalLayoutWidget)
        self.metricas_fpsInterseccion.setObjectName("metricas_fpsInterseccion")
        self.gridLayout_2.addWidget(self.metricas_fpsInterseccion, 0, 9, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.metricas_fpsSemaforos = QtWidgets.QLabel(
            self.horizontalLayoutWidget)
        self.metricas_fpsSemaforos.setObjectName("metricas_fpsSemaforos")
        self.gridLayout_2.addWidget(self.metricas_fpsSemaforos, 0, 7, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 1, 9, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 311, 1051))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 291, 1015))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.indicador_velocidad = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(75)
        self.indicador_velocidad.setFont(font)
        self.indicador_velocidad.setAlignment(QtCore.Qt.AlignCenter)
        self.indicador_velocidad.setObjectName("indicador_velocidad")
        self.horizontalLayout.addWidget(self.indicador_velocidad)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.indicador_limite = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.indicador_limite.setEnabled(True)
        self.indicador_limite.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_limite.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_limite.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_limite.setObjectName("indicador_limite")
        self.horizontalLayout_3.addWidget(
            self.indicador_limite, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.indicador_stop = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.indicador_stop.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_stop.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_stop.setFrameShape(QtWidgets.QFrame.Panel)
        self.indicador_stop.setText("")
        self.indicador_stop.setObjectName("indicador_stop")
        self.horizontalLayout_4.addWidget(self.indicador_stop)
        self.indicador_semaf = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.indicador_semaf.setMinimumSize(QtCore.QSize(50, 100))
        self.indicador_semaf.setMaximumSize(QtCore.QSize(50, 100))
        self.indicador_semaf.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_semaf.setText("")
        self.indicador_semaf.setAlignment(QtCore.Qt.AlignCenter)
        self.indicador_semaf.setObjectName("indicador_semaf")
        self.horizontalLayout_4.addWidget(self.indicador_semaf)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.indicador_conductor_img = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_conductor_img.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_conductor_img.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_conductor_img.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_conductor_img.setText("")
        self.indicador_conductor_img.setObjectName("indicador_conductor_img")
        self.horizontalLayout_7.addWidget(self.indicador_conductor_img)
        self.indicador_conductor_img_zzz = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_conductor_img_zzz.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_conductor_img_zzz.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_conductor_img_zzz.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_conductor_img_zzz.setText("")
        self.indicador_conductor_img_zzz.setObjectName(
            "indicador_conductor_img_zzz")
        self.horizontalLayout_7.addWidget(self.indicador_conductor_img_zzz)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.indicador_predicciones_1 = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_predicciones_1.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_predicciones_1.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_predicciones_1.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_predicciones_1.setObjectName("indicador_predicciones_1")
        self.horizontalLayout_8.addWidget(self.indicador_predicciones_1)
        self.indicador_predicciones_2 = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_predicciones_2.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_predicciones_2.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_predicciones_2.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_predicciones_2.setObjectName("indicador_predicciones_2")
        self.horizontalLayout_8.addWidget(self.indicador_predicciones_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.indicador_vehicCerca1 = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_vehicCerca1.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_vehicCerca1.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_vehicCerca1.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_vehicCerca1.setText("")
        self.indicador_vehicCerca1.setObjectName("indicador_vehicCerca1")
        self.horizontalLayout_11.addWidget(self.indicador_vehicCerca1)
        self.indicador_vehicCerca2 = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_vehicCerca2.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_vehicCerca2.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_vehicCerca2.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_vehicCerca2.setText("")
        self.indicador_vehicCerca2.setObjectName("indicador_vehicCerca2")
        self.horizontalLayout_11.addWidget(self.indicador_vehicCerca2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_9.addWidget(self.label_25)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.indicador_flecha_recto = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_flecha_recto.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_recto.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_recto.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_flecha_recto.setObjectName("indicador_flecha_recto")
        self.horizontalLayout_16.addWidget(self.indicador_flecha_recto)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.indicador_flecha_izq = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.indicador_flecha_izq.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_izq.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_izq.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_flecha_izq.setObjectName("indicador_flecha_izq")
        self.horizontalLayout_10.addWidget(self.indicador_flecha_izq)
        self.indicador_flecha_der = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.indicador_flecha_der.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_der.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_der.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_flecha_der.setObjectName("indicador_flecha_der")
        self.horizontalLayout_10.addWidget(self.indicador_flecha_der)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.indicador_flecha_rectoYizq = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_flecha_rectoYizq.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_rectoYizq.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_rectoYizq.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_flecha_rectoYizq.setObjectName(
            "indicador_flecha_rectoYizq")
        self.horizontalLayout_15.addWidget(self.indicador_flecha_rectoYizq)
        self.indicador_flecha_rectoYder = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.indicador_flecha_rectoYder.setMinimumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_rectoYder.setMaximumSize(QtCore.QSize(100, 100))
        self.indicador_flecha_rectoYder.setFrameShape(QtWidgets.QFrame.Box)
        self.indicador_flecha_rectoYder.setObjectName(
            "indicador_flecha_rectoYder")
        self.horizontalLayout_15.addWidget(self.indicador_flecha_rectoYder)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(320, 780, 681, 951))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.proc_vista360 = QtWidgets.QLabel(self.tab)
        self.proc_vista360.setGeometry(QtCore.QRect(20, 30, 630, 875))
        self.proc_vista360.setMinimumSize(QtCore.QSize(630, 875))
        self.proc_vista360.setMaximumSize(QtCore.QSize(630, 875))
        self.proc_vista360.setFrameShape(QtWidgets.QFrame.Box)
        self.proc_vista360.setObjectName("proc_vista360")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.proc_vista360_2 = QtWidgets.QLabel(self.tab_2)
        self.proc_vista360_2.setGeometry(QtCore.QRect(20, 30, 630, 875))
        self.proc_vista360_2.setMinimumSize(QtCore.QSize(630, 875))
        self.proc_vista360_2.setMaximumSize(QtCore.QSize(630, 875))
        self.proc_vista360_2.setFrameShape(QtWidgets.QFrame.Box)
        self.proc_vista360_2.setObjectName("proc_vista360_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 651, 901))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.roadDirector_wheelImg_real = QtWidgets.QLabel(self.groupBox_3)
        self.roadDirector_wheelImg_real.setGeometry(
            QtCore.QRect(10, 80, 300, 300))
        self.roadDirector_wheelImg_real.setMinimumSize(QtCore.QSize(300, 300))
        self.roadDirector_wheelImg_real.setMaximumSize(QtCore.QSize(100, 100))
        self.roadDirector_wheelImg_real.setFrameShape(QtWidgets.QFrame.Box)
        self.roadDirector_wheelImg_real.setObjectName(
            "roadDirector_wheelImg_real")
        self.horizontalLayout_19.addWidget(self.groupBox_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.roadDirector_wheelImg_predicted = QtWidgets.QLabel(
            self.groupBox_5)
        self.roadDirector_wheelImg_predicted.setGeometry(
            QtCore.QRect(10, 80, 300, 300))
        self.roadDirector_wheelImg_predicted.setMinimumSize(
            QtCore.QSize(300, 300))
        self.roadDirector_wheelImg_predicted.setMaximumSize(
            QtCore.QSize(100, 100))
        self.roadDirector_wheelImg_predicted.setAutoFillBackground(False)
        self.roadDirector_wheelImg_predicted.setFrameShape(
            QtWidgets.QFrame.Box)
        self.roadDirector_wheelImg_predicted.setObjectName(
            "roadDirector_wheelImg_predicted")
        self.horizontalLayout_19.addWidget(self.groupBox_5)
        self.verticalLayout_14.addLayout(self.horizontalLayout_19)
        self.tabWidget.addTab(self.tab_3, "")
        self.notificaciones = QtWidgets.QGroupBox(self.centralwidget)
        self.notificaciones.setGeometry(QtCore.QRect(0, 1060, 311, 411))
        self.notificaciones.setObjectName("notificaciones")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.notificaciones)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 291, 371))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.listaNotificaciones = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.listaNotificaciones.setContentsMargins(0, 0, 0, 0)
        self.listaNotificaciones.setObjectName("listaNotificaciones")
        self.notif_conductorDesconectado = QtWidgets.QGroupBox(
            self.verticalLayoutWidget_2)
        self.notif_conductorDesconectado.setMinimumSize(QtCore.QSize(0, 80))
        self.notif_conductorDesconectado.setMaximumSize(
            QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setKerning(False)
        self.notif_conductorDesconectado.setFont(font)
        self.notif_conductorDesconectado.setStyleSheet("background : #FFB732")
        self.notif_conductorDesconectado.setTitle("")
        self.notif_conductorDesconectado.setFlat(False)
        self.notif_conductorDesconectado.setCheckable(False)
        self.notif_conductorDesconectado.setObjectName(
            "notif_conductorDesconectado")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(
            self.notif_conductorDesconectado)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 291, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_11.setMinimumSize(QtCore.QSize(55, 50))
        self.label_11.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Color Emoji")
        font.setPointSize(40)
        font.setKerning(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet("color: black")
        self.label_22.setScaledContents(False)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_10.addWidget(self.label_22)
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_26.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color : black")
        self.label_26.setScaledContents(True)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_10.addWidget(self.label_26)
        self.horizontalLayout_9.addLayout(self.verticalLayout_10)
        self.listaNotificaciones.addWidget(self.notif_conductorDesconectado)
        self.notif_conductorDistraido = QtWidgets.QGroupBox(
            self.verticalLayoutWidget_2)
        self.notif_conductorDistraido.setMinimumSize(QtCore.QSize(0, 80))
        self.notif_conductorDistraido.setMaximumSize(
            QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setKerning(False)
        self.notif_conductorDistraido.setFont(font)
        self.notif_conductorDistraido.setStyleSheet("background : #CC0000")
        self.notif_conductorDistraido.setTitle("")
        self.notif_conductorDistraido.setFlat(False)
        self.notif_conductorDistraido.setCheckable(False)
        self.notif_conductorDistraido.setObjectName("notif_conductorDistraido")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(
            self.notif_conductorDistraido)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 291, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_27.setMinimumSize(QtCore.QSize(55, 50))
        self.label_27.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Color Emoji")
        font.setPointSize(40)
        font.setKerning(False)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_12.addWidget(self.label_27)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setScaledContents(False)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_11.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_29.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setScaledContents(True)
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_11.addWidget(self.label_29)
        self.horizontalLayout_12.addLayout(self.verticalLayout_11)
        self.listaNotificaciones.addWidget(self.notif_conductorDistraido)
        self.notif_limiteVelocidad = QtWidgets.QGroupBox(
            self.verticalLayoutWidget_2)
        self.notif_limiteVelocidad.setMinimumSize(QtCore.QSize(0, 80))
        self.notif_limiteVelocidad.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setKerning(False)
        self.notif_limiteVelocidad.setFont(font)
        self.notif_limiteVelocidad.setStyleSheet("background : #CC0000")
        self.notif_limiteVelocidad.setTitle("")
        self.notif_limiteVelocidad.setFlat(False)
        self.notif_limiteVelocidad.setCheckable(False)
        self.notif_limiteVelocidad.setObjectName("notif_limiteVelocidad")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(
            self.notif_limiteVelocidad)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 291, 81))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_5)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_35 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_35.setMinimumSize(QtCore.QSize(55, 50))
        self.label_35.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Color Emoji")
        font.setPointSize(40)
        font.setKerning(False)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_14.addWidget(self.label_35)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_36 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setScaledContents(False)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_13.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_37.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setScaledContents(True)
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_13.addWidget(self.label_37)
        self.horizontalLayout_14.addLayout(self.verticalLayout_13)
        self.listaNotificaciones.addWidget(self.notif_limiteVelocidad)
        self.notif_cambioSemaforo = QtWidgets.QGroupBox(
            self.verticalLayoutWidget_2)
        self.notif_cambioSemaforo.setMinimumSize(QtCore.QSize(0, 80))
        self.notif_cambioSemaforo.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setKerning(False)
        self.notif_cambioSemaforo.setFont(font)
        self.notif_cambioSemaforo.setStyleSheet("background : #4CA6FF")
        self.notif_cambioSemaforo.setTitle("")
        self.notif_cambioSemaforo.setFlat(False)
        self.notif_cambioSemaforo.setCheckable(False)
        self.notif_cambioSemaforo.setObjectName("notif_cambioSemaforo")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(
            self.notif_cambioSemaforo)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 291, 81))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_4)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_32 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_32.setMinimumSize(QtCore.QSize(55, 50))
        self.label_32.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Color Emoji")
        font.setPointSize(40)
        font.setKerning(False)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_13.addWidget(self.label_32)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_33 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setScaledContents(False)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_12.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_34.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setScaledContents(True)
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_12.addWidget(self.label_34)
        self.horizontalLayout_13.addLayout(self.verticalLayout_12)
        self.listaNotificaciones.addWidget(self.notif_cambioSemaforo)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.listaNotificaciones.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionCerrar_GUI = QtWidgets.QAction(MainWindow)
        self.actionCerrar_GUI.setObjectName("actionCerrar_GUI")
        self.actionCerrar_Aplicacion = QtWidgets.QAction(MainWindow)
        self.actionCerrar_Aplicacion.setObjectName("actionCerrar_Aplicacion")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionTest_Action = QtWidgets.QAction(MainWindow)
        self.actionTest_Action.setObjectName("actionTest_Action")
        self.actionCerrar_GUI_2 = QtWidgets.QAction(MainWindow)
        self.actionCerrar_GUI_2.setObjectName("actionCerrar_GUI_2")
        self.actionCerrar_Aplicacion_2 = QtWidgets.QAction(MainWindow)
        self.actionCerrar_Aplicacion_2.setObjectName(
            "actionCerrar_Aplicacion_2")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Sistema Integral de Ayuda a la conduccion - GUI"))
        self.groupBox.setTitle(_translate("MainWindow", "Otros datos"))
        self.label_31.setText(_translate("MainWindow", "Posicion Volante"))
        self.dato_velocidadVehiculo.setText(
            _translate("MainWindow", "velocidad"))
        self.label_3.setText(_translate("MainWindow", "Intersección"))
        self.dato_volante.setText(_translate("MainWindow", "volante"))
        self.dato_atencionConductor.setText(
            _translate("MainWindow", "AtencionCond"))
        self.label_14.setText(_translate("MainWindow", "Conductor"))
        self.dato_interseccion.setText(
            _translate("MainWindow", "Interseccion"))
        self.dato_aceleracionVehiculo.setText(
            _translate("MainWindow", "aceleracion"))
        self.label_30.setText(_translate("MainWindow", "Posicion Freno"))
        self.dato_Acelerador.setText(_translate("MainWindow", "acelerador"))
        self.label_8.setText(_translate("MainWindow", "Velocidad vehiculo"))
        self.dato_interseccion_2.setText(
            _translate("MainWindow", "Posicion Acelerador"))
        self.label_5.setText(_translate("MainWindow", "Aceleracion vehiculo"))
        self.dato_freno.setText(_translate("MainWindow", "freno"))
        self.Camaras.setTitle(_translate(
            "MainWindow", "Cámaras + Object detection"))
        self.CamaraCentral.setText(_translate("MainWindow", "Camara central"))
        self.CamaraLat1.setText(_translate("MainWindow", "Camara Lateral 1"))
        self.CamaraLat2.setText(_translate("MainWindow", "Camara Lateral 2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Métricas"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "FPS Object detection:"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.metricas_numSemaforos.setText(
            _translate("MainWindow", "# semaforos"))
        self.label_24.setText(_translate("MainWindow", "Marcas calzada:"))
        self.label_9.setText(_translate("MainWindow", "FPS semáforos:"))
        self.label_19.setText(_translate("MainWindow", "Numero semáforos:"))
        self.label_12.setText(_translate("MainWindow", "FPS Interseccion:"))
        self.metricas_fpsVision.setText(_translate("MainWindow", "FPS"))
        self.fpsVision_2.setText(_translate("MainWindow", "FPS"))
        self.metricas_fpsDetect.setText(_translate("MainWindow", "FPS_detect"))
        self.metricas_fpsInterseccion.setText(
            _translate("MainWindow", "fps_interseccion"))
        self.label_16.setText(_translate("MainWindow", "marcasCalzada"))
        self.label_23.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "FPS:"))
        self.metricas_fpsSemaforos.setText(
            _translate("MainWindow", "fps_semaf"))
        self.label_21.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Velocidad"))
        self.indicador_velocidad.setText(_translate("MainWindow", "120"))
        self.label_6.setText(_translate("MainWindow", "Km/h"))
        self.label_7.setText(_translate("MainWindow", "Límite:"))
        self.indicador_limite.setText(_translate("MainWindow", "TODO"))
        self.label_10.setText(_translate("MainWindow", "STOP/Semáforo:"))
        self.label_13.setText(_translate(
            "MainWindow", "Atencion del conductor"))
        self.label_15.setText(_translate("MainWindow", "Predicciones IA"))
        self.indicador_predicciones_1.setText(
            _translate("MainWindow", "Interseccion"))
        self.indicador_predicciones_2.setText(_translate("MainWindow", "TODO"))
        self.label_25.setText(_translate(
            "MainWindow", "Analisis marcas calzada"))
        self.indicador_flecha_recto.setText(
            _translate("MainWindow", "fecha recta"))
        self.indicador_flecha_izq.setText(
            _translate("MainWindow", "flecha izq"))
        self.indicador_flecha_der.setText(
            _translate("MainWindow", "flecha der"))
        self.indicador_flecha_rectoYizq.setText(
            _translate("MainWindow", "recto_izq"))
        self.indicador_flecha_rectoYder.setText(
            _translate("MainWindow", "recto_der"))
        self.proc_vista360.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "Vista Cenital RGB"))
        self.proc_vista360_2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Vista Cenital Lineas"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Real"))
        self.roadDirector_wheelImg_real.setText(
            _translate("MainWindow", "TextLabel"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Predicted"))
        self.roadDirector_wheelImg_predicted.setText(
            _translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), _translate("MainWindow", "Road Director"))
        self.notificaciones.setTitle(
            _translate("MainWindow", "Notificaciones"))
        self.label_11.setText(_translate("MainWindow", "⚠️"))
        self.label_22.setText(_translate(
            "MainWindow", "Conductor desconectado!"))
        self.label_26.setText(_translate(
            "MainWindow", "El servidor de atencion del conductor esta desconectado"))
        self.label_27.setText(_translate("MainWindow", "⚠️"))
        self.label_28.setText(_translate("MainWindow", "Conductor distraido!"))
        self.label_29.setText(_translate(
            "MainWindow", "Mantengase atento a la carretera"))
        self.label_35.setText(_translate("MainWindow", "👮"))
        self.label_36.setText(_translate("MainWindow", "Limite de velocidad"))
        self.label_37.setText(_translate(
            "MainWindow", "Ha sobrepasado el limite de velocidad. Reduzca velocidad"))
        self.label_32.setText(_translate("MainWindow", "🚦"))
        self.label_33.setText(_translate("MainWindow", "Semaforo en verde"))
        self.label_34.setText(_translate(
            "MainWindow", "El semáforo ha cambiado. Puede reanudar la marcha."))
        self.actionCerrar_GUI.setText(_translate("MainWindow", "Cerrar GUI"))
        self.actionCerrar_Aplicacion.setText(
            _translate("MainWindow", "Cerrar Aplicacion"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionTest_Action.setText(_translate("MainWindow", "Test Action"))
        self.actionCerrar_GUI_2.setText(_translate("MainWindow", "Cerrar GUI"))
        self.actionCerrar_Aplicacion_2.setText(
            _translate("MainWindow", "Cerrar Aplicacion"))



class Ui_PantallaCargaTFG(object):
    def setupUi(self, PantallaCargaTFG):
        PantallaCargaTFG.setObjectName("PantallaCargaTFG")
        PantallaCargaTFG.resize(800, 600)
        PantallaCargaTFG.setMinimumSize(QtCore.QSize(800, 600))
        PantallaCargaTFG.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(PantallaCargaTFG)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 801, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(500, 300))
        self.label_2.setMaximumSize(QtCore.QSize(500, 300))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setMinimumSize(QtCore.QSize(600, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem13 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        spacerItem14 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.imagenescuela = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.imagenescuela.setMinimumSize(QtCore.QSize(331, 61))
        self.imagenescuela.setMaximumSize(QtCore.QSize(331, 61))
        self.imagenescuela.setText("")
        self.imagenescuela.setPixmap(QtGui.QPixmap(
            "../Documentacion/MemoriaJuan/Presentacion/imgs/logo-ETSII-US-Horizontal-Color.png"))
        self.imagenescuela.setScaledContents(True)
        self.imagenescuela.setObjectName("imagenescuela")
        self.horizontalLayout_7.addWidget(self.imagenescuela)
        spacerItem15 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        PantallaCargaTFG.setCentralWidget(self.centralwidget)

        self.retranslateUi(PantallaCargaTFG)
        QtCore.QMetaObject.connectSlotsByName(PantallaCargaTFG)

    def retranslateUi(self, PantallaCargaTFG):
        _translate = QtCore.QCoreApplication.translate
        PantallaCargaTFG.setWindowTitle(_translate(
            "PantallaCargaTFG", "Cargando - US-TFG-SistemaAyudaConducción"))
        self.label_2.setText(_translate("PantallaCargaTFG", "Imagen"))
        self.label_3.setText(_translate("PantallaCargaTFG", "Cargando"))
        self.label_4.setText(_translate(
            "PantallaCargaTFG", "Sistema integral de ayuda a la conducción"))
        self.label_7.setText(_translate("PantallaCargaTFG", "Realizado por:"))
        self.label_6.setText(_translate(
            "PantallaCargaTFG", "Juan Arteaga Carmona"))
        self.label_5.setText(_translate(
            "PantallaCargaTFG", "Antonio Jesús Santiago Muñoz"))
        self.label_10.setText(_translate("PantallaCargaTFG", "Dirigido por:"))
        self.label_9.setText(_translate(
            "PantallaCargaTFG", "Manuel Jesús Domínguez Morales"))
        self.label_11.setText(_translate(
            "PantallaCargaTFG", "Universidad de Sevilla"))
        self.label_12.setText(_translate(
            "PantallaCargaTFG", "Curso 2019/2020"))
        self.label_13.setText(_translate(
            "PantallaCargaTFG", "Grado en Ingeniería Informática - Tecnologías informáticas"))

        _translate = QtCore.QCoreApplication.translate
        PantallaCargaTFG.setWindowTitle(_translate(
            "PantallaCargaTFG", "Cargando - US-TFG-SistemaAyudaConducción"))
        self.label_2.setText(_translate("PantallaCargaTFG", "Imagen"))
        self.label_3.setText(_translate("PantallaCargaTFG", "Cargando"))
        self.label_4.setText(_translate(
            "PantallaCargaTFG", "Sistema integral de ayuda a la conducción"))
        self.label_7.setText(_translate("PantallaCargaTFG", "Realizado por:"))
        self.label_6.setText(_translate(
            "PantallaCargaTFG", "Juan Arteaga Carmona"))
        self.label_5.setText(_translate(
            "PantallaCargaTFG", "Antonio Jesús Santiago Muñoz"))
        self.label_10.setText(_translate("PantallaCargaTFG", "Dirigido por:"))
        self.label_9.setText(_translate(
            "PantallaCargaTFG", "Manuel Jesús Domínguez Morales"))
        self.label_11.setText(_translate(
            "PantallaCargaTFG", "Universidad de Sevilla"))
        self.label_12.setText(_translate(
            "PantallaCargaTFG", "Curso 2019/2020"))
        self.label_13.setText(_translate(
            "PantallaCargaTFG", "Grado en Ingeniería Informática - Tecnologías informáticas"))


class InterfazGrafica:

    def __init__(self):

        self.app = QtWidgets.QApplication(sys.argv)
        self.interfazgrafica = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.interfazgrafica)
        self.interfazgrafica.show()

        # Imagen para el bucle de OpenCV
        self.recordatorioCV = cv2.imread('resources/aplicacionContinuaEjecutandose/laAplicacionContinua.png')

        # Imágenes        
        self.semafGenerico = cv2.resize(cv2.imread('resources/guiImg/semaforo_generico.png'), (50,100))
        self.semafVerde = cv2.resize(cv2.imread('resources/guiImg/semaforo_verde.png'), (50, 100))
        self.semafRojo= cv2.resize(cv2.imread('resources/guiImg/semaforo_rojo.png'), (50, 100))

        self.imgConductor= cv2.resize(cv2.imread('resources/guiImg/face-outline.png'), (100, 100))
        self.imgConductorzzz = cv2.resize(cv2.imread('resources/guiImg/sleep.png'), (100, 100))

        self.senyalstop = cv2.resize(cv2.imread('resources/guiImg/stop.png'), (100,100) )
        self.senyalIntersec = cv2.resize(cv2.imread('resources/guiImg/interseccion.png'), (100,100) )
        self.senyalCebra = cv2.resize(cv2.imread('resources/guiImg/cebra.jpg'), (100, 100))

        self.imgVolante = cv2.resize(cv2.imread('resources/guiImg/wheel.png'), (300,300))

        self.limite30 = cv2.resize(cv2.imread('resources/guiImg/Limite_30.png'), (100,100))
        self.limite60 = cv2.resize(cv2.imread('resources/guiImg/Limite_60.png'), (100,100))
        self.limite90 = cv2.resize(cv2.imread('resources/guiImg/Limite_90.png'), (100,100))

        self.flechaRecto = cv2.resize(cv2.imread('resources/guiImg/flechaRecto.png'), (100,100))
        self.flechaRectoYDer = cv2.resize(cv2.imread('resources/guiImg/flechaRectoYDer.png'), (100,100))
        self.flechaRectoYIzq = cv2.resize(cv2.imread('resources/guiImg/flechaRectoYIzq.png'), (100, 100))
        self.flechaDer = cv2.resize(cv2.imread('resources/guiImg/flechaDer.png'), (100,100))
        self.flechaIzq = cv2.resize(cv2.imread('resources/guiImg/flechaIzq.png'), (100, 100))

        self.muertoIzq = cv2.resize(cv2.imread('resources/guiImg/angulomuerto.png'), (100, 100))
        self.muertoDer = cv2.flip(self.muertoIzq, 1)


    def cambiaProgresoLoading(self, num):
        self.ui.progressBar.value = num

    def cargaFinalizada(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.interfazgrafica)
        self.interfazgrafica.show()

        

    def actualizaInfoGui(self, datos):
        #self.DatosGUI = datos

        mainCam, lat1, lat2, velocidad, atencion_conductor, fps_vision, topdown, topDownMasked, semaforo, fps_detect, fps_semafs, num_semafs, interseccion, fps_interseccion, pasoPeatones, existeStop, acelerador, freno, anguloVolante, anguloVolante_predict, notificaConductorSinAtencion, notificaCambioSemaforoVerde, limiteVelocidad, porEncimalimiteVel, senyalizquierda, senyalderecha, senyaldelanteDer, senyaldelanteIzq, vehiculoCercaLat1, vehiculoCercaLat2 = datos


        #Notificaciones
        #Ocultamos todas
        self.ui.notif_cambioSemaforo.setVisible(False)
        self.ui.notif_conductorDesconectado.setVisible(False)
        self.ui.notif_conductorDistraido.setVisible(False)
        self.ui.notif_limiteVelocidad.setVisible(False)


        #Angulo muerto

        muertIzq = self.muertoIzq
        height, width, channel = muertIzq.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(muertIzq.data, width, height,
                            bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.indicador_vehicCerca1.setPixmap(QtGui.QPixmap.fromImage(qImg))
        self.ui.indicador_vehicCerca1.setDisabled(True)

        muertder = self.muertoDer
        height, width, channel = muertder.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(muertder.data, width, height,
                            bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.indicador_vehicCerca2.setPixmap(QtGui.QPixmap.fromImage(qImg))
        self.ui.indicador_vehicCerca2.setDisabled(True)

        if vehiculoCercaLat1:
            self.ui.indicador_vehicCerca1.setDisabled(False)
        if vehiculoCercaLat2:
            self.ui.indicador_vehicCerca2.setDisabled(False)



        #Camara Principal
        mainCam = mainCam.copy()
        height, width, channel = mainCam.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(mainCam.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.CamaraCentral.setPixmap(QtGui.QPixmap.fromImage(qImg))

        #Lateral 1
        lat1 = lat1.copy()
        height, width, channel = lat1.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(lat1.data, width, height,
                            bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.CamaraLat1.setPixmap(QtGui.QPixmap.fromImage(qImg))

        #Lateral 1
        lat2 = lat2.copy()
        height, width, channel = lat2.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(lat2.data, width, height,bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.CamaraLat2.setPixmap(QtGui.QPixmap.fromImage(qImg))

        #TopDown y lineas

        topdown = topdown.copy()
        height, width, channel = topdown.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(topdown.data, width, height,
                            bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.proc_vista360.setPixmap(QtGui.QPixmap.fromImage(qImg))

        topDownMasked = topDownMasked.copy()
        height, width, channel = topDownMasked.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(topDownMasked.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.proc_vista360_2.setPixmap(QtGui.QPixmap.fromImage(qImg))


        #Métricas
        self.ui.metricas_fpsVision.setText(f"{fps_vision:.2f}")
        self.ui.metricas_fpsDetect.setText(f"{fps_detect:.2f}")
        self.ui.metricas_fpsSemaforos.setText(f"{fps_semafs:.2f}")
        self.ui.metricas_numSemaforos.setText(f"{num_semafs}")
        self.ui.metricas_fpsInterseccion.setText(f"{fps_interseccion:.2f}")


        #Datos
        self.ui.dato_velocidadVehiculo.setText(f'{velocidad:.4f} Km/h')
        self.ui.indicador_velocidad.setText(f'{velocidad:.0f}')
        self.ui.dato_Acelerador.setText(f'{acelerador:.2f}')
        self.ui.dato_freno.setText(f'{freno:.2f}')
        self.ui.dato_volante.setText(f'{anguloVolante:.4f}')

        #Atencion del conductor

        height, width, channel = self.imgConductor.shape
        bytesPerLine = 3 * width
        qImg_conductor = QtGui.QImage(self.imgConductor.data, width, height,bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

        height, width, channel = self.imgConductorzzz.shape
        bytesPerLine = 3 * width
        qImg_conductorzzz = QtGui.QImage(
            self.imgConductorzzz.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

        if atencion_conductor:
            self.ui.dato_atencionConductor.setText(f'Atento - {atencion_conductor}')
            myFont = QtGui.QFont()
            myFont.setBold(False)
            myFont.setCapitalization(QtGui.QFont.MixedCase)
            self.ui.dato_atencionConductor.setFont(myFont)
            self.ui.indicador_conductor_img.setPixmap(
                QtGui.QPixmap.fromImage(qImg_conductor))
            self.ui.indicador_conductor_img.setDisabled(False)
            self.ui.indicador_conductor_img_zzz.setVisible(False)


        elif  atencion_conductor is None:
            self.ui.dato_atencionConductor.setText(f'Desconectado - {atencion_conductor}')
            myFont = QtGui.QFont()
            myFont.setBold(False)
            myFont.setCapitalization(QtGui.QFont.MixedCase)
            self.ui.dato_atencionConductor.setFont(myFont)
            self.ui.indicador_conductor_img.setPixmap(
                QtGui.QPixmap.fromImage(qImg_conductor))
            self.ui.indicador_conductor_img.setDisabled(True)
            self.ui.indicador_conductor_img_zzz.setDisabled(True)

            #Notificacion Conductor desconectado
            self.ui.notif_conductorDesconectado.setVisible(True)

        else:
            self.ui.dato_atencionConductor.setText(f'Distraido - {atencion_conductor}')
            myFont = QtGui.QFont()
            myFont.setBold(True)
            myFont.setCapitalization(QtGui.QFont.AllUppercase)
            self.ui.dato_atencionConductor.setFont(myFont)
            self.ui.indicador_conductor_img.setPixmap(QtGui.QPixmap.fromImage(qImg_conductor))
            self.ui.indicador_conductor_img_zzz.setPixmap( QtGui.QPixmap.fromImage(qImg_conductorzzz))
            self.ui.indicador_conductor_img.setDisabled(False)
            self.ui.indicador_conductor_img_zzz.setDisabled(False)
            self.ui.indicador_conductor_img_zzz.setVisible(True)


        #Semaforo
        if semaforo is None:
            semaforo_img = self.semafGenerico.copy()
            qImg = QtGui.QImage(semaforo_img.data, 50, 100,150, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.ui.indicador_semaf.setDisabled(True)
            self.ui.indicador_semaf.setPixmap(QtGui.QPixmap.fromImage(qImg))

        elif semaforo:
            semaforo_img = self.semafVerde.copy()
            qImg = QtGui.QImage(semaforo_img.data, 50, 100, 150, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.ui.indicador_semaf.setDisabled(False)
            self.ui.indicador_semaf.setPixmap(QtGui.QPixmap.fromImage(qImg))
        else:
            semaforo_img = self.semafRojo.copy()
            qImg = QtGui.QImage(semaforo_img.data, 50, 100, 150, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.ui.indicador_semaf.setDisabled(False)
            self.ui.indicador_semaf.setPixmap(QtGui.QPixmap.fromImage(qImg))
            existeStop = True


        #Interseccion

        senyalIntersecc = self.senyalIntersec
        height, width, channel = senyalIntersecc.shape
        bytesPerLine = 3 * width
        qImg_intersec = QtGui.QImage(senyalIntersecc.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

        if interseccion:
            self.ui.indicador_predicciones_1.setPixmap(QtGui.QPixmap.fromImage(qImg_intersec))
            self.ui.indicador_predicciones_1.setDisabled(False)

        else:
            self.ui.indicador_predicciones_1.setDisabled(True)



        #Stop
        senyalstop = self.senyalstop
        height, width, channel = senyalstop.shape
        bytesPerLine = 3 * width
        qImg_stop = QtGui.QImage(senyalstop.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

        if existeStop:
            self.ui.indicador_stop.setPixmap(QtGui.QPixmap.fromImage(qImg_stop))
            self.ui.indicador_stop.setVisible(True)
        else:
            self.ui.indicador_stop.setVisible(False)

        # Paso peatones
        senyalpeatones = self.senyalCebra
        height, width, channel = senyalpeatones.shape
        bytesPerLine = 3 * width
        qImg_peaton = QtGui.QImage(senyalpeatones.data, width, height,
                                 bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

        if pasoPeatones:
            self.ui.indicador_predicciones_2.setPixmap(QtGui.QPixmap.fromImage(qImg_peaton))
            self.ui.indicador_predicciones_2.setVisible(True)

        else:
            self.ui.indicador_predicciones_2.setVisible(False)



        # Volantes
        imgWheel = self.imgVolante
        height, width, channel = imgWheel.shape
        bytesPerLine = 3 * width

        #Real
        anguloVolante = -anguloVolante
        anguloSobre90_real = (anguloVolante*90)/0.7
        rotat_volante_real = imutils.rotate(imgWheel, anguloSobre90_real)
        qImg_Volante = QtGui.QImage(rotat_volante_real.data, width,
                                    height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.roadDirector_wheelImg_real.setPixmap(QtGui.QPixmap.fromImage(qImg_Volante))

        #RD
        anguloSobre90_predict = ((round(anguloVolante_predict,3) * 1.4)-0.7 ) *90.0/0.7
        
        rotat_volante_predict = imutils.rotate(imgWheel, anguloSobre90_predict)
        qImg_Volante = QtGui.QImage(rotat_volante_predict.data, width,
                                    height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.roadDirector_wheelImg_predicted.setPixmap(QtGui.QPixmap.fromImage(qImg_Volante))


        #Limite de velocidad
        if limiteVelocidad is None:
            
            limit30 = self.limite30
            height, width, channel = limit30.shape
            bytesPerLine = 3 * width
            qImg_lim30 = QtGui.QImage(limit30.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

            self.ui.indicador_limite.setPixmap(QtGui.QPixmap.fromImage(qImg_lim30))
            self.ui.indicador_limite.setDisabled(True)
        else:
            self.ui.indicador_limite.setDisabled(False)
            if limiteVelocidad == 30:
                limit30 = self.limite30
                height, width, channel = limit30.shape
                bytesPerLine = 3 * width
                qImg_lim30 = QtGui.QImage(limit30.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

                self.ui.indicador_limite.setPixmap(QtGui.QPixmap.fromImage(qImg_lim30))

            elif limiteVelocidad == 60:
                limit60 = self.limite60
                height, width, channel = limit60.shape
                bytesPerLine = 3 * width
                qImg_lim60 = QtGui.QImage(limit60.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
                self.ui.indicador_limite.setPixmap(QtGui.QPixmap.fromImage(qImg_lim60))

            elif limiteVelocidad == 90:
                limit90 = self.limite90
                height, width, channel = limit90.shape
                bytesPerLine = 3 * width
                qImg_lim90 = QtGui.QImage(limit90.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
                self.ui.indicador_limite.setPixmap(QtGui.QPixmap.fromImage(qImg_lim90))


        #Marcas calzada 


        recto = self.flechaRecto
        height, width, channel = recto.shape
        bytesPerLine = 3 * width
        qImg_recto = QtGui.QImage(recto.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.indicador_flecha_recto.setPixmap(QtGui.QPixmap.fromImage(qImg_recto))
        self.ui.indicador_flecha_recto.setDisabled(True)
        
        izq = self.flechaIzq
        height, width, channel = izq.shape
        bytesPerLine = 3 * width
        qImg_izq = QtGui.QImage(izq.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.indicador_flecha_izq.setPixmap(QtGui.QPixmap.fromImage(qImg_izq))
        self.ui.indicador_flecha_izq.setDisabled(True)

        der = self.flechaDer
        height, width, channel = der.shape
        bytesPerLine = 3 * width
        qImg_der = QtGui.QImage(der.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.indicador_flecha_der.setPixmap(QtGui.QPixmap.fromImage(qImg_der))
        self.ui.indicador_flecha_der.setDisabled(True)

        recDer = self.flechaRectoYDer
        height, width, channel = recDer.shape
        bytesPerLine = 3 * width
        qImg_derrec = QtGui.QImage(recDer.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.indicador_flecha_rectoYder.setPixmap(QtGui.QPixmap.fromImage(qImg_derrec))
        self.ui.indicador_flecha_rectoYder.setDisabled(True)


        recIzq = self.flechaRectoYIzq
        height, width, channel = recIzq.shape
        bytesPerLine = 3 * width
        qImg_izqrec = QtGui.QImage(recIzq.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.indicador_flecha_rectoYizq.setPixmap(QtGui.QPixmap.fromImage(qImg_izqrec))
        self.ui.indicador_flecha_rectoYizq.setDisabled(True)

        if senyalizquierda:
            self.ui.indicador_flecha_izq.setDisabled(False)
        if senyalderecha:
            self.ui.indicador_flecha_der.setDisabled(False)
        if senyaldelanteDer:
            self.ui.indicador_flecha_rectoYder.setDisabled(False)
        if senyaldelanteIzq:
            self.ui.indicador_flecha_rectoYizq.setDisabled(False)


        #Notificacion limite velocidad
        if porEncimalimiteVel:
            self.ui.notif_limiteVelocidad.setVisible(True)

        
        
        
        #Noficaciones
        if notificaConductorSinAtencion:
            self.ui.notif_conductorDistraido.setVisible(True)

        if notificaCambioSemaforoVerde:
            self.ui.notif_cambioSemaforo.setVisible(True)



        






    def cierraGui(self):
        print('Cerrando App')
        self.app.quit()

    def getImgBucleCV(self):
        return self.recordatorioCV


class pantallaCarga:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.interfazgrafica = QtWidgets.QMainWindow()
        self.ui = Ui_PantallaCargaTFG()
        self.ui.setupUi(self.interfazgrafica)
        #self.interfazgrafica.show()

    def cambiaProgresoLoading(self, num):
        self.ui.progressBar.value = num

    
    def cargaCompleta(self):
        print('Carga Completa. Cambiamos a la aplicacion principal')
        pass
        

class OverlaysOpenCV:

    def __init__(self):
        pass


    def overlayInfoMain(self, main, datos):
        res = main.copy()
        
        semaforos, paddingSemaf, vehiculosTrackeados, peatonesTrackeados, vehiculosLat1, vehiculosLat2 = datos

        #Semaforos
        for obj in semaforos:
            start_point_p = (int(obj.Left)-paddingSemaf,int(obj.Top)-paddingSemaf)
            end_point_p = (int(obj.Right)+paddingSemaf,int(obj.Bottom)+paddingSemaf)

            start_point = (int(obj.Left), int(obj.Top))
            end_point = (int(obj.Right), int(obj.Bottom))

            res = cv2.rectangle(res, start_point, end_point, (255, 255, 255), 1)
            res = cv2.rectangle(res, start_point_p, end_point_p, (255, 255, 255), 1)

            res = cv2.putText(res, f'S {obj.Confidence:.2f}% ', start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 255, 255), 1, cv2.LINE_AA)






        #Tracking de vehículos
        for obj in vehiculosTrackeados:
            start_point = (int(obj.getLeft_nv()), int(obj.getTop_nv()))
            end_point = (int(obj.getRight_nv()), int(obj.getBottom_nv()))

            aux2 = (int(obj.getRight_nv()), int(obj.getTop_nv()))
            aux3 = (int(obj.getLeft_nv()), int(obj.getBottom_nv()))

            centro = obj.getCentro()
            
            # pred -> Top Bot L R
            predict_start = (obj.getPrediccion()[2], obj.getPrediccion()[0])
            predict_end = (obj.getPrediccion()[3], obj.getPrediccion()[1])

            aux2_p = (int(obj.getPrediccion()[3]), int(obj.getPrediccion()[0]))
            aux3_p = (int(obj.getPrediccion()[2]), int(obj.getPrediccion()[1]))
            
            
            res = cv2.line(res, start_point, predict_start, (255,255,255), 1)
            res = cv2.line(res, end_point, predict_end, (255,255,255), 1)
            res = cv2.line(res, aux2, aux2_p, (255,255,255), 1)
            res = cv2.line(res, aux3, aux3_p, (255,255,255), 1)           
            
            res = cv2.rectangle(res, start_point, end_point, (0,0,255), 1) # Real
            res = cv2.rectangle(res, predict_start, predict_end, (0,255,0), 1) # Prediccion

            res = cv2.putText(res, f'V({obj.getClassID_nv()}) {obj.getConfidence_nv():.2f}% ID:{obj.getID()}',
                                    start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0,0,255), 1, cv2.LINE_AA)
            
            res = cv2.putText(res, f'PREDICT - {obj.getAcercandoseOalejandose()} - ID:{obj.getID()}', predict_start,
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1, cv2.LINE_AA) # Texto prediccion

            res = cv2.putText(res, f'{obj.getID()}',
                                    centro, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)




        #Tracking de personas
        for obj in peatonesTrackeados:
            start_point = (int(obj.getLeft_nv()), int(obj.getTop_nv()))
            end_point = (int(obj.getRight_nv()), int(obj.getBottom_nv()))

            aux2 = (int(obj.getRight_nv()), int(obj.getTop_nv()))
            aux3 = (int(obj.getLeft_nv()), int(obj.getBottom_nv()))

            centro = obj.getCentro()
            
            # pred -> Top Bot L R
            predict_start = (obj.getPrediccion()[2], obj.getPrediccion()[0])
            predict_end = (obj.getPrediccion()[3], obj.getPrediccion()[1])

            aux2_p = (int(obj.getPrediccion()[3]), int(obj.getPrediccion()[0]))
            aux3_p = (int(obj.getPrediccion()[2]), int(obj.getPrediccion()[1]))
            
            
            res = cv2.line(res, start_point, predict_start, (255,255,255), 1)
            res = cv2.line(res, end_point, predict_end, (255,255,255), 1)
            res = cv2.line(res, aux2, aux2_p, (255,255,255), 1)
            res = cv2.line(res, aux3, aux3_p, (255,255,255), 1)           
            
            res = cv2.rectangle(res, start_point, end_point, (255,0,0), 1) # Real
            res = cv2.rectangle(res, predict_start, predict_end, (255,255,255), 1) # Prediccion

            res = cv2.putText(res, f'V({obj.getClassID_nv()}) {obj.getConfidence_nv():.2f}% ID:{obj.getID()}',
                                    start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255,0,0), 1, cv2.LINE_AA)
            
            res = cv2.putText(res, f'PREDICT - ID:{obj.getID()}', predict_start,
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA) # Texto prediccion

            res = cv2.putText(res, f'{obj.getID()}',
                                    centro, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)    










        return res
        

    def overlayInfoSide1(self, lat1, datos):
        
        res = lat1.copy()
        semaforos, paddingSemaf, vehiculosTrackeados, peatonesTrackeados, vehiculosLat1, vehiculosLat2 = datos
        
        #Tracking de vehículos
        for obj in vehiculosLat1:
            start_point = (int(obj.getLeft_nv()), int(obj.getTop_nv()))
            end_point = (int(obj.getRight_nv()), int(obj.getBottom_nv()))

            aux2 = (int(obj.getRight_nv()), int(obj.getTop_nv()))
            aux3 = (int(obj.getLeft_nv()), int(obj.getBottom_nv()))

            centro = obj.getCentro()
            
                       
            res = cv2.rectangle(res, start_point, end_point, (0,0,255), 1) # Real

            res = cv2.putText(res, f'V({obj.getClassID_nv()}) {obj.getConfidence_nv():.2f}% ID:{obj.getID()}',
                                    start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0,0,255), 1, cv2.LINE_AA)

        return res


    def overlayInfoSide2(self, lat2, datos):
        res = lat2.copy()
        semaforos, paddingSemaf, vehiculosTrackeados, peatonesTrackeados, vehiculosLat1, vehiculosLat2 = datos
        
        #Tracking de vehículos
        for obj in vehiculosLat2:
            start_point = (int(obj.getLeft_nv()), int(obj.getTop_nv()))
            end_point = (int(obj.getRight_nv()), int(obj.getBottom_nv()))

            aux2 = (int(obj.getRight_nv()), int(obj.getTop_nv()))
            aux3 = (int(obj.getLeft_nv()), int(obj.getBottom_nv()))

            centro = obj.getCentro()
            
                       
            res = cv2.rectangle(res, start_point, end_point, (0,0,255), 1) # Real

            res = cv2.putText(res, f'V({obj.getClassID_nv()}) {obj.getConfidence_nv():.2f}% ID:{obj.getID()}',
                                    start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0,0,255), 1, cv2.LINE_AA)

        return res


    def overlay360view(self):
        pass


class notificacionesSonido:
    
    def __init__(self):
        
        self.sonido = None

        # Thread
        t = threading.Thread(target=self._reproduceSonidoSiHayCola)
        t.daemon = True
        t.start()
        
    def _reproduceSonidoSiHayCola(self):
        while True:
            if self.sonido is not None:
                print('Sonido!')
                os.system(f'mpv resources/quindarTones/{self.sonido}.ogg')
                self.sonido = None

            time.sleep(0.1)

    def reproduceAlertaQuindarStart(self):
        self.sonido = 'start'

    def reproduceAlertaQuindarEnd(self):
        self.sonido = 'end'
