# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainxMNKqy.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 458)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 641, 461))
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QWidget#page{\n"
"background-image: url(\"fondo.png\");\n"
"}")
        self.fmLogin = QFrame(self.page)
        self.fmLogin.setObjectName(u"fmLogin")
        self.fmLogin.setEnabled(True)
        self.fmLogin.setGeometry(QRect(20, 20, 300, 430))
        self.fmLogin.setMouseTracking(False)
        self.fmLogin.setFocusPolicy(Qt.NoFocus)
        self.fmLogin.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.fmLogin.setAcceptDrops(False)
        self.fmLogin.setStyleSheet(u"QFrame#fmLogin{\n"
"	background-color: rgba(19, 28, 41, 100);\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.btnLogin = QPushButton(self.fmLogin)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(20, 350, 261, 41))
        font = QFont()
        font.setBold(True)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet(u"QPushButton{\n"
"color: #fff;\n"
"background-color: #132d42; \n"
"border-radius: 7px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: #265880; \n"
"}")
        self.txtUser = QLineEdit(self.fmLogin)
        self.txtUser.setObjectName(u"txtUser")
        self.txtUser.setGeometry(QRect(10, 210, 281, 31))
        font1 = QFont()
        font1.setPointSize(13)
        self.txtUser.setFont(font1)
        self.txtUser.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.txtUser.setFrame(True)
        self.txtPass = QLineEdit(self.fmLogin)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(10, 270, 281, 31))
        self.txtPass.setFont(font1)
        self.txtPass.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.pushButton_3 = QPushButton(self.fmLogin)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 30, 301, 151))
        self.pushButton_3.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u"login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(120, 120))
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(380, 120, 211, 181))
        self.frame_2.setStyleSheet(u"QFrame#frame_2{\n"
"background-image: url(\"parkeapp.png\");\n"
"border: 0px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btnSalir_2 = QPushButton(self.page)
        self.btnSalir_2.setObjectName(u"btnSalir_2")
        self.btnSalir_2.setGeometry(QRect(610, 0, 31, 24))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.btnSalir_2.setFont(font2)
        self.btnSalir_2.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"color: white;\n"
"padding-bottom: 5px;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 0, 0, 120);\n"
"color: white;\n"
"}")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QWidget#page_2{\n"
"background-image: url(\"fond.png\");\n"
"}")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 221, 431))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: rgba(19, 28, 41, 100);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnIngreso = QPushButton(self.frame)
        self.btnIngreso.setObjectName(u"btnIngreso")
        self.btnIngreso.setGeometry(QRect(0, 110, 221, 51))
        self.btnIngreso.setFont(font)
        self.btnIngreso.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnIngreso.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"color: #fff;\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(38, 88, 128, 140);\n"
"border: 0px;\n"
"}\n"
"")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 131, 81))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: #fff;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 10, 131, 81))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: #fff;")
        self.btnSalida = QPushButton(self.frame)
        self.btnSalida.setObjectName(u"btnSalida")
        self.btnSalida.setGeometry(QRect(0, 160, 221, 51))
        self.btnSalida.setFont(font)
        self.btnSalida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSalida.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"color: #fff;\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(38, 88, 128, 140);\n"
"border: 0px;\n"
"}\n"
"\n"
"")
        self.btnAyuda = QPushButton(self.frame)
        self.btnAyuda.setObjectName(u"btnAyuda")
        self.btnAyuda.setGeometry(QRect(0, 260, 221, 51))
        self.btnAyuda.setFont(font)
        self.btnAyuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAyuda.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"color: #fff;\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(38, 88, 128, 140);\n"
"border: 0px;\n"
"}\n"
"")
        self.lbCapacidad = QLabel(self.frame)
        self.lbCapacidad.setObjectName(u"lbCapacidad")
        self.lbCapacidad.setGeometry(QRect(10, 360, 201, 16))
        font5 = QFont()
        font5.setPointSize(10)
        self.lbCapacidad.setFont(font5)
        self.lbCapacidad.setStyleSheet(u"color: #fff;")
        self.lblEnuso = QLabel(self.frame)
        self.lblEnuso.setObjectName(u"lblEnuso")
        self.lblEnuso.setGeometry(QRect(10, 380, 201, 16))
        self.lblEnuso.setFont(font5)
        self.lblEnuso.setStyleSheet(u"color: #fff;")
        self.lblDisponibles = QLabel(self.frame)
        self.lblDisponibles.setObjectName(u"lblDisponibles")
        self.lblDisponibles.setGeometry(QRect(10, 400, 201, 16))
        self.lblDisponibles.setFont(font5)
        self.lblDisponibles.setStyleSheet(u"color: #fff;")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 30, 51, 41))
        self.pushButton.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u"carwhite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(40, 50))
        self.btnVerautos = QPushButton(self.frame)
        self.btnVerautos.setObjectName(u"btnVerautos")
        self.btnVerautos.setGeometry(QRect(0, 210, 221, 51))
        self.btnVerautos.setFont(font)
        self.btnVerautos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVerautos.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"color: #fff;\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(38, 88, 128, 140);\n"
"border: 0px;\n"
"}\n"
"\n"
"")
        self.btnSalir = QPushButton(self.page_2)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(610, 0, 31, 24))
        self.btnSalir.setFont(font2)
        self.btnSalir.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"color: white;\n"
"padding-bottom: 5px;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 0, 0, 120);\n"
"color: white;\n"
"}")
        self.stackedWidget_2 = QStackedWidget(self.page_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(270, 20, 361, 431))
        self.stackedWidget_2.setStyleSheet(u"")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setStyleSheet(u"QWidget#page_9{\n"
"	background-color: rgba(19, 28, 41, 100);\n"
"	border-radius: 10px;\n"
"}")
        self.btnAuto = QPushButton(self.page_9)
        self.btnAuto.setObjectName(u"btnAuto")
        self.btnAuto.setGeometry(QRect(190, 100, 121, 31))
        self.btnAuto.setFont(font)
        self.btnAuto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAuto.setStyleSheet(u"QPushButton{\n"
"color: #fff;\n"
"background-color: #132d42; \n"
"border-radius: 7px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #265880; \n"
"}")
        self.btnMoto = QPushButton(self.page_9)
        self.btnMoto.setObjectName(u"btnMoto")
        self.btnMoto.setGeometry(QRect(50, 100, 121, 31))
        self.btnMoto.setFont(font)
        self.btnMoto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMoto.setStyleSheet(u"QPushButton{\n"
"color: #fff;\n"
"background-color: #132d42; \n"
"border-radius: 7px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #265880; \n"
"}")
        self.label_6 = QLabel(self.page_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 20, 361, 31))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: #fff;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 24px;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.wInfo = QWidget(self.page_9)
        self.wInfo.setObjectName(u"wInfo")
        self.wInfo.setGeometry(QRect(20, 160, 321, 251))
        self.txtPlaca = QLineEdit(self.wInfo)
        self.txtPlaca.setObjectName(u"txtPlaca")
        self.txtPlaca.setGeometry(QRect(10, 20, 151, 31))
        self.txtPlaca.setFont(font1)
        self.txtPlaca.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.txtPlaca.setFrame(True)
        self.txtMarca = QLineEdit(self.wInfo)
        self.txtMarca.setObjectName(u"txtMarca")
        self.txtMarca.setGeometry(QRect(10, 80, 151, 31))
        self.txtMarca.setFont(font1)
        self.txtMarca.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.txtMarca.setInputMethodHints(Qt.ImhNone)
        self.txtMarca.setFrame(True)
        self.txtColor = QLineEdit(self.wInfo)
        self.txtColor.setObjectName(u"txtColor")
        self.txtColor.setGeometry(QRect(10, 140, 151, 31))
        self.txtColor.setFont(font1)
        self.txtColor.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.txtColor.setFrame(True)
        self.cbTipo_2 = QComboBox(self.wInfo)
        self.cbTipo_2.addItem("")
        self.cbTipo_2.addItem("")
        self.cbTipo_2.setObjectName(u"cbTipo_2")
        self.cbTipo_2.setGeometry(QRect(10, 200, 151, 31))
        self.cbTipo_2.setFont(font1)
        self.cbTipo_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.btnCancelarI = QPushButton(self.wInfo)
        self.btnCancelarI.setObjectName(u"btnCancelarI")
        self.btnCancelarI.setGeometry(QRect(200, 130, 111, 31))
        self.btnCancelarI.setFont(font)
        self.btnCancelarI.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancelarI.setStyleSheet(u"QPushButton{\n"
"color: #fff;\n"
"background-color: #132d42; \n"
"border-radius: 7px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #265880; \n"
"}")
        self.btnAceptarI = QPushButton(self.wInfo)
        self.btnAceptarI.setObjectName(u"btnAceptarI")
        self.btnAceptarI.setGeometry(QRect(200, 80, 111, 31))
        self.btnAceptarI.setFont(font)
        self.btnAceptarI.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAceptarI.setStyleSheet(u"QPushButton{\n"
"color: #fff;\n"
"background-color: #132d42; \n"
"border-radius: 7px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #265880; \n"
"}")
        self.cbTipo = QComboBox(self.wInfo)
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(10, 200, 151, 31))
        self.cbTipo.setFont(font1)
        self.cbTipo.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"QWidget#page_5{\n"
"	background-color: rgba(19, 28, 41, 100);\n"
"	border-radius: 10px;\n"
"}")
        self.label_7 = QLabel(self.page_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 20, 361, 31))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: #fff;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 24px;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.tvVerautos = QTableWidget(self.page_5)
        if (self.tvVerautos.columnCount() < 2):
            self.tvVerautos.setColumnCount(2)
        font6 = QFont()
        font6.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font6);
        self.tvVerautos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tvVerautos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tvVerautos.setObjectName(u"tvVerautos")
        self.tvVerautos.setGeometry(QRect(10, 90, 341, 331))
        self.tvVerautos.setStyleSheet(u"QTableView#tvVerautos{\n"
"color: #fff;\n"
"	background-color: rgba(124, 124, 124, 150);\n"
"border-radius: 7px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 10px;\n"
"text-align: left;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"color: #fff;\n"
"background-color: rgba(124, 124, 124, 150);\n"
"border: 1px solid rgba(124, 124, 124, 150);\n"
"border-right-color: #fff;\n"
"\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"background-color: transparent;\n"
"border-color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover{\n"
"background-color: rgba(38, 88, 128, 100);\n"
"}\n"
"\n"
"\n"
"")
        self.tvVerautos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tvVerautos.setColumnCount(2)
        self.tvVerautos.horizontalHeader().setMinimumSectionSize(39)
        self.tvVerautos.horizontalHeader().setDefaultSectionSize(171)
        self.tvVerautos.verticalHeader().setVisible(False)
        self.tvVerautos.verticalHeader().setCascadingSectionResizes(False)
        self.tvVerautos.verticalHeader().setDefaultSectionSize(28)
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.page_10.setStyleSheet(u"QWidget#page_10{\n"
"	background-color: rgba(19, 28, 41, 100);\n"
"	border-radius: 10px;\n"
"}")
        self.chbTarjeta = QCheckBox(self.page_10)
        self.chbTarjeta.setObjectName(u"chbTarjeta")
        self.chbTarjeta.setGeometry(QRect(90, 110, 181, 31))
        self.chbTarjeta.setFont(font1)
        self.chbTarjeta.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.label_5 = QLabel(self.page_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 20, 361, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #fff;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 24px;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.txtPlaca_2 = QLineEdit(self.page_10)
        self.txtPlaca_2.setObjectName(u"txtPlaca_2")
        self.txtPlaca_2.setGeometry(QRect(90, 180, 181, 31))
        self.txtPlaca_2.setFont(font1)
        self.txtPlaca_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.txtPlaca_2.setFrame(True)
        self.txtCosto = QLineEdit(self.page_10)
        self.txtCosto.setObjectName(u"txtCosto")
        self.txtCosto.setGeometry(QRect(90, 250, 181, 31))
        self.txtCosto.setFont(font1)
        self.txtCosto.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(143, 143, 143);\n"
"color: rgb(208, 208, 208);\n"
"padding-bottom: 4px;\n"
"padding-left: 3px")
        self.txtCosto.setFrame(True)
        self.btnAceptarS = QPushButton(self.page_10)
        self.btnAceptarS.setObjectName(u"btnAceptarS")
        self.btnAceptarS.setGeometry(QRect(120, 320, 121, 31))
        self.btnAceptarS.setFont(font)
        self.btnAceptarS.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAceptarS.setStyleSheet(u"QPushButton{\n"
"color: #fff;\n"
"background-color: #132d42; \n"
"border-radius: 7px;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #265880; \n"
"}")
        self.stackedWidget_2.addWidget(self.page_10)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setStyleSheet(u"QWidget#page_7{\n"
"	background-color: rgba(19, 28, 41, 100);\n"
"	border-radius: 10px;\n"
"}")
        self.pushButton_2 = QPushButton(self.page_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 360, 361, 81))
        self.pushButton_2.setStyleSheet(u"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u"Logo_U.T.P..png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(60, 100))
        self.pushButton_4 = QPushButton(self.page_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 20, 321, 411))
        self.pushButton_4.setStyleSheet(u"background-color: transparent;")
        icon3 = QIcon()
        icon3.addFile(u"textAbout.fw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(300, 300))
        self.label_8 = QLabel(self.page_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 20, 361, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: #fff;\n"
"font-family: Segoe UI, Helvetica, sans-serif;\n"
"font-size: 24px;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.page_7)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"INICIAR SESI\u00d3N", None))
        self.txtUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.txtPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton_3.setText("")
        self.btnSalir_2.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.btnIngreso.setText(QCoreApplication.translate("MainWindow", u"INGRESO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PARKE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"APP", None))
        self.btnSalida.setText(QCoreApplication.translate("MainWindow", u"SALIDA", None))
        self.btnAyuda.setText(QCoreApplication.translate("MainWindow", u"AYUDA", None))
        self.lbCapacidad.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>CAPACIDAD: <span style=\" font-weight:700;\">50</span></p></body></html>", None))
        self.lblEnuso.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>EN USO: <span style=\" font-weight:700;\">0</span></p></body></html>", None))
        self.lblDisponibles.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>DISPONIBLES: <span style=\" font-weight:700;\">50</span></p></body></html>", None))
        self.pushButton.setText("")
        self.btnVerautos.setText(QCoreApplication.translate("MainWindow", u"VER AUTOS", None))
        self.btnSalir.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.btnAuto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.btnMoto.setText(QCoreApplication.translate("MainWindow", u"MOTO", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"INGRESO", None))
        self.txtPlaca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placa", None))
        self.txtMarca.setText("")
        self.txtMarca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.txtColor.setText("")
        self.txtColor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.cbTipo_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Alto cilindraje", None))
        self.cbTipo_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Bajo Cilindraje", None))

        self.cbTipo_2.setPlaceholderText("")
        self.btnCancelarI.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.btnAceptarI.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.cbTipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Camioneta", None))
        self.cbTipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Deportivo", None))
        self.cbTipo.setItemText(2, QCoreApplication.translate("MainWindow", u"Cl\u00e1sico", None))

        self.cbTipo.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"VER AUTOS", None))
        ___qtablewidgetitem = self.tvVerautos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Vehiculo", None));
        ___qtablewidgetitem1 = self.tvVerautos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Placa", None));
        self.chbTarjeta.setText(QCoreApplication.translate("MainWindow", u"Tarjeta de propiedad", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SALIDA", None))
        self.txtPlaca_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placa", None))
        self.txtCosto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Costo", None))
        self.btnAceptarS.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.pushButton_2.setText("")
        self.pushButton_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ACERCA DE", None))
    # retranslateUi

