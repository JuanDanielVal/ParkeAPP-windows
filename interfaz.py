
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> ICONO
import ctypes

myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

## ==> IMPORTACION MODULO CLASES
from clases import *

## ==> PANTALLA DE CARGA
from ui_splash_screen import Ui_SplashScreen

## ==> VENTANA PRINCIPAL
from mainwindow import Ui_MainWindow

## ==> GLOBALES
counter = 0

## ==> APLICACION
class MainWindow(QMainWindow):
    
    ## ==> Declaración de variables y objetos a usar
    bandera = ""
    
    #usuarios registrados
    persona1 = Usuarios("admin", "12345")
    persona2 = Usuarios("Inyer", "medina")
    persona3 = Usuarios("Juanda", "56789")
    persona4 = Usuarios("Felipe", "poo")
    
    #lista de usuarios
    lista_usuarios = [persona1, persona2, persona3, persona4]
    #lista de vehiculos
    lista_vehiculos = []
    
    #variables
    uso = 0
    disponibles = 50
    
    
    btndesign = ("background-color: rgba(24, 55, 79, 140);"
    "border: 3px solid rgba(0, 0, 0, 0);"
    "border-left-color: #fff;color: #fff;"
    "text-align: left;padding-left: 40px;"
    "font-family: Segoe UI, Helvetica, sans-serif;"
    "font-size: 15px;")
    btnd = ("QPushButton{"
	"background-color: transparent;"
    "color: #fff;"
    "text-align: left;"
    "padding-left: 40px;"
    "font-family: Segoe UI, Helvetica, sans-serif;"
    "font-size: 15px;}"

    "QPushButton:hover{"
	"background-color: rgba(38, 88, 128, 140);"
    "border: 0px;"
    "}")
    
    
    
    ## ==> CONSTRUCTOR DE CLASE MAINWINDOW
    def __init__(self):
        ## super()
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## remover barra
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ##titulo e icono de la app
        self.setWindowTitle("ParkeApp")
        self.setWindowIcon(QIcon("icono.ico"))
        
        ##declaración de métodos que usarán los botones
        self.ui.btnLogin.clicked.connect(self.login)
        self.ui.btnIngreso.clicked.connect(self.ingreso)
        self.ui.btnSalida.clicked.connect(self.salida)
        self.ui.btnAyuda.clicked.connect(self.ayuda)
        self.ui.btnVerautos.clicked.connect(self.verautos)
        self.ui.btnSalir.clicked.connect(self.cerrar)
        self.ui.btnSalir_2.clicked.connect(self.cerrar)
        self.ui.btnAceptarI.clicked.connect(self.aceptarI)
        self.ui.btnCancelarI.clicked.connect(lambda: self.ui.stackedWidget_2.hide())
        self.ui.btnMoto.clicked.connect(self.moto)
        self.ui.btnAuto.clicked.connect(self.auto)
        self.ui.btnAceptarS.clicked.connect(self.salida_auto)
        
        
        self.ui.wInfo.hide()
        
        ##tamaño máximo de los text edit
        self.ui.txtPlaca.setMaxLength(6)
        self.ui.txtPlaca_2.setMaxLength(6)
        
        self.ui.cbTipo_2.hide()
        
        self.ui.stackedWidget_2.hide()


    ## ==> ACCIÓN DEL BOTON LOGIN    
    def login(self):
        
        ##variables
        correcto = False
        
        ##se recorre la lista de usuarios para verificar si coincide lo que ingreso
        ##el usuario, con lo almacenado en la base de datos
        for numero in self.lista_usuarios:
            if numero.getUser() == self.ui.txtUser.text() and numero.getPass() == self.ui.txtPass.text():
                correcto = True
                break
        
        ##mensaje de error    
        if not correcto:
            QMessageBox.information(self, "Error", "Ha ingresado un usuario o contraseña incorrectos", QMessageBox.Ok)
            return
         
        ##mensaje de inicio se sesión correcto   
        else:
            QMessageBox.information(self, "Información", "Ha iniciado sesión correctamente", QMessageBox.Ok)
            
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            
    
    ## ==> ACCION DEL BOTON INGRESO         
    def ingreso(self):
        self.resetear()
        self.ui.btnIngreso.setStyleSheet(self.btndesign)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_9)
        self.ui.stackedWidget_2.show()
        
        
    ## ==> ACCION DEL BOTON SALIDA    
    def salida(self):
        self.resetear()
        self.ui.btnSalida.setStyleSheet(self.btndesign)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_10)
        self.ui.stackedWidget_2.show()

              
    ## ==> ACCION DEL BOTON AYUDA     
    def ayuda(self):
        self.resetear()
        self.ui.btnAyuda.setStyleSheet(self.btndesign)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_7)
        self.ui.stackedWidget_2.show()
    
    
    ## ==> ACCION DEL BOTON VER AUTOS    
    def verautos(self):
        self.resetear()
        self.ui.btnVerautos.setStyleSheet(self.btndesign)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)
        self.ui.stackedWidget_2.show()
    
    ## ==> RESETEO DE HOJAS DE ESTILO    
    def resetear(self):
        self.ui.btnVerautos.setStyleSheet(self.btnd)
        self.ui.btnIngreso.setStyleSheet(self.btnd)
        self.ui.btnSalida.setStyleSheet(self.btnd)
        self.ui.btnAyuda.setStyleSheet(self.btnd)
     
    ## ==> ACCION DEL BOTON CERRAR VENTANA   
    def cerrar(self):
        sys.exit(app.exec_())
    
    ## ==> ACCION DEL BOTON DE ACEPTAR EN LA PESTAÑA INGRESO     
    def aceptarI(self):
        
        ##validación de cupos disponibles
        if self.uso > 50:
            QMessageBox.information(self, "Error", "Ya no hay cupos disponibles", QMessageBox.Ok)
            return
        
        ##se obtiene la info de los text edit
        placa = self.ui.txtPlaca.text().lower()
        marca = self.ui.txtMarca.text().lower()
        color = self.ui.txtColor.text().lower()
        
        ##se recorre la lista de vehículos para verificar si la placa ingresada 
        ##está en la base de datos
        band = False
        for lista in self.lista_vehiculos:
            if lista.getPlaca() == placa:
                band = True
        
        ##mensaje de error        
        if band:
            QMessageBox.information(self, "Error", "El vehículo ya se encuentra en la base de datos", QMessageBox.Ok)
            return
        
        ##mensaje de error
        if placa == "" or marca == "" or color == "":
            QMessageBox.information(self, "Error", "Rellene todos los campos", QMessageBox.Ok)
            return
        
        ##se valida si la placa coincide con el formato exigido    
        c = [char for char in placa]  

        i = 0
        for n in c:
            
            if i>=3:
                if not n.isdigit():
                    QMessageBox.information(self, "Error", "Ingresó un formato invalido\nFormato exigido: XXX###", QMessageBox.Ok) 
                    return
            
            else:
                if not n.isalpha():
                    QMessageBox.information(self, "Error", "Ingresó un formato invalido\nFormato exigido: XXX###", QMessageBox.Ok)
                    return
                
            i += 1
                    
        
        ## ==> Instanciación de los objetos, seguidamente se almacenan en la lista de vehiculos
        ##caso motos
        if self.bandera == "moto":
            tipo = self.ui.cbTipo_2.currentText()
            if(tipo == "Alto cilindraje"):
                self.lista_vehiculos.append(Moto_AltoCC(placa, marca, color, tipo))
            else:
                self.lista_vehiculos.append(Moto_AltoCC(placa, marca, color, tipo))
                
        ## ==> Instanciación de los objetos, seguidamente se almacenan en la lista de vehiculos
        ##caso autos        
        else:
            tipo = self.ui.cbTipo.currentText()
            if(tipo == "Camioneta"):
                self.lista_vehiculos.append(Camioneta(placa, marca, color, tipo))
            elif(tipo == "Deportivo"):
                self.lista_vehiculos.append(Camioneta(placa, marca, color, tipo))
            elif(tipo == "Clasico"):
                self.lista_vehiculos.append(Camioneta(placa, marca, color, tipo))
        
                
        QMessageBox.information(self, "Información", "Vehículo ingresado con éxito", QMessageBox.Ok) 
        
        ##iteracion de variables globales
        self.disponibles = self.disponibles - 1
        self.uso = self.uso + 1
        
        ##actualización de datos
        self.ui.lblDisponibles.setText(("DISPONIBLES: <strong>{}</strong>").format(self.disponibles))
        self.ui.lblEnuso.setText(("EN USO: <strong>{}</strong>").format(self.uso))
        
        ## ==> Se agregan los attr del objeto a la tabla
        self.agregartbl(marca.upper(), placa.upper())
    
    ## ==> ACCION DEL BOTON MOTO    
    def moto(self):
        self.bandera = "moto"
        self.ui.cbTipo_2.show()
        self.ui.cbTipo.hide()
        self.ui.wInfo.show()
    
    ## ==> ACCION DEL BOTON AUTO     
    def auto(self):
        self.bandera = "auto"
        self.ui.cbTipo_2.hide()
        self.ui.cbTipo.show()
        self.ui.wInfo.show()
    
    ## ==> ACCION DEL BOTON ACEPTAR EN LA PESTAÑA DE SALIDA     
    def salida_auto(self):
        
        ##se obtiene la info de los text edit
        placa = self.ui.txtPlaca_2.text().lower()
        costo_ = self.ui.txtCosto.text().lower()
        
        ##validaciones
        if placa == "" or costo_ == "":
            QMessageBox.information(self, "Información", "Dejó algunos campos vacios", QMessageBox.Ok) 
            return
        
        costo = int(costo_)
        
        ##validación si no cuenta con tarjeta de propiedad
        if not self.ui.chbTarjeta.isChecked():
            QMessageBox.information(self, "Información", "Si no cuenta con una tarjeta de propiedad del vehiculo, no podrá salir", QMessageBox.Ok) 
            return
        
        ##se valida si la placa coincide con el formato exigido  
        c = [char for char in placa]  
        
        i = 0
        for n in c:
            
            if i>=3:
                if not n.isdigit():
                    QMessageBox.information(self, "Error", "Ingresó un formato invalido", QMessageBox.Ok) 
                    return
            
            else:
                if not n.isalpha():
                    QMessageBox.information(self, "Error", "Ingresó un formato invalido", QMessageBox.Ok)
                    return
                
            i += 1
        
        ##validación del costo menor a 0    
        if costo <= 0:
            QMessageBox.information(self, "Error", "Ingresó un valor menor que 0", QMessageBox.Ok)
            return
        
        
        ##se recorre la lista de vehiculos para ver si hay una coincidencia con la placa
        ##ingresada por el usuario
        bandera = False
        j = 0
        
        for lista in self.lista_vehiculos:
            if lista.getPlaca() == placa:
                bandera = True
                marca = lista.getMarca()
                self.lista_vehiculos.pop(j)
                
            j += 1
        
                
        if not bandera:
            QMessageBox.information(self, "Error", "El vehículo no se encuentra en la base de datos", QMessageBox.Ok)
            return
                

        QMessageBox.information(self, "Información", "El vehículo ha salido con éxito", QMessageBox.Ok)  
        
        ##iteración de variables globales   
        self.disponibles = self.disponibles + 1
        self.uso = self.uso - 1
        
        #actualización de datos
        self.ui.lblDisponibles.setText(("DISPONIBLES: <strong>{}</strong>").format(self.disponibles))
        self.ui.lblEnuso.setText(("EN USO: <strong>{}</strong>").format(self.uso))
        
        ## ==> Se elimina el objeto de la tabla
        self.eliminartbl(j)
    
    ## ==> MÉTODO PARA AGREGAR LOS ATRIBUTOS DE UN OBJETO A LA TABLA    
    def agregartbl(self, marca, placa):
        m = QTableWidgetItem(marca)
        p = QTableWidgetItem(placa)
        self.ui.tvVerautos.insertRow(self.uso-1)
        self.ui.tvVerautos.setItem(self.uso-1, 0, m)
        self.ui.tvVerautos.setItem(self.uso-1, 1, p)
    
    ## ==> MÉTODO PARA ELIMINAR LOS ATRIBUTOS DE UN OBJETO DE LA TABLA   
    def eliminartbl(self, indice):
        self.ui.tvVerautos.removeRow(indice-1)

        
    

# PANTALLA DE CARGA
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> CODIGO DE LA INTERFAZ
        ########################################################################
        
        ## TITULO
        self.setWindowTitle("ParkeApp")
        self.setWindowIcon(QIcon("icono.ico"))

        ## REMOVER BARRA DE VENTANA
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## EFECTO 
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> INICIO
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER EN MILISEGUNDOS
        self.timer.start(35)

        # CAMBIOS DE DESCRIPCION

        # Texto inicial
        self.ui.label_description.setText("<strong>BIENVENIDOS</strong> A PARKE<strong>APP</strong>")

        # Texto una vez cambiado 
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>CARGANDO</strong> BASES DE DATOS"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>CARGANDO</strong> INTERFAZ"))


        ## MOSTRAR ==> VENTANA PRINCIPAL
        ########################################################################
        self.show()
        ## ==> FIN ##

    ## ==> FUNCIONES DE LA PANTALLA DE CARGA
    ########################################################################
    def progress(self):

        # SE HACE USO DE LA VARIABLE GLOBAL COUNTER
        global counter

        #  PONER UN VALOR PREDETERMINADO A LA BARRA DE PROGRESO
        self.ui.progressBar.setValue(counter)

        # VALIDACION CUANDO LA BARRA DE CARGA LLEGA AL 100
        if counter > 100:
            # PARAR TIMER
            self.timer.stop()

            # MOSTRAR LA VENTANA PRINCIPAL
            self.main = MainWindow()
            self.main.show()

            # SE CIERRAR EL WIDGET DE LA PANTALLA DE CARGA
            self.close()

        # SE INCREMENTA EL CONTADOR
        counter += 1



## ==> MAIN
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
