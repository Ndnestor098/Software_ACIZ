#librerias Usadas
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import os
import time
import datetime
from datetime import date, datetime
import sqlite3 as sql
import cv2
import yagmail
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yagmail
import imutils
from tkinter import filedialog
from os import scandir
import random



#---------------------------------------------Iniciar Sesion-----------------------------------------------------------------
class Sension():
	def __init__(self):
		#------------Ubicacion de Base de Dato------------
		self.__Data_Base = f'{os.getcwd()}/BD/Datos_General.db'

#----------------------------------------Configuracion de Ventana------------------------------------------------------------
		self.root = Tk()
		self.root.iconbitmap(f'{os.getcwd()}/Imagenes/Icono.ico')
		self.root.title("Sysors")
		self.root.resizable(0,0)

		#Toma de Datos de la Ventana
		wtotal = self.root.winfo_screenwidth()
		htotal = self.root.winfo_screenheight()
		wventana = 400
		hventana = 512

		#Formula para el Calculo de la Ventana
		pwidth = round(wtotal/2-wventana/2)
		pheight = round(htotal/2-hventana/2)

		#Geometría de la Ventana
		self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

#-----------------------------------------------Imagenes---------------------------------------------------------------------
		
		self.Image_Avatar = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\Avatar.png".format(os.getcwd())).resize((115,170)))
		self.Image_Boton = ImageTk.PhotoImage(Image.open(r"{}\Imagen\login.png".format(os.getcwd())).resize((160,150)))
		self.Image_L = ImageTk.PhotoImage(Image.open(r"{}\Imagen\lock.png".format(os.getcwd())).resize((46,39)))
		self.Image_U = ImageTk.PhotoImage(Image.open(r"{}\Imagen\user.png".format(os.getcwd())).resize((35,35)))
		self.Image_back = ImageTk.PhotoImage(Image.open(r"{}\Imagen\back.png".format(os.getcwd())).resize((35,35)))
		self.Image_sign = ImageTk.PhotoImage(Image.open(r"{}\Imagen\sign.png".format(os.getcwd())).resize((160,65)))
		self.Image_Gmail = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\gmail.png".format(os.getcwd())).resize((35,35)))
		self.Siguiente = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\Boton_siguiente.png".format(os.getcwd())).resize((60,25)))



		self.Iniciar()

		self.root.mainloop()

#-----------------------------------------Configuracion de Frames------------------------------------------------------------
	def Iniciar(self):
		#Destruir Frames para no sobrecargar el sistema 
		try:
			self.frame_Regis.destroy()
			self.frame_forget.destroy()
		except:
			pass
		
		#-----------Frame de inicio---------------------
		self.frame_init = Frame(self.root, bg='white')
		self.frame_init.place(x=0, y=0, width=400, height=512)

		#-----------Orden de imagenes-------------------
		Label(self.frame_init, image=self.Image_Avatar, background='white').place(x=150, y=30)

		#-----------------Titulo-------------------------
		Label(self.frame_init, bg='white', text='Iniciar Sesión', font=('Arial', 20, 'bold')).place(x=114, y=185)
		
		
		#-------------Entrada de Usuario-----------------
		self.Entry_User = Entry(self.frame_init, relief=FLAT, bd=1, bg='#d7e1e2', font=('Arial', 10, 'bold'), fg='black')
		self.Entry_User.place(x=120, y=238, height=38, width=173)
		self.Entry_User.focus() #Inicializar escritura
		self.Entry_User.bind("<Return>", lambda _: self.Entry_Key.focus()) #Al dar Enter pasa a la Entrada "Entry_Key"
		Label(self.frame_init, image=self.Image_U, bg='white').place(x=75, y=238) #Imagen de Usuario

		#-------------Entrada de clave-------------------
		self.Entry_Key = Entry(self.frame_init, relief=FLAT, bd=1, bg='#d7e1e2', font=('Arial', 14, 'bold'), fg='black')
		self.Entry_Key.place(x=120, y=319, height=38, width=173)
		self.Entry_Key.config(show='*') # Ocultar clave
		self.Entry_Key.bind("<Return>", lambda _: self.Check()) #Al dar Enter pasa a la Entrada "Logueo"
		Label(self.frame_init, image=self.Image_L, bg='white').place(x=70, y=319) #Imagen de Usuario
		
		#-------------Mensaje de Error------------------- 
		self.Error_Incio = Label(self.frame_init, bg='white', text='', font=('Arial', 12, 'bold'), fg='red')
		self.Error_Incio.place(x=102, y=362)
		
		#-------------Boton de Inicio--------------------
		Button(self.frame_init, relief=FLAT, image=self.Image_Boton, bd=0, command=self.Check , height=60, bg='white').place(x=125, y=400)
		
		#-------------Boton Registrarce------------------
		Button(self.frame_init, text='Registrate', fg='black', relief=FLAT, bd=0, bg='white', font=('Arial', 9, 'bold'), command=self.Sign_Up).place(x=107, y=485)
		Label(self.frame_init, text='¿No tienes cuenta?', bg='white').place(x=5,y=485)
		
		#-------------Olvidaste la Clave-----------------
		Button(self.frame_init, text='¿Olvidaste la clave?', fg='black', relief=FLAT, bd=0, bg='white', font=('Arial', 9, 'bold'), command=self.Entry_Code).place(x=270, y=485)

#--------------------------------------------Checkin de Inicio---------------------------------------------------------------
	def Check(self):
		#Usuario
		R_1 = self.Exit_Data(self.Entry_User.get(), self.Entry_Key.get())
		
		usuario = self.Entry_User.get()

		#Check Usuario
		if R_1 == True:
			self.root.destroy()
			ACIZ(self.ID, usuario)
			self.Close_Data()
				
		
		else:
			self.Error_Incio['text'] = 'Usuario o Clave incorrecta'
			self.Close_Data()

#--------------------------------------------Registrar Usuario---------------------------------------------------------------
	def Sign_Up(self):
		#-----Destruccion de Widget--------
		self.frame_init.destroy()
		self.root.update()

		#-----------Frame de inicio---------------------
		self.frame_Regis = Frame(self.root, bg='white')
		self.frame_Regis.place(x=0, y=0, width=400, height=512)

		#--------------Mensaje--------------------------
		Label(self.frame_Regis, text='Regitrar', bg='white', font=('Arial', 20, 'bold')).place(x=140, y=20)
		Label(self.frame_Regis, text='Los envios de correos podria llegar en bandeja de Spam', bg='white', font=('Arial', 9, 'bold')).place(x=36, y=490)

		
		#----------Mensajes de Errores------------------
		self.Error_User = Label(self.frame_Regis, text='', bg='white', font=('Arial', 9, 'bold'), fg='red')
		self.Error_User.place(x=120, y=120) #Error de no introducir nombre de usuario

		self.Error_clave = Label(self.frame_Regis, text='', bg='white', font=('Arial', 9, 'bold'), fg='red')
		self.Error_clave.place(x=140, y=258) #Error de no introducir o no coinciden claves

		self.Error_Question = Label(self.frame_Regis, text='', bg='white', font=('Arial', 9, 'bold'), fg='red')
		self.Error_Question.place(x=140, y=338) #Error de no introducir nombre de Mascotas

		#------------Boton de Regresar-----------------
		self.back = Button(self.frame_Regis, image=self.Image_back, bg='white', bd=0, command=self.Iniciar)
		self.back.place(x=10, y=10)
		
		#------Entrada de Registro de Usuario----------
		self.Entry_User_R = Entry(self.frame_Regis, relief=FLAT, bd=1, bg='#d7e1e2', font=('Arial', 12, 'bold'), fg='black')
		self.Entry_User_R.place(x=105, y=80, height=38, width=200)
		self.Entry_User_R.focus()
		self.Entry_User_R.bind("<Return>", lambda _: self.Entry_Key_R.focus()) #Al dar Enter pasa a la Entrada "Entry_Key_R"
		Label(self.frame_Regis, image=self.Image_U, bg='white').place(x=60, y=80) #Imagen de Usuario

		#--------Entrada de clave de Usuario-----------
		self.Entry_Key_R = Entry(self.frame_Regis, relief=FLAT, bd=1, bg='#d7e1e2', font=('Arial', 12, 'bold'), fg='black')
		self.Entry_Key_R.place(x=105, y=150, height=38, width=200)
		self.Entry_Key_R.bind("<Return>", lambda _: self.Entry_Key_C.focus()) #Al dar Enter pasa a la Entrada "Entry_Key_C"
		Label(self.frame_Regis, image=self.Image_L, bg='white').place(x=53, y=150) #Imagen de Candado

		#------Entrada de confirmacion de clave--------
		self.Entry_Key_C = Entry(self.frame_Regis, relief=FLAT, bd=1, bg='#d7e1e2', font=('Arial', 12, 'bold'), fg='black')
		self.Entry_Key_C.place(x=105, y=220, height=38, width=200)
		self.Entry_Key_C.bind("<Return>", lambda _: self.Entry_Gmail.focus()) #Al dar Enter pasa a la Entrada "Entry_Gmail"
		Label(self.frame_Regis, image=self.Image_L, bg='white').place(x=53, y=220) #Imagen de Candado

		#----------Entrada de pregunta clave-----------
		self.Entry_Gmail = Entry(self.frame_Regis, relief=FLAT, bd=1, bg='#d7e1e2', font=('Arial', 12, 'bold'), fg='black')
		self.Entry_Gmail.place(x=105, y=290, height=38, width=200)
		self.Entry_Gmail.bind("<Return>", lambda _: self.Confirm_C()) #Al dar Enter llama a la Funcion "Confirm_C"
		Label(self.frame_Regis, image=self.Image_Gmail, bg='white').place(x=60, y=290) #Imagen de Pregunta

		#--------------Boton de Registrar--------------
		self.Boton_Register = Button(self.frame_Regis, relief=FLAT, image=self.Image_sign, bd=0 , bg='white', command=self.Confirm_C)
		self.Boton_Register.place(x=120, y=378)

#------------------------------------Frame del chequeo del codigo enviado----------------------------------------------------
	def Entry_Code(self):
		#-------Desactivar Entradas de Registro--------
		self.Entry_User_R.config(state='disabled')
		self.Entry_Key_R.config(state='disabled')
		self.Entry_Key_C.config(state='disabled')
		self.Entry_Gmail.config(state='disabled')
		self.Boton_Register.config(state='disabled')
		self.back.config(state='disabled')

		#----------Frame de Entrada Codigo-------------
		self.Frame_code = Frame(self.frame_Regis, background='#d7d7d7')
		self.Frame_code.place(x=75, y=150, height=110, width=250)

		#-------------------Titulo---------------------
		Label(self.Frame_code, text='Ingresa el Codigo', font=('Arial', 11, 'bold'), background='#d7d7d7').place(x=57, y=5)

		#-------------Entrada del Codigo---------------
		Code = Entry(self.Frame_code, font=('Arial', 20, 'bold'))
		Code.place(x=70,y=40, height=30, width=100)
		Code.focus()
		Code.bind("<Return>", lambda _: self.Validacion_Gmail(2,Code.get()))

		#--------------Boton de Chequeo----------------
		Button(self.Frame_code, image=self.Siguiente, relief=FLAT, background='#d7d7d7', command=lambda:self.Validacion_Gmail(2,Code.get())).place(x=88, y=80)

		#--------------------Marco--------------------
		Label(self.Frame_code, bg='black').place(x=0,y=0,height=110,width=1)
		Label(self.Frame_code, bg='black').place(x=0,y=0,height=1,width=250)
		Label(self.Frame_code, bg='black').place(x=0,y=109,height=1,width=250)
		Label(self.Frame_code, bg='black').place(x=249,y=0,height=110,width=1)
		
#-------------------------------Algoritmo de confirmacion de usuario y clave-------------------------------------------------
	#Confirmar la existencia de datos en la entradas
	def Confirm_C(self):
		#Borrar Datos escritos en caso de fallo del usuario
		self.Error_Question['text'] = ''
		self.Error_clave['text'] = ''
		self.Error_User['text'] = ''


		#Confirmar la existencia del usuario
		if self.Exit_Data_2(self.Entry_User_R.get()): #Resivimos aviso de la funcion de la base de datos
			self.Error_User['text'] = 'El usuario ingresado existe'
		else:
			self.Close_Data()


			#iniciar confirmaciones 
			if len(self.Entry_User_R.get()) != 0: #Comprobar si esta vacia la casilla de usuario 
				
				if self.Entry_Key_C.get() == self.Entry_Key_R.get(): #Comprobar si las claves son iguales
					
					if len(self.Entry_Key_C.get()) >= 8: #Comprobar si tiene los 8 caracteres minimos
						self.Validacion_Clave()
						
							
					else:#No se cumplio los 8  caracteres minimos
						self.Error_clave['text'] = 'Minimo 8 Caracteres'

				else: #Claves no coinciden 
					self.Error_clave['text'] = 'Claves no coinciden'
			
			else: #Esta vacia la casilla de usuario 
				self.Error_User['text'] = 'No se ha ingresado usuario'
			
	#Validacion de clave segun los requisitos 
	def Validacion_Clave(self):
		Clave = []

		for x in self.Entry_Key_R.get():
			Clave.append(x)



		May = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
		Num = '1234567890'

		Ap_M = False
		Ap_N = False

		for x in range(len(Clave)):
			
			for i in May:
				if Clave[x] == i:
					Ap_M = True

			for e in Num:
				if Clave[x] == e:
					Ap_N = True

		#Envio de Datos
		if Ap_M == True or Ap_N == True: #Confirmar si la clave tiene Mayusculas o numeros
			
			if len(self.Entry_Gmail.get()) != 0: #Comprobar si la casilla pregunta esta vacia 
				self.Validacion_Gmail(1,'null')	
				
	

			else: #Casilla de preguntas vacia
				self.Error_Question['text'] = 'Introducir Correo'
			

		else: #Faltan Mayusculas o Numeros
			self.Error_clave['text'] = 'Falta May. o Numeros'

	#Envio de codigo para validar el Email
	def Validacion_Gmail(self, select, code):
		if select == 1:
			Clave_Gmail = 'vzgmvlblnnonwodh'
			Emisor = 'ndsmartscompany@gmail.com'
			Asunto = 'Clave de confimacion de cuenta ACIZ'

			if int(time.strftime('%H')) < 12 and int(time.strftime('%H')) >= 6:
				saludo = 'dias'
			
			elif int(time.strftime('%H')) >= 12 and int(time.strftime('%H')) < 19:
				saludo = 'tardes'

			elif int(time.strftime('%H')) >= 19:
				saludo = 'noches'

			else:
				saludo = 'noches'


			self.codigo = str()

			for x in range(6):
				self.codigo += str(random.randint(0,9))
		

			cuerpo = f"""
				Buenas {saludo} Estimado {self.Entry_User_R.get()}, ACIZ ha recibido una solicitud para usar
				{self.Entry_Gmail.get()} como direccion de correo electronico para una cuenta de ACIZ.

				Utiliza este codigo para terminar de configurar esta direccion de correo electronico en su
				cuenta de ACIZ:
										
							{self.codigo}

				El codigo deja de ser valido en el momento que cierra el programa ACIZ.

				Si no reconoces estas acciones, puedes ignorar el mensaje 
			
			"""

			yag = yagmail.SMTP(user=Emisor, password=Clave_Gmail)
			yag.send(self.Entry_Gmail.get(),Asunto,cuerpo)

			self.Entry_Code()
		
		else:
			if self.codigo == code:
				self.Save_Data()
				self.Close_Data()
				Craecion(self.Entry_User_R.get())

				self.frame_Regis.destroy()
				self.Frame_code.destroy()
				
				self.Iniciar()

#---------------------------------------------Olvido de clave----------------------------------------------------------------
	def Forget_key(self):
		#-------Frame de Olvido----------
		self.frame_forget = Frame(self.root, bg='white')
		self.frame_forget.place(x=0, y=0, width=400, height=512)

		#--------Boton de Regresar---------
		Button(self.frame_forget, image=self.Image_back, bg='white', bd=0, command=self.Iniciar).place(x=10, y=10)

#----------------------------------------------Base de Dato------------------------------------------------------------------
	#-------------Entrada de la Base de Dato--------------
	def Save_Data(self):
		self.conn = sql.connect(self.__Data_Base)

		cursor = self.conn.cursor()

		cursor.execute(f"""INSERT INTO Usuarios (Nombre, Clave, Email, Registro, DB) VALUES ('{self.Entry_User_R.get()}','{self.Entry_Key_R.get()}','{self.Entry_Gmail.get()}',TRUE, TRUE);""")

		self.conn.commit()
		
	#-------------Salida de la Base de Dato--------------
	def Exit_Data(self, Usuario, Key):

		self.conn = sql.connect(self.__Data_Base)		

		cursor = self.conn.cursor()
		
		data = cursor.execute(f"SELECT ID, Nombre, Clave FROM Usuarios WHERE Nombre = '{Usuario}' AND Clave = '{Key}'")
		
		Data_Tupla = ('null','null','null')

		for x in data:
			Data_Tupla = x
			self.ID = x[0]
		
		if Data_Tupla[1] == Usuario and Data_Tupla[2] == Key:
			return True
		else:
			return False
			
	def Exit_Data_2(self, Usuario):

		self.conn = sql.connect(self.__Data_Base)		

		cursor = self.conn.cursor()
		
		data = cursor.execute(f"SELECT Nombre FROM Usuarios WHERE Nombre = '{Usuario}'")
		
		Data_Tupla = ('null')

		for x in data:
			Data_Tupla = x
		
		if Data_Tupla[0] == Usuario:
			return True
		else:
			return False

	#------------Cerrar la Base de Dato-------------------
	def Close_Data(self):
		self.conn.close()



#====================================================================================================================================================


#--------------------------------------------Aplicacion ACIZ-------------------------------------------------------
class ACIZ():
	def __init__(self, ID, User):
		self.User = User
		self.ID = ID
#------------------------------------------Iniciar Base de Datos----------------------------------------------------
		self.DB_Empresa = r'{}\BD\Datos_General.db'.format(os.getcwd())

		self.__DB = r'{}\BD\{}'.format(os.getcwd(), f'{self.User}_Logistica.db')

#-------------------------------------------------Ventana-----------------------------------------------------------
		self.root = Tk()
		
		self.root.geometry('900x512')
		self.root.title('ACIZ')
		self.root.iconbitmap(r'{}\Imagenes\Muestra.ico'.format(os.getcwd()))
		self.root.resizable(0,0)
		
		#Toma de Datos de la Ventana
		wtotal = self.root.winfo_screenwidth()
		htotal = self.root.winfo_screenheight()
		wventana = 900
		hventana = 512

		#Formula para el Calculo de la Ventana
		pwidth = round(wtotal/2-wventana/2)
		pheight = round(htotal/2-hventana/2)

		#Geometría de la Ventana
		self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
#-------------------------------------------------Imagenes----------------------------------------------------------
		
		Config = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Config.png'.format(os.getcwd())).resize((40,40)), master=self.root)
		self.Boton = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Registrar.png'.format(os.getcwd())).resize((300,300)), master=self.root)
		self.Avatar = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Avatar.png'.format(os.getcwd())).resize((210,300)), master=self.root)
		self.Avatar2 = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Avatar.png'.format(os.getcwd())).resize((80,90)), master=self.root)
		self.compra = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Buy.png'.format(os.getcwd())).resize((110,110)), master=self.root)
		self.venta = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Sell.png'.format(os.getcwd())).resize((110,110)), master=self.root) 
		self.inventario = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Inventario.png'.format(os.getcwd())).resize((110,110)), master=self.root) 
		self.empleados = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Empleados.png'.format(os.getcwd())).resize((110,110)), master=self.root) 
		self.Estd = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Estd.png'.format(os.getcwd())).resize((110,110)), master=self.root) 
		self.Distri = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Distri.png'.format(os.getcwd())).resize((110,110)), master=self.root) 
		self.image_entry = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\entry.png'.format(os.getcwd())).resize((200,55)), master=self.root)
		self.Regis = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Registrar_E.png'.format(os.getcwd())).resize((210,230)), master=self.root) 
		self.Lapiz = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\lapiz.png'.format(os.getcwd())).resize((70,70)))
		self.mas = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\mas.png'.format(os.getcwd())).resize((70,70)))
		self.cancelar = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\cancelar.png'.format(os.getcwd())).resize((70,70)))
		self.Image_back = ImageTk.PhotoImage(Image.open(r"{}\Imagen\back.png".format(os.getcwd())).resize((30,30)))
		self.Image_Ayuda = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\pregunta.png".format(os.getcwd())).resize((30,30)))
		self.Image_Cuenta = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\usuario_config.png".format(os.getcwd())).resize((30,30)))
		self.Image_Actualizar = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\Cargando.png".format(os.getcwd())).resize((30,30)))
		self.Logotipo = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\Logotipo.png".format(os.getcwd())).resize((39,38)))
		self.Logotipo_2 = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\Logotipo.png".format(os.getcwd())).resize((50,38)))
		self.Ayuda_C = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\foto_compra.png".format(os.getcwd())).resize((450,200)))
		self.Ayuda_V = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\foto_venta.png".format(os.getcwd())).resize((450,200)))
		self.Ayuda_I = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\foto_inventario.png".format(os.getcwd())).resize((450,200)))
		self.Ayuda_E = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\foto_empleo.png".format(os.getcwd())).resize((450,200)))
		self.Ayuda_D = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\foto_distri.png".format(os.getcwd())).resize((450,200)))
		self.Ayuda_ES = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\foto_estadisticas.png".format(os.getcwd())).resize((450,200)))
		self.atras = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\atras.png".format(os.getcwd())).resize((35,35)))
		self.siguiente = ImageTk.PhotoImage(Image.open(r"{}\Imagenes\siguiente.png".format(os.getcwd())).resize((35,35)))
		self.Image_Logo = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Logotipo.png'.format(os.getcwd())).resize((50,50)))
		self.Image_prueba = Image.open(r"{}\Imagenes\Cargando.png".format(os.getcwd()))
		self.Image_Logo2 = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Logotipo.png'.format(os.getcwd())).resize((80,80)))
		self.Image_A_F= ImageTk.PhotoImage(Image.open(r'{}\Imagenes\agregar_foto.png'.format(os.getcwd())).resize((140,140)))
		self.Image_Init = ImageTk.PhotoImage(Image.open(r"{}\Imagen\Frame.png".format(os.getcwd())).resize((400,512)))
		self.Image_Boton = ImageTk.PhotoImage(Image.open(r"{}\Imagen\login.png".format(os.getcwd())).resize((160,150)))
		self.Diario = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Diario.png'.format(os.getcwd())).resize((110,110)), master=self.root) 
		self.Semana = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Semana.png'.format(os.getcwd())).resize((110,110)), master=self.root) 
		self.Mensual = ImageTk.PhotoImage(Image.open(r'{}\Imagenes\Mensual.png'.format(os.getcwd())).resize((110,110)), master=self.root) 

#-------------------------------------------------Cabezera----------------------------------------------------------
		
		self.Frame_C = Frame(self.root, bg='#4E74A6', height=100, width=900)
		self.Frame_C.place(x=0, y=0)

		#Logo de Empresa
		Label(self.Frame_C, image=self.Avatar2, bg='#4E74A6').place(x=5, y=5)

		#Nombre de Empresa
		self.Empresa = Label(self.Frame_C, text='Sysors', font=('Nexa Rust Slab Black 01', 30, 'bold'), bg='#4E74A6', fg='#F2F2F2')
		self.Empresa.place(x=100, y=16)

		self.dato_rif = Label(self.Frame_C, text='', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#4E74A6', fg='#F2F2F2')
		self.dato_rif.place(x=100, y=65)
		
		#Configuracion
		self.Boton_Configuracion = Button(self.Frame_C, image=Config, bg='#4E74A6', relief=FLAT, bd=0, activebackground='#4E74A6', command=self.Ajustes)
		self.Boton_Configuracion.place(x=840, y=30)


		#Frame del Reloj
		self.Frame_Reloj = Frame(self.Frame_C, bg="#4E74A6", height=100, width=210)
		self.Frame_Reloj.place (x=600, y=0)
		
		#Base de la Hora
		self.Hora = Label(self.Frame_Reloj, text="", font=('Nexa Rust Slab Black 01', 30, 'bold'), fg='#F2F2F2', bg='#4E74A6')
		self.Hora.place(x=9, y=8)

		#Base de la Dia
		self.Dia = Label(self.Frame_Reloj, text="", font=('Nexa Rust Slab Black 01', 15, 'bold'), fg='#F2F2F2', bg='#4E74A6')
		self.Dia.place(x=-1, y=58)

		

		self.Check_Ganancia()
		self.Check_Perdida()
		self.update_clock()
		self.get_date()
		self.Check_Registro()



		self.root.mainloop()

#--------------------------------------------------Reloj------------------------------------------------------------

	#Actualizacion del reloj
	def update_clock(self):
		now = time.strftime("%H:%M:%S")
		self.Hora.config(text=now)
		self.Frame_Reloj.after(1000, self.update_clock)

	#Actualizacion de Fecha
	def get_date(self):
		datetime_object = datetime.now()
		week_day = datetime_object.strftime("%A")
		Dias = {'Mondey':'Lunes', 'Tuesday':'Martes', 'Wednesday':'Miercoles', 'Thursday':'Jueves', 'Friday':'Viernes', 'Saturday':'Sabado', 'Sunday':'Domingo'}

		today = date.today()
		d1 = today.strftime("%d/%m/%Y")
		self.Dia.config(text = d1 + ' | ' + Dias[week_day])

#-----------------------------------------------Base de Dato--------------------------------------------------------
	#Chequear Si es un nuevo usuario
	def Check_Registro(self):
		self.conn = sql.connect(self.DB_Empresa)		

		cursor = self.conn.cursor()
		
		data = cursor.execute(f"SELECT Registro, Clave, Email FROM Usuarios WHERE Nombre = '{self.User}'")

		for x in data:
			self.Clave_user = x[1]
			self.Email = x[2]
			#Aqui se chequea con el RR si la base de dato muesta un valor True se registrara nuevo usuario, si la base
			#registra False se continuara el codigo
			if x[0] == '1' or x[0] == 1:
				self.Registro()
			else:
				self.Inicio_APP()
		
		self.Close_Data()


	#Actualizar de nuevo usuario ha ya existente
	def Update_Register(self):
		self.conn = sql.connect(self.DB_Empresa)		

		cursor = self.conn.cursor()
		
		data = cursor.execute(f'UPDATE Usuarios SET Registro=0 WHERE Nombre="{self.User}"')

		self.conn.commit()

		self.Close_Data()


	#Entrada de nuevo registro
	def Entry_Empresa(self):
		self.conn = sql.connect(self.DB_Empresa)		

		cursor = self.conn.cursor()
		
		data = cursor.execute(f"""INSERT INTO DAT_Empresa (ID_Usuario, Empresa, RIF, Direccion, Numero, Imagen) VALUES 
			({self.ID}, '{self.nombre_regisro.get()}', '{self.RIF.get()}', '{self.direccion_registro.get()}', '{self.contacto_registro.get()}','Agregar')""")

		self.conn.commit()

		self.Close_Data()


	#Salida de nombre de la empresa para usar en la aplicacion
	def Exit_Empresa(self):
		self.conn = sql.connect(self.DB_Empresa)		

		cursor = self.conn.cursor()
		
		data = cursor.execute(f"SELECT Empresa, RIF, Direccion, Numero FROM DAT_Empresa WHERE ID_Usuario = '{self.ID}'")

		self.nombre_empresa = ''
		self.nombre_rif = ''

		for x in data:
			self.nombre_empresa = x[0] #Nombre de la empresa 
			self.nombre_rif = x[1] #RIF de la empresa
			self.ubicacion_empresa = x[2] #Ubicacion de la empresa
			self.contacto_empresa = x[3] #Contacto de la empresa


		self.Close_Data()


#EXAMINAR ESTAS FUNCIONES MAS AFONDO=================================================
	#En caso de que no exista se crea al instante
	def Decidir_default(self):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()
					
		cursor.execute(f"INSERT INTO Preguntas (P_Compras, P_Ventas, ID_user) VALUES ('True', 'True', {self.ID})")
					
		self.conn.commit()

		self.Close_Data()


	#Tomar datos de Preguntas de Compras
	def Check_Decision_C(self):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()
					
		data = cursor.execute(f"SELECT P_Compras FROM Preguntas WHERE ID_Usuario = {self.ID}")
						
		for x in data:
			self.desicion_tomada_compra = x[0]

		self.Close_Data()


	#Tomar datos de Preguntas de Ventas 
	def Check_Decision_V(self):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()
					
		data = cursor.execute(f"SELECT P_Ventas FROM Preguntas WHERE ID_Usuario = {self.ID}")
						
		for x in data:
			self.desicion_tomada_ventas = x[0]

		self.Close_Data()


	#Chequeo de existencia de respuesta
	def Check_decision_existente(self):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()
					
		data = cursor.execute(f"SELECT ID_Usuario FROM Preguntas ")
		
		respuesta_D = False
		
		for x in data:
			if x[0] == self.ID:
				respuesta_D = True
				break
			else:
				respuesta_D = False
	
		self.Close_Data()
		
		#Chequeo de respuesta
		if respuesta_D == False:
			self.Decidir_default()
			
			self.Check_Decision_C()

			self.Check_Decision_V()
		
		else:
			self.Check_Decision_C()

			self.Check_Decision_V()
#====================================================================================





	def Check_Ganancia(self):
		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute("SELECT sum(PrecioT) FROM Venta")
		
		for x in data:
			self.Ganancia = x[0]
			
		self.Close_Data()

	#Actualizar El precio Total
	def Check_Perdida(self):
		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute("SELECT sum(PrecioT) FROM Gastos")
		
		for x in data:
			self.Perdida = x[0]
			
		self.Close_Data()


	#Cerrar Base de Datos
	def Close_Data(self):
		self.conn.close()

#-------------------------------------------------Ajustes-----------------------------------------------------------
	def Ajustes(self):
		#Desactivar Boton de Configuracion
		self.Boton_Configuracion.config(state='disabled')

		self.Configuracion = Frame(self.root,bg='#F2F2F2', height=412, width=900)
		self.Configuracion.place(x=0, y=101)

		ajuste_botones = Frame(self.Configuracion, bg='#d7d7d7', height=412, width=240)
		ajuste_botones.place(x=0, y=0)

		#======Boton Back======
		self.Boton_Back = Button(ajuste_botones, image=self.Image_back, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Destruir_Configuracion)
		self.Boton_Back.place(x=10, y=10)

		#======Boton Ayuda=====
		self.Boton_ayuda = Button(ajuste_botones, bg='#d7d7d7', text='Ayuda', anchor=W, bd=0, activebackground='#d7d7d7', font=('Nexa Rust Slab Black 01', 12, 'bold'), command=self.Ayuda_Cabezera)
		self.Boton_ayuda.place(x=90, y=56, height=40, width=125)

		self.Boton_ayuda_2 = Button(ajuste_botones, bg='#d7d7d7', image=self.Image_Ayuda, bd=0, activebackground='#d7d7d7', command=self.Ayuda_Cabezera)
		self.Boton_ayuda_2.place(x=50, y=60)


		#======Boton Cuenta======
		self.Boton_cuenta = Button(ajuste_botones, bg='#d7d7d7', text='Cuenta', bd=0, anchor=W, activebackground='#d7d7d7', font=('Nexa Rust Slab Black 01', 12, 'bold'), command=self.Confirmar_Identidad)
		self.Boton_cuenta.place(x=90, y=143, height=40, width=125)

		self.Boton_cuenta_2 = Button(ajuste_botones, bg='#d7d7d7', image=self.Image_Cuenta, bd=0, activebackground='#d7d7d7', command=self.Confirmar_Identidad)
		self.Boton_cuenta_2.place(x=50, y=145)


		#======Boton Acerca de ACIZ======
		self.Boton_aciz = Button(ajuste_botones, bg='#d7d7d7', text='Acerca de ACIZ', anchor=W, bd=0, activebackground='#d7d7d7', font=('Nexa Rust Slab Black 01', 12, 'bold'), command=self.Acerca_A)
		self.Boton_aciz.place(x=90, y=235, height=40, width=125)

		self.Boton_aciz_2 = Button(ajuste_botones, bg='#d7d7d7', image=self.Logotipo, bd=0, activebackground='#d7d7d7', command=self.Acerca_A)
		self.Boton_aciz_2.place(x=46, y=232)


		#=====Boton Actualizacion======
		self.Boton_actualizacion = Button(ajuste_botones, bg='#d7d7d7', text='Actualizacion', anchor=W, bd=0, activebackground='#d7d7d7', font=('Nexa Rust Slab Black 01', 12, 'bold'), command=self.Actualizacion)
		self.Boton_actualizacion.place(x=90, y=323, height=40, width=125)

		self.Boton_actualizacion_2 = Button(ajuste_botones, bg='#d7d7d7', image=self.Image_Actualizar, bd=0, activebackground='#d7d7d7', command=self.Actualizacion)
		self.Boton_actualizacion_2.place(x=49, y=325)


		#======Frame======
		self.Saludo = Frame(self.Configuracion,bg='#F2F2F2', height=412, width=660)
		self.Saludo.place(x=240, y=0)

		Label(self.Saludo, font=('Niagara Engraved',30), text=f'Hola {self.User} Estamos Aqui Para Ayudarte').place(x=140, y=40)

		Label(self.Saludo, image=self.Avatar).place(x=220, y=90)
	
	#eliminar Ventana de Configuracion
	def Destruir_Configuracion(self):
		#Destruir Frames para no sobrecargar el Cache
		try:
			self.Acerca.destroy()
		except:
			pass

		try:
			self.Saludo.destroy()
		except:
			pass

		try:
			self.Frame_Errores.destroy()
		except:
			pass

		try:
			self.Frame_Ayuda_Base.destroy()
		except:
			pass

		try:
			self.Frame_Ayuda_Cabezera.destroy()
		except:
			pass

		try:
			self.Actualizar.destroy()
		except:
			pass

		try:
			self.Frame_Cuenta.destroy()
		except:
			pass

		try:
			self.Frame_Indentidad.destroy()
		except:
			pass

		#Eliminar Ventana de Configuracion
		self.Configuracion.destroy()

		#Activar Boton de Configuracion
		self.Boton_Configuracion.config(state='normal')

#--------------------------------------------------Ayuda------------------------------------------------------------
	def Ayuda_Cabezera(self):
		#Eliminar Frame para no cargar la Cache
		try:
			self.Acerca.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache
		try:
			self.Saludo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache
		try:
			self.Frame_Errores.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache
		try:
			self.Frame_Ayuda_Base.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache
		try:
			self.Frame_Ayuda_Cabezera.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache
		try:
			self.Actualizar.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache
		try:
			self.Frame_Cuenta.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache
		try:
			self.Frame_Indentidad.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_C_segundo.destroy()
		except:
			pass
		try:
			self.Frame_D_C.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_I.destroy()
		except:
			pass
		try:
			self.Frame_D_I_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_V.destroy()
		except:
			pass
		try:
			self.Frame_D_V_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_E.destroy()
		except:
			pass
		try:
			self.Frame_D_E_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_D.destroy()
		except:
			pass
		try:
			self.Frame_D_D_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_ES.destroy()
		except:
			pass
		

		self.Frame_Ayuda_Cabezera = Frame(self.Configuracion, bg='#F2F2F2', height=70, width=660)
		self.Frame_Ayuda_Cabezera.place(x=240, y=0)

		Button(self.Frame_Ayuda_Cabezera, text='Descripción de Tablas', font=('Nexa Rust Slab Black 01', 14, 'bold'), fg='#1d56b8', relief=FLAT, bd=0, command=lambda:self.Ayuda_Base(0), bg='#F2F2F2').place(x=50, y=25)

		Button(self.Frame_Ayuda_Cabezera, text='Envio de Funciones/Errores', font=('Nexa Rust Slab Black 01', 14, 'bold'), fg='#1d56b8', relief=FLAT, bd=0, command= lambda:self.Ayuda_Base(1), bg='#F2F2F2').place(x=335, y=25)

		self.Ayuda_Base(0)
	
	#=================Ayuda General=================
	def Ayuda_Base(self, Eleccion):
		if Eleccion == 0:
			try:
				self.Frame_Errores.destroy()
			except:
				pass
			try:
				self.Saludo.destroy()
			except:
				pass

			self.Frame_Ayuda_Base = Frame(self.Configuracion, bg='#F2F2F2', height=337, width=660)
			self.Frame_Ayuda_Base.place(x=240, y=75)

			Label(self.Frame_Ayuda_Base, bd=2, bg='black', height=337).place(x=205, y=0, width=0)
			Label(self.Frame_Ayuda_Base, bd=2, bg='black', ).place(x=0, y=0, width=660, height=0)


			Button(self.Frame_Ayuda_Base, text='Tabla de Compras/Gastos', bg='#F2F2F2', activebackground='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), relief=FLAT, bd=0, command=self.A_Compra).place(x=20, y=20)
			
			Button(self.Frame_Ayuda_Base, text='Tabla de Inventario/Mercancia', bg='#F2F2F2', activebackground='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), relief=FLAT, bd=0, command=self.A_Inventario).place(x=20, y=70)
			
			Button(self.Frame_Ayuda_Base, text='Tabla de Ventas/Ganancias', bg='#F2F2F2', activebackground='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), relief=FLAT, bd=0, command=self.A_Venta).place(x=20, y=120)
			
			Button(self.Frame_Ayuda_Base, text='Tabla de Empleados', bg='#F2F2F2', activebackground='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), relief=FLAT, bd=0, command=self.A_Empleo).place(x=20, y=170)
			
			Button(self.Frame_Ayuda_Base, text='Tabla de Distribuidores', bg='#F2F2F2', activebackground='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), relief=FLAT, bd=0, command=self.A_Distri).place(x=20, y=220)

			Button(self.Frame_Ayuda_Base, text='Tabla de Estadisticas/Analisis, ', bg='#F2F2F2', activebackground='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), relief=FLAT, bd=0, command= self.A_Estadistica).place(x=20, y=270)

		else:
			try:
				self.Frame_Ayuda_Base.destroy()
			except:
				pass
			try:
				self.Saludo.destroy()
			except:
				pass

			self.Frame_Errores = Frame(self.Configuracion, bg='#F2F2F2', height=337, width=660)
			self.Frame_Errores.place(x=240, y=75)

			Label(self.Frame_Errores, text='Correo:', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold')).place(x=10, y=30)

			Entry(self.Frame_Errores, bg='#d7d7d7').place(x=60, y=30, height=25, width=250)

			Label(self.Frame_Errores, text='Asunto:', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold')).place(x=10, y=90)

			Entry(self.Frame_Errores, bg='#d7d7d7').place(x=60, y=90, height=25, width=250)

			Label(self.Frame_Errores, text='Opinion', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold')).place(x=300, y=120)

			Text(self.Frame_Errores, height=10, bg='#d7d7d7', width=81).place(x=5, y=139)

			Button(self.Frame_Errores, text='Enviar', bg='#F2F2F2', activebackground='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), bd=1).place(x=300, y=312)


	#=================Ayuda Compra==================
	def A_Compra(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_C_segundo.destroy()
		except:
			pass
		try:
			self.Frame_D_C.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_I.destroy()
		except:
			pass
		try:
			self.Frame_D_I_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_V.destroy()
		except:
			pass
		try:
			self.Frame_D_V_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_E.destroy()
		except:
			pass
		try:
			self.Frame_D_E_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_D.destroy()
		except:
			pass
		try:
			self.Frame_D_D_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_ES.destroy()
		except:
			pass
		


		#Frame de la ventana completa de Ayuda Compra/Gastos
		self.Frame_D_C = Frame(self.Frame_Ayuda_Base, bg='#F2F2F2', width=455, height=336)
		self.Frame_D_C.place(x=206, y=1)

		#imagen de Referencia 
		Label(self.Frame_D_C, image=self.Ayuda_C, bg="#F2F2F2").place(x=0, y=5)

		#Frame de los Textos
		self.Frame_D_C_segundo = Frame(self.Frame_D_C, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_C_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_C_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Compra).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_C_segundo, text='1. Numero de indentificación de los productos', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_C_segundo, text='2. Nombres de los productos', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_C_segundo, text='3. Precio de compra por unidad', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_C_segundo, text='4. Cantidad comprada', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)
	

	#Siguiente pagina
	def Segundo_A_Compra(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_C_segundo.destroy()

		#Frame de los Textos
		self.Frame_D_C_segundo = Frame(self.Frame_D_C, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_C_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_C_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Tercero_A_Compra).place(x=398, y=87)

		#boton Atras
		Button(self.Frame_D_C_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.A_Compra).place(x=350, y=87)

		#Texto
		Label(self.Frame_D_C_segundo, text='5. Precio Cantidad por Unidad', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_C_segundo, text='6. Fecha de Cuando se compro el producto', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_C_segundo, text='7. Cantidada Total de los productos', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_C_segundo, text='8. Precio Total de todas las compras', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)


	#Ultima pagina
	def Tercero_A_Compra(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_C_segundo.destroy()

		#Frame de los textos
		self.Frame_D_C_segundo = Frame(self.Frame_D_C, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_C_segundo.place(x=0, y=209)

		#Boton Atras
		Button(self.Frame_D_C_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Compra).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_C_segundo, text='9. Agregar Compra', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_C_segundo, text='10. Modificar Compra (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_C_segundo, text='11. Eliminar compra (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_C_segundo, text='12. Retoreceder a la anterior pagina', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)


	#===============Ayuda Inventario================
	def A_Inventario(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_C_segundo.destroy()
		except:
			pass
		try:
			self.Frame_D_C.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_I.destroy()
		except:
			pass
		try:
			self.Frame_D_I_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_V.destroy()
		except:
			pass
		try:
			self.Frame_D_V_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_E.destroy()
		except:
			pass
		try:
			self.Frame_D_E_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_D.destroy()
		except:
			pass
		try:
			self.Frame_D_D_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_ES.destroy()
		except:
			pass
		


		#Frame de la ventana completa de Ayuda Compra/Gastos
		self.Frame_D_I = Frame(self.Frame_Ayuda_Base, bg='#F2F2F2', width=455, height=336)
		self.Frame_D_I.place(x=206, y=1)

		#imagen de Referencia 
		Label(self.Frame_D_I, image=self.Ayuda_I, bg="#F2F2F2").place(x=0, y=5)

		#Frame de los Textos
		self.Frame_D_I_segundo = Frame(self.Frame_D_I, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_I_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_I_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Inventario).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_I_segundo, text='1. Numero de indentificación de los productos', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_I_segundo, text='2. Nombres de los productos', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_I_segundo, text='3. Precio de Unidad del producto', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_I_segundo, text='4. Mercancia disponible de los productos Total', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)
	
	#Siguiente pagina
	def Segundo_A_Inventario(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_I_segundo.destroy()

		#Frame de los Textos
		self.Frame_D_I_segundo = Frame(self.Frame_D_I, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_I_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_I_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Tercero_A_Inventario).place(x=398, y=87)

		#boton Atras
		Button(self.Frame_D_I_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.A_Inventario).place(x=350, y=87)

		#Texto
		Label(self.Frame_D_I_segundo, text='5. Precio Mercancia por Unidad', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_I_segundo, text='6. Fecha de Cuando se agrego el producto', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_I_segundo, text='7. Mercancia Total de los disponible', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_I_segundo, text='8. Precio Total de todas las Mercancia', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)

	#Ultima Pagina
	def Tercero_A_Inventario(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_I_segundo.destroy()

		#Frame de los textos
		self.Frame_D_I_segundo = Frame(self.Frame_D_I, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_I_segundo.place(x=0, y=209)

		#Boton Atras
		Button(self.Frame_D_I_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Inventario).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_I_segundo, text='9. Agregar Mercancia', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_I_segundo, text='10. Modificar Mercancia (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_I_segundo, text='11. Eliminar Mercancia (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		Label(self.Frame_D_I_segundo, text='12. Retoreceder a la anterior pagina', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)


	#=================Ayuda Venta===================
	def A_Venta(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_C_segundo.destroy()
		except:
			pass
		try:
			self.Frame_D_C.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_I.destroy()
		except:
			pass
		try:
			self.Frame_D_I_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_V.destroy()
		except:
			pass
		try:
			self.Frame_D_V_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_E.destroy()
		except:
			pass
		try:
			self.Frame_D_E_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_D.destroy()
		except:
			pass
		try:
			self.Frame_D_D_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_ES.destroy()
		except:
			pass
		


		#Frame de la ventana completa de Ayuda Compra/Gastos
		self.Frame_D_V = Frame(self.Frame_Ayuda_Base, bg='#F2F2F2', width=455, height=336)
		self.Frame_D_V.place(x=206, y=1)

		#imagen de Referencia 
		Label(self.Frame_D_V, image=self.Ayuda_V, bg="#F2F2F2").place(x=0, y=5)

		#Frame de los Textos
		self.Frame_D_V_segundo = Frame(self.Frame_D_V, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_V_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_V_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Venta).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_V_segundo, text='1. Numero de indentificación de los productos', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_V_segundo, text='2. Nombres de los productos', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_V_segundo, text='3. Precio de venta por unidad', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_V_segundo, text='4. Cantidad disponible de los productos', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)
	

	#Siguiente pagina
	def Segundo_A_Venta(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_V_segundo.destroy()

		#Frame de los Textos
		self.Frame_D_V_segundo = Frame(self.Frame_D_V, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_V_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_V_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Tercero_A_Venta).place(x=398, y=87)

		#boton Atras
		Button(self.Frame_D_V_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.A_Venta).place(x=350, y=87)

		#Texto
		Label(self.Frame_D_V_segundo, text='5. Precio Cantidad por Unidad', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_V_segundo, text='6. Fecha de Cuando se vendio el producto', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_V_segundo, text='7. Cantidada Total de los producto', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_V_segundo, text='8. Precio Total de todas las ventas', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)


	#Ultima Pagina
	def Tercero_A_Venta(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_V_segundo.destroy()

		#Frame de los textos
		self.Frame_D_V_segundo = Frame(self.Frame_D_V, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_V_segundo.place(x=0, y=209)

		#Boton Atras
		Button(self.Frame_D_V_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Venta).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_V_segundo, text='9. Agregar Venta', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_V_segundo, text='10. Modificar Venta (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_V_segundo, text='11. Eliminar Venta (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_V_segundo, text='12. Retoreceder a la anterior pagina', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)


	#===============Ayuda Empleado==================
	def A_Empleo(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_C_segundo.destroy()
		except:
			pass
		try:
			self.Frame_D_C.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_I.destroy()
		except:
			pass
		try:
			self.Frame_D_I_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_V.destroy()
		except:
			pass
		try:
			self.Frame_D_V_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_E.destroy()
		except:
			pass
		try:
			self.Frame_D_E_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_D.destroy()
		except:
			pass
		try:
			self.Frame_D_D_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_ES.destroy()
		except:
			pass
		

		#Frame de la ventana completa de Ayuda Compra/Gastos
		self.Frame_D_E = Frame(self.Frame_Ayuda_Base, bg='#F2F2F2', width=455, height=336)
		self.Frame_D_E.place(x=206, y=1)

		#imagen de Referencia 
		Label(self.Frame_D_E, image=self.Ayuda_E, bg="#F2F2F2").place(x=0, y=5)

		#Frame de los Textos
		self.Frame_D_E_segundo = Frame(self.Frame_D_E, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_E_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_E_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Empleo).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_E_segundo, text='1. Nombres de los Empleados', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_E_segundo, text='2. Nacimientos de los Empleados', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_E_segundo, text='3. Puesto Laboral del Empleado', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_E_segundo, text='4. Nomina o Pago de los Empleados', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)

	
	#Siguiente pagina
	def Segundo_A_Empleo(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_E_segundo.destroy()

		#Frame de los Textos
		self.Frame_D_E_segundo = Frame(self.Frame_D_E, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_E_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_E_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Tercero_A_Empleo).place(x=398, y=87)

		#boton Atras
		Button(self.Frame_D_E_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.A_Empleo).place(x=350, y=87)

		#Texto
		Label(self.Frame_D_E_segundo, text='5. Nota o Acotacion sobre el empleado (actitud o caracteristicas)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_E_segundo, text='6. Lista de empleados existentes', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_E_segundo, text='7. Agregar Empleado', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		
	#Ultima Pagina
	def Tercero_A_Empleo(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_E_segundo.destroy()

		#Frame de los textos
		self.Frame_D_E_segundo = Frame(self.Frame_D_E, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_E_segundo.place(x=0, y=209)

		#Boton Atras
		Button(self.Frame_D_E_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Empleo).place(x=398, y=87)
		
		#Texto
		Label(self.Frame_D_E_segundo, text='8. Modificacion del Empleado (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_E_segundo, text='9. Eliminar Base del Empleado (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_E_segundo, text='10. Retoreceder a la anterior pagina', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)


	#=============Ayuda Distribuidores==============
	def A_Distri(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_C_segundo.destroy()
		except:
			pass
		try:
			self.Frame_D_C.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_I.destroy()
		except:
			pass
		try:
			self.Frame_D_I_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_V.destroy()
		except:
			pass
		try:
			self.Frame_D_V_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_E.destroy()
		except:
			pass
		try:
			self.Frame_D_E_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_D.destroy()
		except:
			pass
		try:
			self.Frame_D_D_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_ES.destroy()
		except:
			pass
		


		#Frame de la ventana completa de Ayuda Compra/Gastos
		self.Frame_D_D = Frame(self.Frame_Ayuda_Base, bg='#F2F2F2', width=455, height=336)
		self.Frame_D_D.place(x=206, y=1)

		#imagen de Referencia 
		Label(self.Frame_D_D, image=self.Ayuda_D, bg="#F2F2F2").place(x=0, y=5)

		#Frame de los Textos
		self.Frame_D_D_segundo = Frame(self.Frame_D_D, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_D_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_D_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Distri).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_D_segundo, text='1. Base de Datos de las Distribuidoras', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_D_segundo, text='2. Nombres de las Distribuidoras', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_D_segundo, text='3. RIF de las Distribuidoras (No Obligatorio)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_D_segundo, text='4. Ubicación de las Distribuidoras (No Obligatorio)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)
	

	#Siguiente pagina
	def Segundo_A_Distri(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_D_segundo.destroy()

		#Frame de los Textos
		self.Frame_D_D_segundo = Frame(self.Frame_D_D, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_D_segundo.place(x=0, y=209)

		#Boton siguiente
		Button(self.Frame_D_D_segundo, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Tercero_A_Distri).place(x=398, y=87)

		#boton Atras
		Button(self.Frame_D_D_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.A_Distri).place(x=350, y=87)

		#Texto
		Label(self.Frame_D_D_segundo, text='5. Contacto de las Distribuidoras', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_D_segundo, text='6. Agregar Empleados', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)


	#Siguiente pagina
	def Tercero_A_Distri(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		self.Frame_D_D_segundo.destroy()

		#Frame de los Textos
		self.Frame_D_D_segundo = Frame(self.Frame_D_D, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_D_segundo.place(x=0, y=209)

		#boton Atras
		Button(self.Frame_D_D_segundo, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Segundo_A_Distri).place(x=398, y=87)

		#Texto
		Label(self.Frame_D_D_segundo, text='7. Modificar Base del Empleado (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_D_segundo, text='8. Eliminar Base del Empleado (Seleccionar antes de hacer Click al boton)', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_D_segundo, text='9. Retoreceder a la anterior pagina', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)


#=============Ayuda Distribuidores==============
	def A_Estadistica(self):
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_C_segundo.destroy()
		except:
			pass
		try:
			self.Frame_D_C.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_I.destroy()
		except:
			pass
		try:
			self.Frame_D_I_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los textos
		try:
			self.Frame_D_V.destroy()
		except:
			pass
		try:
			self.Frame_D_V_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_E.destroy()
		except:
			pass
		try:
			self.Frame_D_E_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_D.destroy()
		except:
			pass
		try:
			self.Frame_D_D_segundo.destroy()
		except:
			pass
		#Eliminar Frame para no cargar la Cache, El Frame eliminado es de los Texto
		try:
			self.Frame_D_ES.destroy()
		except:
			pass
		

		#Frame de la ventana completa de Ayuda Compra/Gastos
		self.Frame_D_ES = Frame(self.Frame_Ayuda_Base, bg='#F2F2F2', width=455, height=336)
		self.Frame_D_ES.place(x=206, y=1)

		#imagen de Referencia 
		Label(self.Frame_D_ES, image=self.Ayuda_ES, bg="#F2F2F2").place(x=0, y=5)

		#Frame de los Textos
		self.Frame_D_ES_segundo = Frame(self.Frame_D_ES, bg='#F2F2F2', width=455, height=150)
		self.Frame_D_ES_segundo.place(x=0, y=209)

		#Texto
		Label(self.Frame_D_ES_segundo, text='1. Analisis diario a medida que se ingresa informacion', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=10)

		#Texto
		Label(self.Frame_D_ES_segundo, text='2. Analisis semanal a medida que se ingresa informacion', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=40)

		#Texto
		Label(self.Frame_D_ES_segundo, text='3. Analisis mensual a medida que se ingresa informacion', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=70)

		#Texto
		Label(self.Frame_D_ES_segundo, text='4. Retroceder a la pagina anterior', font=('Nexa Rust Slab Black 01', 10), bg='#F2F2F2').place(x=10, y=100)
	

#--------------------------------------------------Cuenta-----------------------------------------------------------
	def Cuenta(self):
		
		self.Confirmar_Identidad()

		self.Frame_Cuenta = Frame(self.Configuracion,bg='#F2F2F2', height=412, width=660)
		self.Frame_Cuenta.place(x=240, y=0)

		Button(self.Frame_Cuenta, image=self.Image_A_F, bg='#d7d7d7', relief=FLAT, bd=0).place(x=32, y=28)

		#Nombre Empresa
		Label(self.Frame_Cuenta, text='Empresa: ', font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=200, y=40)
		Label(self.Frame_Cuenta, text=self.nombre_empresa, font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=290, y=40)

		#RIF Empresa
		Label(self.Frame_Cuenta, text='RIF: ', font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=200, y=70)
		Label(self.Frame_Cuenta, text=self.nombre_rif, font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=290, y=70)

		#Ubicacion Empresa
		Label(self.Frame_Cuenta, text='Ubicacion: ', font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=200, y=100)
		Label(self.Frame_Cuenta, text=self.ubicacion_empresa, font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=290, y=100)

		#Contacto Empresa
		Label(self.Frame_Cuenta, text='Contacto: ', font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=200, y=130)
		Label(self.Frame_Cuenta, text=self.contacto_empresa, font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=290, y=130)

		#Usuario
		Label(self.Frame_Cuenta, text='Usuario: ', font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=20, y=210)
		Label(self.Frame_Cuenta, text=self.User, font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=90, y=210)

		#Clave
		Label(self.Frame_Cuenta, text='Clave: ', font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=20, y=245)
		Label(self.Frame_Cuenta, text=self.Clave_user, font=('Nexa Rust Slab Black 01', 11), bg='#F2F2F2').place(x=90, y=245)


		Button(self.Frame_Cuenta, text='Editar Informacion', bg='#d7d7d7').place(x=270, y=370)

	#Confirmar cuenta
	def Confirmar_Identidad(self):
		#Destruir Frame
		try:
			self.Acerca.destroy()
		except:
			pass

		try:
			self.Saludo.destroy()
		except:
			pass

		try:
			self.Frame_Errores.destroy()
		except:
			pass

		try:
			self.Frame_Ayuda_Base.destroy()
		except:
			pass

		try:
			self.Frame_Ayuda_Cabezera.destroy()
		except:
			pass

		try:
			self.Actualizar.destroy()
		except:
			pass

		try:
			self.Frame_Cuenta.destroy()
		except:
			pass

		try:
			self.Frame_Indentidad.destroy()
		except:
			pass

		#Frame de identidad
		self.Frame_Indentidad = Frame(self.Configuracion,bg='#F2F2F2', height=412, width=660)
		self.Frame_Indentidad.place(x=240, y=0)

		#-----------Titulo de la Ventana------------------
		Label(self.Frame_Indentidad, bg='#F2F2F2', text='Iniciar Sesión', font=('Arial', 20, 'bold')).place(x=236, y=10)
		
		
		#-----------Entrada de Usuario-------------------
		self.User_Check_I = Entry(self.Frame_Indentidad, relief=FLAT, bd=1, bg='#d7e1e2', font=('Arial', 10, 'bold'), fg='black')
		self.User_Check_I.place(x=243, y=100, height=38, width=173)
		self.User_Check_I.focus()
		self.User_Check_I.bind("<Return>", lambda _: self.Key_Check_I.focus())
		

		#-----------Entrada de clave---------------------
		self.Key_Check_I = Entry(self.Frame_Indentidad, relief=FLAT, bd=1, bg='#d7e1e2', font=('Arial', 14, 'bold'), fg='black')
		self.Key_Check_I.place(x=243, y=180, height=38, width=173)
		self.Key_Check_I.config(show='*')
		self.Key_Check_I.bind("<Return>", lambda _: self.Check_Identidad())
		

		#---------------Mensaje-------------------------- 
		self.M_K = Label(self.Frame_Indentidad, bg='#F2F2F2', text='', font=('Arial', 10, 'bold'), fg='red')
		self.M_K.place(x=212, y=230)

		
		#-----------Boton de Inicio----------------------
		Button(self.Frame_Indentidad, relief=FLAT, image=self.Image_Boton, bd=0 , height=60, bg='#F2F2F2', command=self.Check_Identidad).place(x=248, y=300)

		self.Intentos_Clave = 0

	#Chequeo de identidad
	def Check_Identidad(self):

		if self.User_Check_I.get() == self.User and self.Key_Check_I.get() == self.Clave_user:
			#Cuenta confirmada // Destruir Frame de Identidad
			self.Frame_Indentidad.destroy()
			self.Cuenta()

		else:
			#Fallo de la clave
			self.M_K['text'] = f'Usuario o Clave incorrecta,{3-self.Intentos_Clave} intentos'

			#Suma de los intentos restante
			self.Intentos_Clave += 1

		if self.Intentos_Clave > 3:

			#Desactivar botones por seguridad
			self.Boton_ayuda.config(state='disabled')
			self.Boton_ayuda_2.config(state='disabled')
			self.Boton_cuenta.config(state='disabled')
			self.Boton_cuenta_2.config(state='disabled')
			self.Boton_aciz.config(state='disabled')
			self.Boton_aciz_2.config(state='disabled')
			self.Boton_actualizacion.config(state='disabled')
			self.Boton_actualizacion_2.config(state='disabled')
			self.Boton_Back.config(state='disabled')



			#Frame del tiempo de espera
			self.Frame_Espera = Frame(self.Configuracion,bg='#FFFFFF', height=412, width=660)
			self.Frame_Espera.place(x=240, y=0)

			#Label del video
			self.V_Espera = Label(self.Frame_Espera, bd=0)
			self.V_Espera.place(x=280, y=115)

			#Bucle del video
			self.C_Bucle = 0

			#llamar al video
			self.Tercera_Captura()

			#Conteo de segundos
			self.Tiempo_Espera()


	#Tercera Captura
	def Tercera_Captura(self):
		#Capturamos la ubicacion del video
		self.Tercera_Cature = cv2.VideoCapture(r"{}\Imagenes\video.mp4".format(os.getcwd()))
		
		#Se llama a la configuracion del video
		self.Tercer_Video()


	#Tercera Video
	def Tercer_Video(self):
		#Caturar Video
		ret, frame = self.Tercera_Cature.read()

		#Comprobando los Datos del video
		if ret == True:
			#Acomodamos el Frame al tamano deseado
			frame = imutils.resize(frame, width=100)

			#Se cambia el color para que sea compatible con el Label
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

			#Creamos la imagen
			im = Image.fromarray(frame)
			img = ImageTk.PhotoImage(image=im)

			#insertamos la imagen en el Label
			self.V_Espera.configure(image=img)
			self.V_Espera.image=img

			#Se llama continuamente, para pasar los Frame
			self.V_Espera.after(20, self.Tercer_Video)
	
		else:
			#Controlamos el bucle segun lo deseado
			self.C_Bucle += 1

			#DEfinimos el tiempo del bucle
			if self.C_Bucle == 5:
				pass

			else:
				#Volvemos a llamar a la captura para repetir el bucle cuanto deseemos
				self.V_Espera.after(10, self.Tercera_Captura)
	

	#Formato de Tiempo de Espera por Equivocacion
	def Tiempo_Espera(self):
		self.hora_inicio = datetime.now()

		self.variable_hora_actual = StringVar(self.Frame_Espera, value=self.obtener_tiempo_transcurrido_formateado())

		self.tiempo = Label(self.Frame_Espera, font=('Nexa Rust Slab Black 01', 40, 'bold'), textvariable = self.variable_hora_actual, bg='#FFFFFF')
		self.tiempo.place(x=300, y=240)

		self.refrescar_tiempo_transcurrido()


	#Algoritmo de tiempo de espera
	def segundos_a_segundos_minutos_y_horas(self, segundos):
		#Algoritmo de conversion
		horas = int(segundos / 60 / 60)

		segundos -= horas*60*60

		minutos = int(segundos/60)

		segundos -= minutos*60

		if segundos == 11:
			#Destruir Frame de pantalla de carga
			self.Frame_Espera.destroy()

			#Normalizar los Intentos
			self.Intentos_Clave = 0

			#Anular el mensaje
			self.M_K['text'] = ''

			#Normalizar los botones
			self.Boton_ayuda.config(state='normal')
			self.Boton_ayuda_2.config(state='normal')
			self.Boton_cuenta.config(state='normal')
			self.Boton_cuenta_2.config(state='normal')
			self.Boton_aciz.config(state='normal')
			self.Boton_aciz_2.config(state='normal')
			self.Boton_actualizacion.config(state='normal')
			self.Boton_actualizacion_2.config(state='normal')
			self.Boton_Back.config(state='normal')


		return f"{segundos:02d}"


	#Formatear el tiempo
	def obtener_tiempo_transcurrido_formateado(self):
		segundos_transcurridos= (datetime.now() - self.hora_inicio).total_seconds()
		
		return self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))


	#Refrezcar Calculo del tiempo
	def refrescar_tiempo_transcurrido(self):
		
		self.variable_hora_actual.set(self.obtener_tiempo_transcurrido_formateado())


		self.tiempo.after(500, self.refrescar_tiempo_transcurrido)

#----------------------------------------------Acerca De ACIZ-------------------------------------------------------
	def Acerca_A(self):
		#Destruir Frame
		try:
			self.Acerca.destroy()
		except:
			pass

		try:
			self.Saludo.destroy()
		except:
			pass

		try:
			self.Frame_Errores.destroy()
		except:
			pass

		try:
			self.Frame_Ayuda_Base.destroy()
		except:
			pass

		try:
			self.Frame_Ayuda_Cabezera.destroy()
		except:
			pass

		try:
			self.Actualizar.destroy()
		except:
			pass

		try:
			self.Frame_Cuenta.destroy()
		except:
			pass

		try:
			self.Frame_Indentidad.destroy()
		except:
			pass


		#Frame
		self.Acerca = Frame(self.Configuracion, bg='#F2F2F2', height=412, width=660)
		self.Acerca.place(x=240, y=0)

		#Logotipo
		Label(self.Acerca, image=self.Logotipo_2, bg='#F2F2F2').place(x=25, y=5)

		#Titulo
		Label(self.Acerca, text='Sysors', font=('Nexa Rust Slab Black 01', 14, 'bold'), bg='#F2F2F2').place(x=85, y=12)

		#Politica de Privacidad
		Label(self.Acerca, text='Sysors. ofrece este programa de gestión de empresa llamada ACIZ, con el fin de ayudar a las empresas y negocios', bg='#F2F2F2').place(x=25, y=50)
		Label(self.Acerca, text='a organizar sus datos e inventarios, el  cual  seguirá  mejorando  con  sus  actualizaciones  con  el  fin  de  ayudar a ', bg='#F2F2F2').place(x=25, y=70)
		Label(self.Acerca, text='ejemplificar el uso del programa y su seguridad.', bg='#F2F2F2').place(x=25, y=90)

		Label(self.Acerca, text='Política y Responsabilidades', font=('Arial',11,'bold'), bg='#F2F2F2').place(x=230, y=120)

		Label(self.Acerca, text='•Sysors no se hará cargo de responsabilidad ninguna perdida de datos de su empresa o negocio.', bg='#F2F2F2').place(x=45, y=145)

		Label(self.Acerca, text='terceros.', bg='#F2F2F2').place(x=50, y=185)
		Label(self.Acerca, text='•Sysors no se hará cargo de responsabilidad a virus o malware, que afecte los equipos de trabajos de  ', bg='#F2F2F2').place(x=45, y=170)

		Label(self.Acerca, text='•Sysors protege la información de sus usuarios.', bg='#F2F2F2').place(x=45, y=210)

		Label(self.Acerca, text='programas.', bg='#F2F2F2').place(x=50, y=250)
		Label(self.Acerca, text='•Sysors no recopila información personal de ningún usuario que este registrado o usando nuestros ', bg='#F2F2F2').place(x=45, y=235)
		
		Label(self.Acerca, text='Empresas y negocios.', bg='#F2F2F2').place(x=50, y=290)
		Label(self.Acerca, text='•Sysors únicamente ofrece un solo “servicio’’, el cual es ayudar a la gestión de datos de los usuarios, ', bg='#F2F2F2').place(x=45, y=275)
		
		Label(self.Acerca, text='publicación en medios sociales y redes, sin ninguna autorización de Sysors.', bg='#F2F2F2').place(x=50, y=330)
		Label(self.Acerca, text='•Sysors no permite la venta (Terceros) o distribución ilegal de nuestros programas, tampoco cualquier ', bg='#F2F2F2').place(x=45, y=315)
		
		Label(self.Acerca, text='Page 1', bg='#F2F2F2').place(x=600, y=350)

		Button(self.Acerca, image=self.siguiente, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Acerca_Segundo).place(x=600, y=370)


	def Acerca_Segundo(self):
		#Destruir Frame
		self.Acerca.destroy()
		
		#Frame
		self.Acerca = Frame(self.Configuracion, bg='#F2F2F2', height=412, width=660)
		self.Acerca.place(x=240, y=0)
		
		#Logotipo
		Label(self.Acerca, image=self.Logotipo_2, bg='#F2F2F2').place(x=25, y=5)

		#Titulo
		Label(self.Acerca, text='Sysors', font=('Nexa Rust Slab Black 01', 14, 'bold'), bg='#F2F2F2').place(x=85, y=12)

		#Politica de Privacidad
		Label(self.Acerca, text='•Sysors es el único dueño legítimo de ACIZ.', bg='#F2F2F2').place(x=45, y=50)
		Label(self.Acerca, text='anuncio contactar por los medios dados.', bg='#F2F2F2').place(x=50, y=90)

		Label(self.Acerca, text='•Sysors por el momento no utiliza ningún medio de anuncio, cualquier programa de Sysors que tenga ', bg='#F2F2F2').place(x=45, y=75)
		
		Label(self.Acerca, text='dicho “servicio”.', bg='#F2F2F2').place(x=50, y=160)
		Label(self.Acerca, text='o ponga a disposición a través de la misma; no será responsable por cualquier error u omisión en ', bg='#F2F2F2').place(x=50, y=145)
		Label(self.Acerca, text='se hace responsable de la exactitud, utilidad o disponibilidad de cualquier información que se transmita ', bg='#F2F2F2').place(x=50, y=130)
		Label(self.Acerca, text='•Este programa y sus componentes se ofrecen únicamente con fines de “servicio”; este programa no ', bg='#F2F2F2').place(x=45, y=115)
		
		Label(self.Acerca, text='Servicio: ACIZ solo se encarga de administrar y ordenar base de datos de los usuarios que lo utilicen. ', bg='#F2F2F2').place(x=25, y=185)

		Label(self.Acerca, text='Contacto:      ndsmartscompany@gmail.com', bg='#F2F2F2').place(x=25, y=220)

		Label(self.Acerca, text='Page 2', bg='#F2F2F2').place(x=20, y=350)
		
		Button(self.Acerca, image=self.atras, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Acerca_A).place(x=20, y=370)

#----------------------------------------------Actualizaciones------------------------------------------------------
	def Actualizacion(self):
		#Destruir Frame
		try:
			self.Acerca.destroy()
		except:
			pass

		try:
			self.Saludo.destroy()
		except:
			pass

		try:
			self.Frame_Errores.destroy()
		except:
			pass

		try:
			self.Frame_Ayuda_Base.destroy()
		except:
			pass

		try:
			self.Frame_Ayuda_Cabezera.destroy()
		except:
			pass

		try:
			self.Actualizar.destroy()
		except:
			pass

		try:
			self.Frame_Cuenta.destroy()
		except:
			pass

		try:
			self.Frame_Indentidad.destroy()
		except:
			pass

		#Frame
		self.Actualizar = Frame(self.Configuracion,bg='#FFFFFF', height=412, width=660)
		self.Actualizar.place(x=240, y=0)

		#Espacio del Video
		self.V_O = Label(self.Actualizar, bd=0)
		self.V_O.place(x=280, y=115)

		#Controlador del bucle
		self.C_Bucle = 0

		self.Captura()

	#Primera Captura
	def Captura(self):
		#Capturamos la ubicacion del video
		self.Cature = cv2.VideoCapture(r"{}\Imagenes\video.mp4".format(os.getcwd()))
		
		#Se llama a la configuracion del video
		self.Video()

	#Primer Video
	def Video(self):
		#Caturar Video
		ret, frame = self.Cature.read()

		#Comprobando los Datos del video
		if ret == True:
			#Acomodamos el Frame al tamano deseado
			frame = imutils.resize(frame, width=100)

			#Se cambia el color para que sea compatible con el Label
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

			#Creamos la imagen
			im = Image.fromarray(frame)
			img = ImageTk.PhotoImage(image=im)

			#insertamos la imagen en el Label
			self.V_O.configure(image=img)
			self.V_O.image=img

			#Se llama continuamente, para pasar los Frame
			self.V_O.after(20, self.Video)
				
		else:
			#Controlamos el bucle segun lo deseado
			self.C_Bucle += 1
			
			#DEfinimos el tiempo del bucle
			if self.C_Bucle == 3:
				self.Info_Update()

			else:
				#Volvemos a llamar a la captura para repetir el bucle cuanto deseemos
				self.V_O.after(10, self.Captura)


	#informacion de las Actualizaciones
	def Info_Update(self):
		self.Actualizar.destroy()

		#Frame
		self.Actualizar = Frame(self.Configuracion,bg='#FFFFFF', height=412, width=660)
		self.Actualizar.place(x=240, y=0)

		#Texto
		Label(self.Actualizar, text='ACIZ Esta Actualizado', font=('Nexa Rust Slab Black 01', 10), bg="#FFFFFF").place(x=260, y=50)

		#Video de Check
		self.Confirm_Video = Label(self.Actualizar, bd=0)
		self.Confirm_Video.place(x=200,y=30)

		#Texto
		Label(self.Actualizar, text='Copyright © 2022 Los creadores de ACIZ. Todos los derechos reservados.', bg="#FFFFFF").place(x=135, y=80)

		#Texto
		Label(self.Actualizar, text='Version: 0.5, Alpha', bg="#FFFFFF").place(x=275, y=110)

		self.Captura_2()


	#Segunda CAptura
	def Captura_2(self):
		#Capturamos la ubicacion del video
		self.Cature_2 = cv2.VideoCapture(r"{}\Imagenes\Check.mp4".format(os.getcwd()))
		
		#Se llama a la configuracion del video
		self.Video_2()

	#Segundo Video
	def Video_2(self):
		#Caturar Video
		ret, frame = self.Cature_2.read()

		#Comprobando los Datos del video
		if ret == True:
			#Acomodamos el Frame al tamano deseado
			frame = imutils.resize(frame, width=50)

			#Se cambia el color para que sea compatible con el Label
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

			#Creamos la imagen
			im = Image.fromarray(frame)
			img = ImageTk.PhotoImage(image=im)

			#insertamos la imagen en el Label
			self.Confirm_Video.configure(image=img)
			self.Confirm_Video.image=img

			#Se llama continuamente, para pasar los Frame
			self.Confirm_Video.after(20, self.Video_2)

#-------------------------------------------------Registro----------------------------------------------------------
	def Registro(self):
		#Frame para registrar a nuevas empresas
		self.Frame_R = Frame(self.root,bg='#F2F2F2', height=412, width=900)
		self.Frame_R.place(x=0, y=101)

		#Imagen del avatar que se muestra
		Label(self.Frame_R, image=self.Avatar, bg='#F2F2F2').place(x=650, y=50)

		#Entrada para registrar el nombre de la empresa
		Label(self.Frame_R, text='Empresa', font=('Nexa Rust Slab Black 01', 15, 'bold'),bg='#F2F2F2').place(x=135, y=60)
		Label(self.Frame_R, image=self.image_entry, bg='#F2F2F2').place(x=80,y=90)
		self.nombre_regisro = Entry(self.Frame_R, bg='#d7e1e2', bd=0, font=('Nexa Rust Slab Black 01', 12, 'bold'))
		self.nombre_regisro.place(x=90, y=99, height=40, width=185)
		self.nombre_regisro.focus() #Localiza el cursor de la entrada
		self.nombre_regisro.bind('<Return>', lambda _: self.RIF.focus()) #LLama a la otra entrada para lozalizar el cursor

		#Entrada para regitrar el RIF de la empresa
		Label(self.Frame_R, text='RIF', font=('Nexa Rust Slab Black 01', 15, 'bold'),bg='#F2F2F2').place(x=475, y=60)
		Label(self.Frame_R, image=self.image_entry, bg='#F2F2F2').place(x=390,y=90)
		self.RIF = Entry(self.Frame_R, bg='#d7e1e2', bd=0, font=('Nexa Rust Slab Black 01', 12, 'bold'))
		self.RIF.place(x=405, y=99, height=40, width=185)
		self.RIF.bind('<Return>', lambda _: self.direccion_registro.focus()) #LLama a la otra entrada para lozalizar el cursor

		#Entrada para regitrar la direccion de la empresa
		Label(self.Frame_R, text='Dirección', font=('Nexa Rust Slab Black 01', 15, 'bold'), bg='#F2F2F2').place(x=135, y=200)
		Label(self.Frame_R, image=self.image_entry, bg='#F2F2F2').place(x=80,y=230)
		self.direccion_registro = Entry(self.Frame_R, bg='#d7e1e2', bd=0, font=('Nexa Rust Slab Black 01', 12, 'bold'))
		self.direccion_registro.place(x=92, y=239, height=40, width=180)
		self.direccion_registro.bind('<Return>', lambda _: self.contacto_registro.focus()) #LLama a la otra entrada para lozalizar el cursor

		#Entrada para regitrar el numero de contacto de la empresa
		Label(self.Frame_R, text='Contacto', font=('Nexa Rust Slab Black 01', 15, 'bold'),bg='#F2F2F2').place(x=445, y=200)
		Label(self.Frame_R, image=self.image_entry, bg='#F2F2F2').place(x=390,y=230)
		self.contacto_registro = Entry(self.Frame_R, bg='#d7e1e2', bd=0, font=('Nexa Rust Slab Black 01', 12, 'bold'))
		self.contacto_registro.place(x=402, y=239, height=40, width=180)
		self.contacto_registro.bind('<Return>', lambda _: self.Envio_Registro()) #LLama a la funcion de Envio_Registro()

		#Boton para llamar la funcion de Envio_Registro()
		Button(self.Frame_R, image=self.Regis, bd=0, relief=FLAT, bg='#F2F2F2', command=self.Envio_Registro).place(x=235, y=330, height=67, width=207)

#---------------------------------------------Registrar Empresa-----------------------------------------------------
	def Envio_Registro(self):
		#Datos a ver si son Falsos o Verdaderos
		C_NR = False
		C_RIF = False
		C_DR = False
		C_CR = False

		if self.nombre_regisro.get() != '': #Ver si el entry de nombre de la empresa esta vacio
			C_NR = True
		else:
			M_NR = Label(self.Frame_R, text='(Rellena el recuadro)', fg='#BE1622').place(x=127, y=150)

		if self.RIF.get() != '': #Ver si el entry del RIF esta vacio
			C_RIF = True
		else:
			Label(self.Frame_R, text='(Rellena el recuadro)', fg='#BE1622').place(x=436, y=150)

		
		if self.direccion_registro.get() != '': #Ver si el entry de la direccion esta vacio
			C_DR = True
		else:
			Label(self.Frame_R, text='(Rellena el recuadro)', fg='#BE1622').place(x=127, y=290)


		if self.contacto_registro.get() != '': #Ver si el entry de el numero de contacto esta vacio
			C_CR = True
		else:
			Label(self.Frame_R, text='(Rellena el recuadro)', fg='#BE1622').place(x=436, y=290)


		if (C_NR) and (C_RIF) and (C_DR) and (C_CR): #Comprobar si todo esta en orden 
			self.Entry_Empresa()

			self.Update_Register()

			self.Check_Registro()

#----------------------------------------------Inico de la App------------------------------------------------------
	def Inicio_APP(self):
		Label(self.root, bg='black',height=1, width=900).place(x=0, y=100)

		self.Frame_B = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_B.place(x=0, y=101)

		#Titulo y presentacion de la empresa
		self.Exit_Empresa()
		self.Empresa['text'] = self.nombre_empresa
		self.dato_rif['text'] = self.nombre_rif


		#Boton Comprar
		Button(self.Frame_B, image=self.compra, bg='#F2F2F2', relief=FLAT, bd=0, command=self.B_Gastos).place(x=117, y=58)
		Label(self.Frame_B, text='Gastos', font=('Nexa Rust Slab Black 01', 15, 'bold'), bg='#F2F2F2').place(x=135, y=170)

		#Boton Inventario
		Button(self.Frame_B, image=self.inventario, bg='#F2F2F2', relief=FLAT, bd=0, command=self.B_Inventario).place(x=395, y=58)
		Label(self.Frame_B, text='Inventario', font=('Nexa Rust Slab Black 01', 15, 'bold'), bg='#F2F2F2').place(x=401, y=170)

		#Boton Ventas
		Button(self.Frame_B, image=self.venta, bg='#F2F2F2', relief=FLAT, bd=0, command=self.B_Vender).place(x=670, y=58)
		Label(self.Frame_B, text='Ventas', font=('Nexa Rust Slab Black 01', 15, 'bold'), bg='#F2F2F2').place(x=692, y=170)

		#Boton Empleados
		Button(self.Frame_B, image=self.empleados, bg='#F2F2F2', relief=FLAT, bd=0, command=self.B_Empleados).place(x=117, y=250)
		Label(self.Frame_B, text='Empleados', font=('Nexa Rust Slab Black 01', 15, 'bold'), bg='#F2F2F2').place(x=118, y=364)

		#Boton Distribuidoras
		Button(self.Frame_B, image=self.Distri, bg='#F2F2F2', relief=FLAT, bd=0, command=self.B_Distribuidores).place(x=395, y=250)
		Label(self.Frame_B, text='Distribuidores', font=('Nexa Rust Slab Black 01', 15, 'bold'), bg='#F2F2F2').place(x=383, y=364)

		#Boton Estadisticas
		Button(self.Frame_B, image=self.Estd, bg='#F2F2F2', relief=FLAT, bd=0, command=self.B_Estadisticas).place(x=670, y=250)
		Label(self.Frame_B, text='Estadisticas', font=('Nexa Rust Slab Black 01', 15, 'bold'), bg='#F2F2F2').place(x=666, y=364)

#-----------------------------------------------Boton Gastos-------------------------------------------------------
	def B_Gastos(self):
		self.Boton_Configuracion.config(state='disabled')

		#Frame Principal
		self.Frame_boton_Gastos = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_boton_Gastos.place(x=0, y=101)

		#Frame de Botones
		ajuste_botones = Frame(self.Frame_boton_Gastos, bg='#d7d7d7', height=412, width=240)
		ajuste_botones.place(x=0, y=0)

		#Boton de Back
		Button(ajuste_botones, image=self.Image_back, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Destroy_Gastos).place(x=10, y=10)

		#Boton de Agregar
		self.Boton_Agregar_C = Button(ajuste_botones, image=self.mas, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Ventana_Agregar_Gastos)
		self.Boton_Agregar_C.place(x=80, y=40)
		Label(ajuste_botones, text='Agregar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=83, y=113)

		#Boton de Modificar
		self.Boton_Modificar_C = Button(ajuste_botones, image=self.Lapiz, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Ventana_Modificar_Gastos)
		self.Boton_Modificar_C.place(x=80, y=160)
		Label(ajuste_botones, text='Modificar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=77, y=234)

		#Boton de Eliminar
		self.Boton_Eliminar_C = Button(ajuste_botones, image=self.cancelar, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Eliminar_Inventario)
		self.Boton_Eliminar_C.place(x=80, y=280)
		Label(ajuste_botones, text='Eliminar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=82, y=353)

		#Mensaje de de Advertencia
		self.Mensaje_Gastos = Label(ajuste_botones, text='', bg='#d7d7d7', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='#e94548')
		self.Mensaje_Gastos.place(x=45, y=385)

		#Titulo del Arbol
		Label(self.Frame_boton_Gastos, text='Gastos', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 12, 'bold'), fg='red').place(x=520,y=6)

		#--------------Arbol Principal---------------------------
		self.ArbolGastos = ttk.Treeview(self.Frame_boton_Gastos, columns=('col1', 'col2', 'col3', 'col4', 'col5'), height=10)

		self.ArbolGastos.column('#0', width=1, anchor=W)
		self.ArbolGastos.column('col1', width=150, anchor=W)
		self.ArbolGastos.column('col2', width=50, anchor=E)
		self.ArbolGastos.column('col3', width=50, anchor=CENTER)
		self.ArbolGastos.column('col4', width=50, anchor=E)
		self.ArbolGastos.column('col5', width=90, anchor=CENTER)

		self.ArbolGastos.heading('#0', text='ID')
		self.ArbolGastos.heading('col1', text='Pagos/Servicios', anchor=CENTER)
		self.ArbolGastos.heading('col2', text='Precio', anchor=CENTER)
		self.ArbolGastos.heading('col3', text='Cantidad', anchor=CENTER)
		self.ArbolGastos.heading('col4', text='Precio C.U', anchor=CENTER)
		self.ArbolGastos.heading('col5', text='Fecha', anchor=CENTER)

		self.ArbolGastos.place(x=250, y=30, width=640, height=350)

		self.ArbolGastos.tag_configure('bg', background='#F2F2F2')



		#--------------Arbol Precio---------------------------
		Label(self.Frame_boton_Gastos, text='Precio Total:', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='Black').place(x=760,y=384)

		self.Precio_Arbol_Gastos = ttk.Treeview(self.Frame_boton_Gastos, height=10)

		self.Precio_Arbol_Gastos.column('#0', width=1)

		self.Precio_Arbol_Gastos.place(x=839, y=385, width=50, height=20)


		#--------------Arbol Cantidad--------------------------
		Label(self.Frame_boton_Gastos, text='Cantidad Total:', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='Black').place(x=247,y=384)

		self.Cantidad_Arbol_Gastos = ttk.Treeview(self.Frame_boton_Gastos, height=10)

		self.Cantidad_Arbol_Gastos.column('#0', width=1)

		self.Cantidad_Arbol_Gastos.place(x=340, y=385, width=50, height=20)
		
		self.Precio_Gastos()
		
		self.Update_Arbol_Gastos()

		self.Precio_Total_Gastos()

	#Destruir Framme
	def Destroy_Gastos(self):
		self.Frame_boton_Gastos.destroy()
		self.Boton_Configuracion.config(state='normal')


	#Limpiar y Actualizar los datos del Arbol
	def Update_Arbol_Gastos(self):
		#Fecha para Agregar al Arbol
		today = date.today()
		d1 = today.strftime("%d/%m/%Y")

		#Limpiando Arbol
		for x in self.ArbolGastos.get_children():
			self.ArbolGastos.delete(x)

		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute(f"SELECT * FROM Gastos WHERE Fecha = '{d1}';")
		
		for x in data:
			self.ArbolGastos.insert('', END, text=x[0], values=(x[1], x[2], x[3], x[4], x[5]))
			
		self.Close_Data()


	#Venatana para agregar productos
	def Ventana_Agregar_Gastos(self):
		self.Mensaje_Gastos['text'] = ''

		self.Boton_Agregar_C.config(state='disabled')

		self.Boton_Modificar_C.config(state='disabled')	

		self.Boton_Eliminar_C.config(state='disabled')

		self.ventana_Gastos = Frame(self.Frame_boton_Gastos, width=300, height=250, bg='#d7d7d7')
		self.ventana_Gastos.place(x=320, y=60)

		#Marco de ventana
		Label(self.ventana_Gastos, bd=1, height=250, bg='black').place(x=-3,y=0)
		Label(self.ventana_Gastos, bd=1, width=300, bg='black').place(x=0,y=-17)
		Label(self.ventana_Gastos, bd=1, height=300, bg='black').place(x=299,y=0)
		Label(self.ventana_Gastos, bd=1, width=300, bg='black').place(x=0,y=248)

		#Entrada de Datos
		Label(self.ventana_Gastos, text='Pagos/Servicios', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=92, y=18)
		self.Entreda_producto_Gastos = Entry(self.ventana_Gastos)
		self.Entreda_producto_Gastos.place(x=25, y=40, height=25, width=250)
		self.Entreda_producto_Gastos.focus()
		self.Entreda_producto_Gastos.bind('<Return>', lambda _:self.Entreda_precio_Gastos.focus())


		#Entrada de Datos
		Label(self.ventana_Gastos, text='Precio por Unidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=80, y=77)
		self.Entreda_precio_Gastos = Entry(self.ventana_Gastos)
		self.Entreda_precio_Gastos.place(x=25, y=100, height=25, width=250)
		self.Entreda_precio_Gastos.bind('<Return>', lambda _:self.Entreda_cantidad_Gastos.focus())


		#Entrada de Datos
		Label(self.ventana_Gastos, text='Cantidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=112, y=135)
		self.Entreda_cantidad_Gastos = Entry(self.ventana_Gastos)
		self.Entreda_cantidad_Gastos.place(x=25, y=158, height=25, width=250)
		self.Entreda_cantidad_Gastos.bind('<Return>', lambda _:self.Mandar_Gastos())

		


		#Boton Gastos
		Button(self.ventana_Gastos, text='Gastos', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Gastos).place(x=35, y=210)
		
		#Boton Cancelar
		Button(self.ventana_Gastos, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_CA).place(x=200, y=210)
	

	#Almacenar los datos en la base de datos
	def Mandar_Gastos(self):
		if self.Entreda_cantidad_Gastos.get() != '' and self.Entreda_producto_Gastos.get() != '' and self.Entreda_precio_Gastos.get() != '':

			self.Boton_Agregar_C.config(state='normal')

			self.Boton_Modificar_C.config(state='normal')	

			self.Boton_Eliminar_C.config(state='normal')
			
			#Fecha para Agregar al Arbol
			today = date.today()

			d1 = today.strftime("%d/%m/%Y")

			try:
				self.conn = sql.connect(self.__DB)		

				cursor = self.conn.cursor()
					
				cursor.execute(f"INSERT INTO Gastos (Gasto, PrecioU, Cantidad, Fecha) VALUES ('{self.Entreda_producto_Gastos.get()}',{self.Entreda_precio_Gastos.get()},{self.Entreda_cantidad_Gastos.get()},'{d1}')")
				self.conn.commit()
				self.Close_Data()

				self.Precio_Gastos()
				self.Update_Arbol_Gastos()
				self.Precio_Total_Gastos()

				self.ventana_Gastos.destroy()

			except:
				self.Close_Data()

				Label(self.ventana_Gastos, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=125)
				
				Label(self.ventana_Gastos, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=184)


	#Activar botones
	def Activar_Botones_CA(self):
		
		self.Boton_Agregar_C.config(state='normal')

		self.Boton_Modificar_C.config(state='normal')	

		self.Boton_Eliminar_C.config(state='normal')

		self.ventana_Gastos.destroy()

	#Activar botones
	def Activar_Botones_CB(self):
		self.Boton_Agregar_C.config(state='normal')

		self.Boton_Modificar_C.config(state='normal')	

		self.Boton_Eliminar_C.config(state='normal')

		self.ventana_Modificar_Gastos.destroy()


	#Agregar el Precio Cantidad x Unidad
	def Precio_Gastos(self):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		cursor.execute(f"UPDATE Gastos SET PrecioT = PrecioU * Cantidad")
				
		self.conn.commit()

		self.Close_Data()


	#Actualizar El precio Total
	def Precio_Total_Gastos(self):
		#Fecha para Agregar al Arbol
		today = date.today()
		d1 = today.strftime("%d/%m/%Y")

		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute(f"SELECT sum(Cantidad), sum(PrecioT) FROM Gastos WHERE Fecha = '{d1}'")
		
		for x in data:
			self.Cantidad_Arbol_Gastos.heading('#0',text=f'{x[0]}', anchor=E)
			self.Precio_Arbol_Gastos.heading('#0',text=f'{x[1]}', anchor=E)

			self.Perdida = x[1]
			
		self.Close_Data()


	#Ventana de Modificar productos
	def Ventana_Modificar_Gastos(self):
		select=self.ArbolGastos.focus()

		row = self.ArbolGastos.item(select, 'values')

		if row != '':
			self.Boton_Agregar_C.config(state='disabled')

			self.Boton_Modificar_C.config(state='disabled')	

			self.Boton_Eliminar_C.config(state='disabled')

			self.Mensaje_Gastos['text'] = ''

			self.ventana_Modificar_Gastos = Frame(self.Frame_boton_Gastos, width=300, height=250, bg='#d7d7d7')
			self.ventana_Modificar_Gastos.place(x=320, y=60)

			#Marco de ventana
			Label(self.ventana_Modificar_Gastos, bd=1, height=250, bg='black').place(x=-3,y=0)
			Label(self.ventana_Modificar_Gastos, bd=1, width=300, bg='black').place(x=0,y=-17)
			Label(self.ventana_Modificar_Gastos, bd=1, height=300, bg='black').place(x=299,y=0)
			Label(self.ventana_Modificar_Gastos, bd=1, width=300, bg='black').place(x=0,y=248)

			#Entrada de Datos
			Label(self.ventana_Modificar_Gastos, text='Pagos/Servicios', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=92, y=18)
			self.Entreda_producto_Gastos_M = Entry(self.ventana_Modificar_Gastos)
			self.Entreda_producto_Gastos_M.place(x=25, y=40, height=25, width=250)
			self.Entreda_producto_Gastos_M.focus()
			self.Entreda_producto_Gastos_M.insert(END, row[0])
			self.Entreda_producto_Gastos_M.bind('<Return>', lambda _:self.Entreda_precio_Gastos_M.focus())


			#Entrada de Datos
			Label(self.ventana_Modificar_Gastos, text='Precio por Unidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=80, y=77)
			self.Entreda_precio_Gastos_M = Entry(self.ventana_Modificar_Gastos)
			self.Entreda_precio_Gastos_M.place(x=25, y=100, height=25, width=250)
			self.Entreda_precio_Gastos_M.insert(END, row[1])
			self.Entreda_precio_Gastos_M.bind('<Return>', lambda _:self.Entreda_cantidad_Gastos_M.focus())


			#Entrada de Datos
			Label(self.ventana_Modificar_Gastos, text='Cantidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=112, y=135)
			self.Entreda_cantidad_Gastos_M = Entry(self.ventana_Modificar_Gastos)
			self.Entreda_cantidad_Gastos_M.place(x=25, y=158, height=25, width=250)
			self.Entreda_cantidad_Gastos_M.insert(END, row[2])
			self.Entreda_cantidad_Gastos_M.bind('<Return>', lambda _:self.Mandar_Modificar_Gastos())


			#Boton Gastosr
			Button(self.ventana_Modificar_Gastos, text='Modificar', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Modificar_Gastos).place(x=35, y=210)
			
			#Boton Cancelar
			Button(self.ventana_Modificar_Gastos, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_CB).place(x=200, y=210)
		

		else:
			self.Mensaje_Gastos['text'] = 'Selecciones un elemento'


	#Actualizar los datos de la base de datos
	def Mandar_Modificar_Gastos(self):
		select=self.ArbolGastos.focus()

		row = self.ArbolGastos.item(select, 'text')

		

		if self.Entreda_cantidad_Gastos_M.get() != '' and self.Entreda_producto_Gastos_M.get() != '' and self.Entreda_precio_Gastos_M.get() != '':

			self.Boton_Agregar_C.config(state='normal')

			self.Boton_Modificar_C.config(state='normal')	

			self.Boton_Eliminar_C.config(state='normal')
			
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()


			try:
				cursor.execute(f"UPDATE Gastos SET Gasto='{self.Entreda_producto_Gastos_M.get()}', PrecioU={self.Entreda_precio_Gastos_M.get()}, Cantidad={self.Entreda_cantidad_Gastos_M.get()} WHERE ID={row}")
				
				self.conn.commit()
					
				self.Precio_Gastos()

				self.Update_Arbol_Gastos()

				self.Precio_Total_Gastos()

				self.ventana_Modificar_Gastos.destroy()

				self.Close_Data()

			except:
				self.Close_Data()

				Label(self.ventana_Modificar_Gastos, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=125)
				
				Label(self.ventana_Modificar_Gastos, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=184)


	#Eliminar datos de la base de datos
	def Eliminar_Inventario(self):
		select=self.ArbolGastos.focus()

		row = self.ArbolGastos.item(select, 'text')

		if row != '':
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			cursor.execute(f"DELETE FROM Gastos WHERE ID = {row}")
					
			self.conn.commit()

			self.Close_Data()

			self.Update_Arbol_Gastos()

			self.Precio_Total_Gastos()

			self.Mensaje_Gastos['text'] = ''


		else:
			self.Mensaje_Gastos['text'] = 'Selecciones un elemento'

#----------------------------------------------Boton Inventario-----------------------------------------------------
	#Ventana de Invetario
	def B_Inventario(self):
		self.Boton_Configuracion.config(state='disabled')

		#Frame Principal
		self.Frame_boton_inventario = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_boton_inventario.place(x=0, y=101)

		#Frame de Botones
		ajuste_botones = Frame(self.Frame_boton_inventario, bg='#d7d7d7', height=412, width=240)
		ajuste_botones.place(x=0, y=0)

		#Boton de Back
		Button(ajuste_botones, image=self.Image_back, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Destroy_Inventario).place(x=10, y=10)

		#Boton de Agregar
		self.Boton_Agregar_i = Button(ajuste_botones, image=self.mas, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Ventana_Agregar_Iventario)
		self.Boton_Agregar_i.place(x=80, y=40)
		Label(ajuste_botones, text='Agregar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=83, y=113)

		#Boton de Modificar
		self.Boton_Modificar_i = Button(ajuste_botones, image=self.Lapiz, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.ventana_Modificar_Inventario)
		self.Boton_Modificar_i.place(x=80, y=160)
		Label(ajuste_botones, text='Modificar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=77, y=234)

		#Boton de Eliminar
		self.Boton_Eliminar_i = Button(ajuste_botones, image=self.cancelar, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Eliminar_Compra)
		self.Boton_Eliminar_i.place(x=80, y=280)
		Label(ajuste_botones, text='Eliminar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=82, y=353)

		#Mensaje de de Advertencia
		self.Mensaje_Inventario = Label(ajuste_botones, text='', bg='#d7d7d7', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='#e94548')
		self.Mensaje_Inventario.place(x=45, y=385)

		#Titulo del Arbol
		Label(self.Frame_boton_inventario, text='Inventario', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 12, 'bold'), fg='#c2915b').place(x=520,y=6)

		#--------------Arbol Principal---------------------------
		self.Arbolinventario = ttk.Treeview(self.Frame_boton_inventario, columns=('col1', 'col2', 'col3', 'col4', 'col5'), height=10)

		self.Arbolinventario.column('#0', width=1, anchor=W)
		self.Arbolinventario.column('col1', width=150, anchor=W)
		self.Arbolinventario.column('col2', width=50, anchor=E)
		self.Arbolinventario.column('col3', width=50, anchor=CENTER)
		self.Arbolinventario.column('col4', width=50, anchor=E)
		self.Arbolinventario.column('col5', width=90, anchor=CENTER)

		self.Arbolinventario.heading('#0', text='ID')
		self.Arbolinventario.heading('col1', text='Producto', anchor=CENTER)
		self.Arbolinventario.heading('col2', text='Precio U.', anchor=CENTER)
		self.Arbolinventario.heading('col3', text='Mercancia T.', anchor=CENTER)
		self.Arbolinventario.heading('col4', text='Precio M.U', anchor=CENTER)
		self.Arbolinventario.heading('col5', text='Fecha', anchor=CENTER)

		self.Arbolinventario.place(x=250, y=30, width=640, height=350)

		self.Arbolinventario.tag_configure('bg', background='#F2F2F2')



		#--------------Arbol Precio---------------------------
		Label(self.Frame_boton_inventario, text='Precio Total:', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='Black').place(x=760,y=384)

		self.Precio_Arbol_Inventario = ttk.Treeview(self.Frame_boton_inventario, height=10)

		self.Precio_Arbol_Inventario.column('#0', width=1)

		self.Precio_Arbol_Inventario.place(x=839, y=385, width=50, height=20)


		#--------------Arbol Cantidad--------------------------
		Label(self.Frame_boton_inventario, text='Mercancia Total:', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='Black').place(x=247,y=384)

		self.Cantidad_Arbol_Inventario = ttk.Treeview(self.Frame_boton_inventario, height=10)

		self.Cantidad_Arbol_Inventario.column('#0', width=1)

		self.Cantidad_Arbol_Inventario.place(x=345, y=385, width=50, height=20)
		
		self.Precio_Inventario()
		
		self.Update_Arbol_Inventario()

		self.Precio_Total_Inventario()

	#Destruir Frame
	def Destroy_Inventario(self):
		self.Frame_boton_inventario.destroy()
		self.Boton_Configuracion.config(state='normal')


	#Limpiar y Actualizar los datos del Arbol
	def Update_Arbol_Inventario(self):
		
		#Limpiando Arbol
		for x in self.Arbolinventario.get_children():
			self.Arbolinventario.delete(x)

		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute(f"SELECT * FROM Inventario;")
		
		for x in data:
			self.Arbolinventario.insert('', END, text=x[0], values=(x[1], x[2], x[3], x[4], x[5]))
			
		self.Close_Data()


	#Agregar el Precio Cantidad x Unidad
	def Precio_Inventario(self):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		cursor.execute(f"UPDATE Inventario SET PrecioT = PrecioU * Cantidad")
				
		self.conn.commit()

		self.Close_Data()


	#Actualizar El precio Total
	def Precio_Total_Inventario(self):
		#Fecha para Agregar al Arbol
		today = date.today()
		d1 = today.strftime("%d/%m/%Y")

		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute(f"SELECT sum(Cantidad), sum(PrecioT) FROM Inventario WHERE Fecha ='{d1}'")
		
		for x in data:
			self.Cantidad_Arbol_Inventario.heading('#0',text=f'{x[0]}', anchor=E)
			self.Precio_Arbol_Inventario.heading('#0',text=f'{x[1]}', anchor=E)
			
		self.Close_Data()


	#Ventana de Agregar Inventario
	def Ventana_Agregar_Iventario(self):
		self.Mensaje_Inventario['text'] = ''

		self.Boton_Agregar_i.config(state='disabled')

		self.Boton_Modificar_i.config(state='disabled')	

		self.Boton_Eliminar_i.config(state='disabled')

		self.ventana_inventario = Frame(self.Frame_boton_inventario, width=300, height=250, bg='#d7d7d7')
		self.ventana_inventario.place(x=320, y=60)

		#Marco de ventana
		Label(self.ventana_inventario, bd=1, height=250, bg='black').place(x=-3,y=0)
		Label(self.ventana_inventario, bd=1, width=300, bg='black').place(x=0,y=-17)
		Label(self.ventana_inventario, bd=1, height=300, bg='black').place(x=299,y=0)
		Label(self.ventana_inventario, bd=1, width=300, bg='black').place(x=0,y=248)

		#Entrada de Datos
		Label(self.ventana_inventario, text='Producto', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=111, y=18)
		self.Entreda_producto_inventario = Entry(self.ventana_inventario)
		self.Entreda_producto_inventario.place(x=25, y=40, height=25, width=250)
		self.Entreda_producto_inventario.focus()
		self.Entreda_producto_inventario.bind('<Return>', lambda _:self.Entreda_precio_inventario.focus())


		#Entrada de Datos
		Label(self.ventana_inventario, text='Precio por Unidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=80, y=77)
		self.Entreda_precio_inventario = Entry(self.ventana_inventario)
		self.Entreda_precio_inventario.place(x=25, y=100, height=25, width=250)
		self.Entreda_precio_inventario.bind('<Return>', lambda _:self.Entreda_cantidad_inventario.focus())


		#Entrada de Datos
		Label(self.ventana_inventario, text='Cantidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=112, y=135)
		self.Entreda_cantidad_inventario = Entry(self.ventana_inventario)
		self.Entreda_cantidad_inventario.place(x=25, y=158, height=25, width=250)
		self.Entreda_cantidad_inventario.bind('<Return>', lambda _:self.Mandar_Inventario())


		#Boton comprar
		Button(self.ventana_inventario, text='Agregar', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Inventario).place(x=35, y=210)
		
		#Boton Cancelar
		Button(self.ventana_inventario, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_IA).place(x=200, y=210)
	

	#Almacenar los datos en la base de datos
	def Mandar_Inventario(self):
		if self.Entreda_cantidad_inventario.get() != '' and self.Entreda_producto_inventario.get() != '' and self.Entreda_precio_inventario.get() != '':

			self.Boton_Agregar_i.config(state='normal')

			self.Boton_Modificar_i.config(state='normal')	

			self.Boton_Eliminar_i.config(state='normal')

			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()
			
			#Fecha para Agregar al Arbol
			today = date.today()
			d1 = today.strftime("%d/%m/%Y")

			try:
				cursor.execute(f"INSERT INTO Inventario (Producto, PrecioU, Cantidad, Fecha) VALUES ('{self.Entreda_producto_inventario.get()}',{self.Entreda_precio_inventario.get()},{self.Entreda_cantidad_inventario.get()},'{d1}')")

				self.conn.commit()

				self.Close_Data()

				self.Precio_Inventario()

				self.Update_Arbol_Inventario()

				self.Precio_Total_Inventario()

				self.ventana_inventario.destroy()

			except:
				self.Close_Data()

				Label(self.ventana_inventario, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=125)
				
				Label(self.ventana_inventario, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=184)


	#Activar botones
	def Activar_Botones_IA(self):
		
		self.Boton_Agregar_i.config(state='normal')

		self.Boton_Modificar_i.config(state='normal')	

		self.Boton_Eliminar_i.config(state='normal')

		self.ventana_inventario.destroy()

	#Activar botones
	def Activar_Botones_IB(self):
		self.Boton_Agregar_i.config(state='normal')

		self.Boton_Modificar_i.config(state='normal')	

		self.Boton_Eliminar_i.config(state='normal')

		self.ventana_Modificar_Inventario.destroy()

	#Ventana de Modificar
	def ventana_Modificar_Inventario(self):
		select=self.Arbolinventario.focus()

		row = self.Arbolinventario.item(select, 'values')

		if row != '':
			self.Boton_Agregar_i.config(state='disabled')

			self.Boton_Modificar_i.config(state='disabled')	

			self.Boton_Eliminar_i.config(state='disabled')

			self.Mensaje_Inventario['text'] = ''

			self.ventana_Modificar_Inventario = Frame(self.Frame_boton_inventario, width=300, height=250, bg='#d7d7d7')
			self.ventana_Modificar_Inventario.place(x=320, y=60)

			#Marco de ventana
			Label(self.ventana_Modificar_Inventario, bd=1, height=250, bg='black').place(x=-3,y=0)
			Label(self.ventana_Modificar_Inventario, bd=1, width=300, bg='black').place(x=0,y=-17)
			Label(self.ventana_Modificar_Inventario, bd=1, height=300, bg='black').place(x=299,y=0)
			Label(self.ventana_Modificar_Inventario, bd=1, width=300, bg='black').place(x=0,y=248)

			#Entrada de Datos
			Label(self.ventana_Modificar_Inventario, text='Producto', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=111, y=18)
			self.Entreda_producto_inventario_M = Entry(self.ventana_Modificar_Inventario)
			self.Entreda_producto_inventario_M.place(x=25, y=40, height=25, width=250)
			self.Entreda_producto_inventario_M.focus()
			self.Entreda_producto_inventario_M.insert(END, row[0])
			self.Entreda_producto_inventario_M.bind('<Return>', lambda _:self.Entreda_precio_inventario_M.focus())


			#Entrada de Datos
			Label(self.ventana_Modificar_Inventario, text='Precio por Unidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=80, y=77)
			self.Entreda_precio_inventario_M = Entry(self.ventana_Modificar_Inventario)
			self.Entreda_precio_inventario_M.place(x=25, y=100, height=25, width=250)
			self.Entreda_precio_inventario_M.insert(END, row[1])
			self.Entreda_precio_inventario_M.bind('<Return>', lambda _:self.Entreda_cantidad_inventario_M.focus())


			#Entrada de Datos
			Label(self.ventana_Modificar_Inventario, text='Cantidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=112, y=135)
			self.Entreda_cantidad_inventario_M = Entry(self.ventana_Modificar_Inventario)
			self.Entreda_cantidad_inventario_M.place(x=25, y=158, height=25, width=250)
			self.Entreda_cantidad_inventario_M.insert(END, row[2])
			self.Entreda_cantidad_inventario_M.bind('<Return>', lambda _:self.Mandar_Modificar_Inventario())


			#Boton comprar
			Button(self.ventana_Modificar_Inventario, text='Modificar', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Modificar_Inventario).place(x=35, y=210)
			
			#Boton Cancelar
			Button(self.ventana_Modificar_Inventario, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_IB).place(x=200, y=210)
		

		else:
			self.Mensaje_Inventario['text'] = 'Selecciones un elemento'


	#Actualizar los datos de la base de datos
	def Mandar_Modificar_Inventario(self):
		select=self.Arbolinventario.focus()

		row = self.Arbolinventario.item(select, 'text')

		

		if self.Entreda_cantidad_inventario_M.get() != '' and self.Entreda_producto_inventario_M.get() != '' and self.Entreda_precio_inventario_M.get() != '':

			self.Boton_Agregar_i.config(state='normal')

			self.Boton_Modificar_i.config(state='normal')	

			self.Boton_Eliminar_i.config(state='normal')
			
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()


			try:
				cursor.execute(f"UPDATE Inventario SET Producto='{self.Entreda_producto_inventario_M.get()}', PrecioU={self.Entreda_precio_inventario_M.get()}, Cantidad={self.Entreda_cantidad_inventario_M.get()} WHERE ID={row}")
				
				self.conn.commit()
					
				self.Precio_Inventario()

				self.Update_Arbol_Inventario()

				self.Precio_Total_Inventario()

				self.ventana_Modificar_Inventario.destroy()

				self.Close_Data()

			except:
				self.Close_Data()

				Label(self.ventana_Modificar_Inventario, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=125)
				
				Label(self.ventana_Modificar_Inventario, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=184)


	#Eliminar datos de la base de datos
	def Eliminar_Compra(self):
		select=self.Arbolinventario.focus()

		row = self.Arbolinventario.item(select, 'text')

		if row != '':
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			cursor.execute(f"DELETE FROM Inventario WHERE ID = {row}")
					
			self.conn.commit()

			self.Close_Data()

			self.Update_Arbol_Inventario()

			self.Precio_Total_Inventario()

			self.Mensaje_Inventario['text'] = ''


		else:
			self.Mensaje_Inventario['text'] = 'Selecciones un elemento'

#------------------------------------------------Boton vender-------------------------------------------------------
	def B_Vender(self):
		self.Boton_Configuracion.config(state='disabled')

		self.Frame_boton_venta = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_boton_venta.place(x=0, y=101)

		ajuste_botones = Frame(self.Frame_boton_venta, bg='#d7d7d7', height=412, width=240)
		ajuste_botones.place(x=0, y=0)
		
		#Boton Back
		Button(ajuste_botones, image=self.Image_back, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Destroy_Ventas).place(x=10, y=10)

		#Boton Agragar Venta
		self.Boton_Agregar_V = Button(ajuste_botones, image=self.mas, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Ventana_Agregar_Venta)
		self.Boton_Agregar_V.place(x=80, y=40)
		Label(ajuste_botones, text='Agregar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=83, y=113)

		#Boton Modificar Venta
		self.Boton_Modificar_V = Button(ajuste_botones, image=self.Lapiz, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Ventana_Modificar_Vender)
		self.Boton_Modificar_V.place(x=80, y=160)
		Label(ajuste_botones, text='Modificar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=77, y=234)

		#boton Eliminar Venta
		self.Boton_Eliminar_V = Button(ajuste_botones, image=self.cancelar, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Eliminar_Venta)
		self.Boton_Eliminar_V.place(x=80, y=280)
		Label(ajuste_botones, text='Eliminar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=82, y=353)

		Label(self.Frame_boton_venta, text='Ventas', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 12, 'bold'), fg='#e94548').place(x=535,y=6)

		#Mensaje de de Advertencia
		self.Mensaje_Venta = Label(ajuste_botones, text='', bg='#d7d7d7', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='#e94548')
		self.Mensaje_Venta.place(x=45, y=385)

		self.ArbolVenta = ttk.Treeview(self.Frame_boton_venta, columns=('col1', 'col2', 'col3', 'col4', 'col5'), height=10)

		self.ArbolVenta.column('#0', width=1, anchor=W)
		self.ArbolVenta.column('col1', width=150, anchor=W)
		self.ArbolVenta.column('col2', width=50, anchor=E)
		self.ArbolVenta.column('col3', width=50, anchor=CENTER)
		self.ArbolVenta.column('col4', width=50, anchor=E)
		self.ArbolVenta.column('col5', width=90, anchor=CENTER)

		self.ArbolVenta.heading('#0', text='ID')
		self.ArbolVenta.heading('col1', text='Producto', anchor=CENTER)
		self.ArbolVenta.heading('col2', text='Precio V.', anchor=CENTER)
		self.ArbolVenta.heading('col3', text='Cantidad', anchor=CENTER)
		self.ArbolVenta.heading('col4', text='Precio C.U', anchor=CENTER)
		self.ArbolVenta.heading('col5', text='Fecha', anchor=CENTER)

		self.ArbolVenta.place(x=250, y=30, width=640, height=350)

		self.ArbolVenta.tag_configure('bg', background='#F2F2F2')

		
		#--------------Arbol Precio---------------------------
		Label(self.Frame_boton_venta, text='Precio Total:', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='Black').place(x=760,y=384)

		self.Precio_Arbol_Venta = ttk.Treeview(self.Frame_boton_venta, height=10)

		self.Precio_Arbol_Venta.column('#0', width=1)

		self.Precio_Arbol_Venta.place(x=839, y=385, width=50, height=20)


		#--------------Arbol Cantidad--------------------------
		Label(self.Frame_boton_venta, text='Cantidad Total:', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='Black').place(x=247,y=384)

		self.Cantidad_Arbol_Venta = ttk.Treeview(self.Frame_boton_venta, height=10)

		self.Cantidad_Arbol_Venta.column('#0', width=1)

		self.Cantidad_Arbol_Venta.place(x=340, y=385, width=50, height=20)

		self.Precio_Vender()

		self.Update_Arbol_Venta()

		self.Precio_Total_Vender()

	#Destruir Frame
	def Destroy_Ventas(self):
		self.Frame_boton_venta.destroy()
		self.Boton_Configuracion.config(state='normal')


	#Limpiar y Actualizar los datos del Arbol
	def Update_Arbol_Venta(self):
		#Fecha para Agregar al Arbol
		today = date.today()
		d1 = today.strftime("%d/%m/%Y")

		#Limpiando Arbol
		for x in self.ArbolVenta.get_children():
			self.ArbolVenta.delete(x)

		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute(f"SELECT * FROM Venta WHERE Fecha = '{d1}';")
		
		for x in data:
			self.ArbolVenta.insert('', END, text=x[0], values=(x[1], x[2], x[3], x[4], x[5]))
			
		self.Close_Data()


	#Venatana para agregar productos
	def Ventana_Agregar_Venta(self):
		self.Mensaje_Venta['text'] = ''

		self.Boton_Agregar_V.config(state='disabled')	
		self.Boton_Modificar_V.config(state='disabled')
		self.Boton_Eliminar_V.config(state='disabled')


		self.ventana_venta = Frame(self.Frame_boton_venta, width=300, height=250, bg='#d7d7d7')
		self.ventana_venta.place(x=320, y=60)

		#Marco de ventana
		Label(self.ventana_venta, bd=1, height=250, bg='black').place(x=-3,y=0)
		Label(self.ventana_venta, bd=1, width=300, bg='black').place(x=0,y=-17)
		Label(self.ventana_venta, bd=1, height=300, bg='black').place(x=299,y=0)
		Label(self.ventana_venta, bd=1, width=300, bg='black').place(x=0,y=248)

		#Entrada de Datos
		Label(self.ventana_venta, text='Producto', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=111, y=18)
		self.Entreda_producto_venta = Entry(self.ventana_venta)
		self.Entreda_producto_venta.place(x=25, y=40, height=25, width=250)
		self.Entreda_producto_venta.focus()
		self.Entreda_producto_venta.bind('<Return>', lambda _:self.Entreda_precio_venta.focus())


		#Entrada de Datos
		Label(self.ventana_venta, text='Precio por Unidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=80, y=77)
		self.Entreda_precio_venta = Entry(self.ventana_venta)
		self.Entreda_precio_venta.place(x=25, y=100, height=25, width=250)
		self.Entreda_precio_venta.bind('<Return>', lambda _:self.Entreda_cantidad_venta.focus())


		#Entrada de Datos
		Label(self.ventana_venta, text='Cantidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=112, y=135)
		self.Entreda_cantidad_venta = Entry(self.ventana_venta)
		self.Entreda_cantidad_venta.place(x=25, y=158, height=25, width=250)
		self.Entreda_cantidad_venta.bind('<Return>', lambda _:self.Mandar_Vender())


		#Boton comprar
		Button(self.ventana_venta, text='Vender', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Vender).place(x=35, y=210)
		
		#Boton Cancelar
		Button(self.ventana_venta, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_VA).place(x=200, y=210)
	

	#Activa los botones desahabilitado
	def Activar_Botones_VA(self):
		
		self.Boton_Modificar_V.config(state='normal')

		self.Boton_Agregar_V.config(state='normal')	

		self.Boton_Eliminar_V.config(state='normal')

		self.ventana_venta.destroy()

	def Activar_Botones_VB(self):
		self.Boton_Modificar_V.config(state='normal')

		self.Boton_Agregar_V.config(state='normal')	

		self.Boton_Eliminar_V.config(state='normal')

		self.ventana_Modificar_venta.destroy()

	#Almacenar los datos en la base de datos
	def Mandar_Vender(self):
		if self.Entreda_cantidad_venta.get() != '' and self.Entreda_producto_venta.get() != '' and self.Entreda_precio_venta.get() != '':

			self.Boton_Modificar_V.config(state='normal')

			self.Boton_Agregar_V.config(state='normal')	

			self.Boton_Eliminar_V.config(state='normal')

			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()
			
			#Fecha para Agregar al Arbol
			today = date.today()
			d1 = today.strftime("%d/%m/%Y")

			try:
				cursor.execute(f"INSERT INTO Venta (Producto, PrecioU, Cantidad, Fecha) VALUES ('{self.Entreda_producto_venta.get()}',{self.Entreda_precio_venta.get()},{self.Entreda_cantidad_venta.get()},'{d1}')")
				
				self.conn.commit()

				self.Close_Data()

				self.Precio_Vender()

				self.Update_Arbol_Venta()

				self.Precio_Total_Vender()

				self.ventana_venta.destroy()

			except:
				self.Close_Data()

				Label(self.ventana_venta, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=125)
				
				Label(self.ventana_venta, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=184)


	#Agregar el Precio Cantidad x Unidad
	def Precio_Vender(self):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		cursor.execute(f"UPDATE Venta SET PrecioT = PrecioU * Cantidad")
				
		self.conn.commit()

		self.Close_Data()


	#Actualizar El precio Total
	def Precio_Total_Vender(self):
		#Fecha para Agregar al Arbol
		today = date.today()
		d1 = today.strftime("%d/%m/%Y")

		#Actualizando Precio
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute(f"SELECT sum(Cantidad), sum(PrecioT) FROM Venta WHERE Fecha = '{d1}'")
		
		for x in data:
			self.Cantidad_Arbol_Venta.heading('#0',text=f'{x[0]}', anchor=E)
			self.Precio_Arbol_Venta.heading('#0',text=f'{x[1]}', anchor=E)

			self.Ganancia = x[1]
			
		self.Close_Data()


	#Ventana de Modificar productos
	def Ventana_Modificar_Vender(self):
		
		select=self.ArbolVenta.focus()

		row = self.ArbolVenta.item(select, 'values')


		if row != '':
			self.Mensaje_Venta['text'] = ''

			self.Boton_Agregar_V.config(state='disabled')	
			self.Boton_Modificar_V.config(state='disabled')
			self.Boton_Eliminar_V.config(state='disabled')

			self.ventana_Modificar_venta = Frame(self.Frame_boton_venta, width=300, height=250, bg='#d7d7d7')
			self.ventana_Modificar_venta.place(x=320, y=60)

			#Marco de ventana
			Label(self.ventana_Modificar_venta, bd=1, height=250, bg='black').place(x=-3,y=0)
			Label(self.ventana_Modificar_venta, bd=1, width=300, bg='black').place(x=0,y=-17)
			Label(self.ventana_Modificar_venta, bd=1, height=300, bg='black').place(x=299,y=0)
			Label(self.ventana_Modificar_venta, bd=1, width=300, bg='black').place(x=0,y=248)

			#Entrada de Datos
			Label(self.ventana_Modificar_venta, text='Producto', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=111, y=18)
			self.Entreda_producto_venta_M = Entry(self.ventana_Modificar_venta)
			self.Entreda_producto_venta_M.place(x=25, y=40, height=25, width=250)
			self.Entreda_producto_venta_M.focus()
			self.Entreda_producto_venta_M.insert(END, row[0])
			self.Entreda_producto_venta_M.bind('<Return>', lambda _:self.Entreda_precio_venta_M.focus())


			#Entrada de Datos
			Label(self.ventana_Modificar_venta, text='Precio por Unidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=80, y=77)
			self.Entreda_precio_venta_M = Entry(self.ventana_Modificar_venta)
			self.Entreda_precio_venta_M.place(x=25, y=100, height=25, width=250)
			self.Entreda_precio_venta_M.insert(END, row[1])
			self.Entreda_precio_venta_M.bind('<Return>', lambda _:self.Entreda_cantidad_Venta_M.focus())


			#Entrada de Datos
			Label(self.ventana_Modificar_venta, text='Cantidad', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=112, y=135)
			self.Entreda_cantidad_Venta_M = Entry(self.ventana_Modificar_venta)
			self.Entreda_cantidad_Venta_M.place(x=25, y=158, height=25, width=250)
			self.Entreda_cantidad_Venta_M.insert(END, row[2])
			self.Entreda_cantidad_Venta_M.bind('<Return>', lambda _:self.Mandar_Modificar_Vender())


			#Boton comprar
			Button(self.ventana_Modificar_venta, text='Modificar', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Modificar_Vender).place(x=35, y=210)
			
			#Boton Cancelar
			Button(self.ventana_Modificar_venta, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_VB).place(x=200, y=210)
		

		else:
			self.Mensaje_Venta['text'] = 'Selecciones un elemento'


	#Actualizar los datos de la base de datos
	def Mandar_Modificar_Vender(self):
		select=self.ArbolVenta.focus()

		row = self.ArbolVenta.item(select, 'text')

		

		if self.Entreda_cantidad_Venta_M.get() != '' and self.Entreda_producto_venta_M.get() != '' and self.Entreda_precio_venta_M.get() != '':

			self.Boton_Modificar_V.config(state='normal')

			self.Boton_Agregar_V.config(state='normal')	

			self.Boton_Eliminar_V.config(state='normal')
			
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()


			try:
				cursor.execute(f"UPDATE Venta SET Producto='{self.Entreda_producto_venta_M.get()}', PrecioU={self.Entreda_precio_venta_M.get()}, Cantidad={self.Entreda_cantidad_Venta_M.get()} WHERE ID={row}")
				
				self.conn.commit()
					
				self.Precio_Vender()

				self.Update_Arbol_Venta()

				self.Precio_Total_Vender()

				self.ventana_Modificar_venta.destroy()

				self.Close_Data()

			except:
				self.Close_Data()

				Label(self.ventana_Modificar_venta, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=125)
				
				Label(self.ventana_Modificar_venta, text='Solo Digitos', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=23, y=184)


	#Eliminar datos de la base de datos
	def Eliminar_Venta(self):
		select=self.ArbolVenta.focus()

		row = self.ArbolVenta.item(select, 'text')

		if row != '':
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			cursor.execute(f"DELETE FROM Venta WHERE ID = {row}")
					
			self.conn.commit()

			self.Close_Data()

			self.Update_Arbol_Venta()

			self.Precio_Total_Vender()

			self.Mensaje_Venta['text'] = ''


		else:
			self.Mensaje_Venta['text'] = 'Selecciones un elemento'

#----------------------------------------------Boton Empleados------------------------------------------------------
	def B_Empleados(self):
		self.Boton_Configuracion.config(state='disabled')

		#Frame Empleados
		self.Frame_boton_Empleados = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_boton_Empleados.place(x=0, y=101)

		ajuste_botones = Frame(self.Frame_boton_Empleados, bg='#d7d7d7', height=412, width=240)
		ajuste_botones.place(x=0, y=0)
		
		#Boton Back
		Button(ajuste_botones, image=self.Image_back, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Destroy_Empleados).place(x=10, y=10)

		#Boton Agragar Empleados
		self.Boton_Agregar_E = Button(ajuste_botones, image=self.mas, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Ventana_Agregar_Empleados)
		self.Boton_Agregar_E.place(x=80, y=40)
		Label(ajuste_botones, text='Agregar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=83, y=113)

		#Boton Modificar Empleados
		self.Boton_Modificar_E = Button(ajuste_botones, image=self.Lapiz, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Ventanas_Modificar_Empleados)
		self.Boton_Modificar_E.place(x=80, y=160)
		Label(ajuste_botones, text='Modificar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=77, y=234)

		#boton Eliminar Empleados
		self.Boton_Eliminar_E = Button(ajuste_botones, image=self.cancelar, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Eliminar_Empleados)
		self.Boton_Eliminar_E.place(x=80, y=280)
		Label(ajuste_botones, text='Eliminar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=82, y=353)

		Label(self.Frame_boton_Empleados, text='Empleados', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 12, 'bold'), fg='black').place(x=520,y=6)

		#Mensaje de de Advertencia
		self.Mensaje_Empleados = Label(ajuste_botones, text='', bg='#d7d7d7', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='#e94548')
		self.Mensaje_Empleados.place(x=45, y=385)

		#Arbol de la base de datos
		self.ArbolEmpleados = ttk.Treeview(self.Frame_boton_Empleados)

		self.ArbolEmpleados.column('#0', width=1, anchor=W)

		self.ArbolEmpleados.heading('#0', text='Empleados')
		
		self.ArbolEmpleados.place(x=250, y=30, width=120, height=370)

		#Frame de Informacion de los Distribuidores
		self.Frame_Informacion = Frame(self.Frame_boton_Empleados, bg='#F2F2F2', height=370, width=500)
		self.Frame_Informacion.place(x=380, y=30)

		Label(self.Frame_Informacion, text='Nombre: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black').place(x=5, y=35)

		Label(self.Frame_Informacion, text='Nacimiento: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black').place(x=5, y=75)

		Label(self.Frame_Informacion, text='Puesto: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black').place(x=5, y=115)

		Label(self.Frame_Informacion, text='Nomina: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black').place(x=5, y=155)

		Label(self.Frame_Informacion, text='Nota: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black').place(x=5, y=195)

		#Respuesta de la Base de Datos
		self.Respuesta_Nombre = Label(self.Frame_Informacion, text='', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Respuesta_Nombre.place(x=80, y=35)

		self.Respuesta_Nacimiento = Label(self.Frame_Informacion, text='', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Respuesta_Nacimiento.place(x=80, y=75)

		self.Respuesta_Puesto = Text(self.Frame_Informacion, bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black', height=3, width=60, relief=FLAT)
		self.Respuesta_Puesto.place(x=80, y=115)

		self.Respuesta_Nomina = Label(self.Frame_Informacion, text='', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Respuesta_Nomina.place(x=80, y=155)

		self.Respuesta_Nota = Label(self.Frame_Informacion, text='', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Respuesta_Nota.place(x=80, y=195)

		self.Seleccion_Empleados()

		self.Update_Arbol_Empleados()

	#Destruir Frame
	def Destroy_Empleados(self):
		self.Frame_boton_Empleados.destroy()
		self.Boton_Configuracion.config(state='normal')


	#Limpiar y Actualizar los datos del Arbol
	def Update_Arbol_Empleados(self):
		#Limpiando Arbol
		for x in self.ArbolEmpleados.get_children():
			self.ArbolEmpleados.delete(x)

		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute("SELECT Nombre FROM Empleados;")
		
		for x in data:
			Nombre = x[0]
			size = len(Nombre)
			if size >= 13:
				self.ArbolEmpleados.insert('', END, text=Nombre[0:13])
			else:
				self.ArbolEmpleados.insert('', END, text=Nombre)
			
		self.Close_Data()

	
	#Plasmar informacion en la pantalla
	def Envio_informacion_Empleados(self, recibir):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute(f"SELECT Nombre, Nacimiento, Puesto, Nomina, Nota FROM Empleados WHERE Nombre LIKE '{recibir}%';")
		
		for x in data:
			self.Respuesta_Puesto.delete(1.0,END)
			self.Respuesta_Nombre['text'] = x[0]
			self.Respuesta_Nacimiento['text'] = x[1]
			self.Respuesta_Puesto.insert(END,x[2])
			self.Respuesta_Nomina['text'] = x[3]
			self.Respuesta_Nota['text'] = x[4]

			
		self.Close_Data()


	#Bucle de informacion
	def Seleccion_Empleados(self):
		select=self.ArbolEmpleados.focus()

		row = self.ArbolEmpleados.item(select, 'text')

		if row != '':
			
			self.Envio_informacion_Empleados(row)
		
			self.Frame_Informacion.after(100, self.Seleccion_Empleados)

		else:
		
			self.Frame_Informacion.after(100, self.Seleccion_Empleados)


	#Ventana de agragar distribuidoras
	def Ventana_Agregar_Empleados(self):
		self.Boton_Agregar_E.config(state='disabled')	
		self.Boton_Modificar_E.config(state='disabled')
		self.Boton_Eliminar_E.config(state='disabled')


		self.ventana_Empleados = Frame(self.Frame_boton_Empleados, width=300, height=250, bg='#d7d7d7')
		self.ventana_Empleados.place(x=320, y=60)

		#Marco de ventana
		Label(self.ventana_Empleados, bd=1, height=250, bg='black').place(x=-3,y=0)
		Label(self.ventana_Empleados, bd=1, width=300, bg='black').place(x=0,y=-17)
		Label(self.ventana_Empleados, bd=1, height=300, bg='black').place(x=299,y=0)
		Label(self.ventana_Empleados, bd=1, width=300, bg='black').place(x=0,y=248)

		#Entrada de Datos
		Label(self.ventana_Empleados, text='Nombre', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=115, y=2)
		self.Nombre_E = Entry(self.ventana_Empleados)
		self.Nombre_E.place(x=25, y=24, height=25, width=250)
		self.Nombre_E.focus()
		self.Nombre_E.bind('<Return>', lambda _:self.Nacimiento_E.focus())	


		#Entrada de Datos
		Label(self.ventana_Empleados, text='Nacimiento', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=13, y=50)
		self.Nacimiento_E = Entry(self.ventana_Empleados)
		self.Nacimiento_E.place(x=25, y=72, height=25, width=70)
		self.Nacimiento_E.bind('<Return>', lambda _:self.Nomina_E.focus())

		#Entrada de Datos
		Label(self.ventana_Empleados, text='Nomina', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=207, y=50)
		self.Nomina_E = Entry(self.ventana_Empleados)
		self.Nomina_E.place(x=205, y=72, height=25, width=70)
		self.Nomina_E.bind('<Return>', lambda _:self.Puesto_E.focus())

		#Entrada de Datos
		Label(self.ventana_Empleados, text='Puesto', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=117, y=98)
		self.Puesto_E = Entry(self.ventana_Empleados)
		self.Puesto_E.place(x=25, y=120, height=25, width=250)
		self.Puesto_E.bind('<Return>', lambda _:self.Nota_E.focus())

		#Entrada de Datos
		Label(self.ventana_Empleados, text='Nota', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=122, y=148)
		self.Nota_E = Entry(self.ventana_Empleados)
		self.Nota_E.place(x=25, y=170, height=25, width=250)
		self.Nota_E.bind('<Return>', lambda _:self.Mandar_Empleados())



		#Boton comprar
		Button(self.ventana_Empleados, text='Agregar', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Empleados).place(x=35, y=214)
		
		#Boton Cancelar
		Button(self.ventana_Empleados, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_E).place(x=200, y=214)
	

	def Activar_Botones_E(self):
		
		self.Boton_Modificar_E.config(state='normal')

		self.Boton_Agregar_E.config(state='normal')	

		self.Boton_Eliminar_E.config(state='normal')

		try:
			self.ventana_Empleados.destroy()
		except:
			pass
		try:
			self.ventana_Modificar_Empleados.destroy()
		except:
			pass


	#Almacenar los datos en la base de datos
	def Mandar_Empleados(self):
		if (self.Nombre_E.get() != '' and self.Nacimiento_E.get() != '' and self.Puesto_E.get() != '' and self.Nomina_E.get() != ''):

			self.Boton_Modificar_E.config(state='normal')

			self.Boton_Agregar_E.config(state='normal')	

			self.Boton_Eliminar_E.config(state='normal')

			today = date.today()
			d1 = today.strftime("%d/%m/%Y")
			
			try:
				self.conn = sql.connect(self.__DB)		

				cursor = self.conn.cursor()
			
				cursor.execute(f"INSERT INTO Empleados (Nombre, Nacimiento, Puesto, Nomina, Nota) VALUES ('{self.Nombre_E.get()}','{self.Nacimiento_E.get()}','{self.Puesto_E.get()}','{self.Nomina_E.get()}', '{self.Nota_E.get()}')")
					
				self.conn.commit()

				self.Close_Data()

				self.Envio_informacion_Empleados(self.Nombre_E.get())

				self.Update_Arbol_Empleados()

				self.ventana_Empleados.destroy()

			except:
				self.Close_Data()

		else:
			Label(self.ventana_Empleados, text='Todos los campos son Obligatorios', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=78, y=192)


	#Ventana modificar empleados	
	def Ventanas_Modificar_Empleados(self):

		select=self.ArbolEmpleados.focus()

		row = self.ArbolEmpleados.item(select, 'text')

		


		if row != '':
			#Insertores
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			data = cursor.execute(f"SELECT * FROM Empleados WHERE Nombre = '{row}';")
			

			for x in data:
				in_Nombre_DM = x[1]
				in_Nacimiento_DM = x[2]
				in_Puesto_DM = x[3]
				in_Nomina_DM = x[4]
				in_Nota_DM = x[5]

			
			self.Close_Data()

			#Ventana
			self.Mensaje_Empleados['text'] = ''

			self.Boton_Agregar_E.config(state='disabled')	
			self.Boton_Modificar_E.config(state='disabled')
			self.Boton_Eliminar_E.config(state='disabled')

			self.ventana_Modificar_Empleados = Frame(self.Frame_boton_Empleados, width=300, height=250, bg='#d7d7d7')
			self.ventana_Modificar_Empleados.place(x=320, y=60)

			#Marco de ventana
			Label(self.ventana_Modificar_Empleados, bd=1, height=250, bg='black').place(x=-3,y=0)
			Label(self.ventana_Modificar_Empleados, bd=1, width=300, bg='black').place(x=0,y=-17)
			Label(self.ventana_Modificar_Empleados, bd=1, height=300, bg='black').place(x=299,y=0)
			Label(self.ventana_Modificar_Empleados, bd=1, width=300, bg='black').place(x=0,y=248)

			#Entrada de Datos
			Label(self.ventana_Modificar_Empleados, text='Nombre', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=115, y=2)
			self.Nombre_E = Entry(self.ventana_Modificar_Empleados)
			self.Nombre_E.place(x=25, y=24, height=25, width=250)
			self.Nombre_E.focus()
			self.Nombre_E.bind('<Return>', lambda _:self.Nacimiento_E.focus())	
			self.Nombre_E.insert(END, in_Nombre_DM)

			#Entrada de Datos
			Label(self.ventana_Modificar_Empleados, text='Nacimiento', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=13, y=50)
			self.Nacimiento_E = Entry(self.ventana_Modificar_Empleados)
			self.Nacimiento_E.place(x=25, y=72, height=25, width=70)
			self.Nacimiento_E.bind('<Return>', lambda _:self.Nomina_E.focus())
			self.Nacimiento_E.insert(END, in_Nacimiento_DM)

			#Entrada de Datos
			Label(self.ventana_Modificar_Empleados, text='Nomina', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=207, y=50)
			self.Nomina_E = Entry(self.ventana_Modificar_Empleados)
			self.Nomina_E.place(x=205, y=72, height=25, width=70)
			self.Nomina_E.bind('<Return>', lambda _:self.Puesto_E.focus())
			self.Nomina_E.insert(END, in_Nomina_DM)

			#Entrada de Datos
			Label(self.ventana_Modificar_Empleados, text='Puesto', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=117, y=98)
			self.Puesto_E = Entry(self.ventana_Modificar_Empleados)
			self.Puesto_E.place(x=25, y=120, height=25, width=250)
			self.Puesto_E.bind('<Return>', lambda _:self.Nota_E.focus())
			self.Puesto_E.insert(END, in_Puesto_DM)

			#Entrada de Datos
			Label(self.ventana_Modificar_Empleados, text='Nota', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=122, y=148)
			self.Nota_E = Entry(self.ventana_Modificar_Empleados)
			self.Nota_E.place(x=25, y=170, height=25, width=250)
			self.Nota_E.bind('<Return>', lambda _:self.Mandar_Modificar_Empleados())
			self.Nota_E.insert(END, in_Nota_DM)


			#Boton comprar
			Button(self.ventana_Modificar_Empleados, text='Modificar', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Modificar_Empleados).place(x=35, y=214)
			
			#Boton Cancelar
			Button(self.ventana_Modificar_Empleados, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_E).place(x=200, y=214)
		

		else:
			self.Mensaje_Empleados['text'] = 'Selecciones un elemento'


	#Actualizar los datos de la base de datos
	def Mandar_Modificar_Empleados(self):
		select=self.ArbolEmpleados.focus()

		row = self.ArbolEmpleados.item(select, 'text')

		

		if self.Nombre_E.get() != '' and self.Nacimiento_E.get() != '' and self.Nomina_E.get() != '' and self.Puesto_E.get() != '' and self.Nota_E.get() != '':

			self.Boton_Modificar_E.config(state='normal')

			self.Boton_Agregar_E.config(state='normal')	

			self.Boton_Eliminar_E.config(state='normal')


			#Conectar Base de Datos			
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			cursor.execute(f"UPDATE Empleados SET Nombre='{self.Nombre_E.get()}', Nacimiento='{self.Nacimiento_E.get()}', Puesto='{self.Puesto_E.get()}', Nomina='{self.Nomina_E.get()}', Nota='{self.Nota_E.get()}' WHERE Nombre LIKE '{row}%'")
				
			self.conn.commit()

			#Actualizar la informacion de la base de Datos

			self.Envio_informacion(row)

			self.Update_Arbol_Empleados()

			self.ventana_Modificar_Empleados.destroy()

			self.Close_Data()

			
		else:
			Label(self.ventana_Modificar_Empleados, text='Todos los campos son obligatorios', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=78, y=192)


	#Eliminar Empleados
	def Eliminar_Empleados(self):
		select=self.ArbolEmpleados.focus()

		row = self.ArbolEmpleados.item(select, 'text')

		if row != '':
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			cursor.execute(f"DELETE FROM Empleados WHERE Nombre LIKE '{row}%'")

			self.conn.commit()

			self.Update_Arbol_Empleados()

			#Limpiar Texto
			self.Mensaje_Empleados['text'] = ''

			#Limpiar Ventana
			self.Respuesta_Nombre['text'] = ''
			self.Respuesta_Nacimiento['text'] = ''
			self.Respuesta_Puesto['text'] = ''
			self.Respuesta_Nomina['text'] = ''
			self.Respuesta_Nota['text'] = ''



		else:
			self.Mensaje_Empleados['text'] = 'Selecciones un elemento'

#--------------------------------------------Boton Distribuidores---------------------------------------------------
	def B_Distribuidores(self):
		self.Boton_Configuracion.config(state='disabled')

		#Frame Distribuidores
		self.Frame_boton_Distribuidores = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_boton_Distribuidores.place(x=0, y=101)

		ajuste_botones = Frame(self.Frame_boton_Distribuidores, bg='#d7d7d7', height=412, width=240)
		ajuste_botones.place(x=0, y=0)
		
		#Boton Back
		Button(ajuste_botones, image=self.Image_back, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Destroy_Distribuidores).place(x=10, y=10)

		#Boton Agragar Venta
		self.Boton_Agregar_D = Button(ajuste_botones, image=self.mas, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Ventana_Agregar_Empresa)
		self.Boton_Agregar_D.place(x=80, y=40)
		Label(ajuste_botones, text='Agregar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=83, y=113)

		#Boton Modificar Venta
		self.Boton_Modificar_D = Button(ajuste_botones, image=self.Lapiz, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.ventana_Modificar_Distribuidores)
		self.Boton_Modificar_D.place(x=80, y=160)
		Label(ajuste_botones, text='Modificar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=77, y=234)

		#boton Eliminar Venta
		self.Boton_Eliminar_D = Button(ajuste_botones, image=self.cancelar, bg='#d7d7d7', relief=FLAT, bd=0, activebackground='#d7d7d7', command=self.Eliminar_Distribuidora)
		self.Boton_Eliminar_D.place(x=80, y=280)
		Label(ajuste_botones, text='Eliminar', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=82, y=353)

		Label(self.Frame_boton_Distribuidores, text='Distribuidores', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 12, 'bold'), fg='black').place(x=520,y=6)

		#Mensaje de de Advertencia
		self.Mensaje_Distribuidores = Label(ajuste_botones, text='', bg='#d7d7d7', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='#e94548')
		self.Mensaje_Distribuidores.place(x=45, y=385)

		#Arbol de la base de datos
		self.ArbolDistribuidores = ttk.Treeview(self.Frame_boton_Distribuidores)

		self.ArbolDistribuidores.column('#0', width=1, anchor=W)

		self.ArbolDistribuidores.heading('#0', text='Distribuidores')
		
		self.ArbolDistribuidores.place(x=250, y=30, width=120, height=370)

		#Frame de Informacion de los Distribuidores
		self.Frame_Informacion = Frame(self.Frame_boton_Distribuidores, bg='#F2F2F2', height=370, width=500)
		self.Frame_Informacion.place(x=380, y=30)

		self.Nombre_Distribuidor = Label(self.Frame_Informacion, text='Nombre E.: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Nombre_Distribuidor.place(x=5, y=35)

		self.RIF_Distribuidor = Label(self.Frame_Informacion, text='RIF: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.RIF_Distribuidor.place(x=5, y=110)

		self.Ubicacion_Distribuidor = Label(self.Frame_Informacion, text='Ubicación: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Ubicacion_Distribuidor.place(x=5, y=200)

		self.Contacto_Distribuidor = Label(self.Frame_Informacion, text='Contacto: ', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Contacto_Distribuidor.place(x=5, y=290)

		#Respuesta de la Base de Datos
		self.Respuesta_Nombre = Label(self.Frame_Informacion, text='', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Respuesta_Nombre.place(x=80, y=35)

		self.Respuesta_RIF = Label(self.Frame_Informacion, text='', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Respuesta_RIF.place(x=80, y=110)

		self.Respuesta_Ubicacion = Text(self.Frame_Informacion, bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black', height=3, width=60, relief=FLAT)
		self.Respuesta_Ubicacion.place(x=80, y=200)

		self.Respuesta_Contacto = Label(self.Frame_Informacion, text='', bg='#F2F2F2', font=('Nexa Rust Slab Black 01', 9, 'bold'), fg='black')
		self.Respuesta_Contacto.place(x=80, y=290)

		self.Seleccion()

		self.Update_Arbol_Distribuidores()

	#Destruir Frame
	def Destroy_Distribuidores(self):
		self.Frame_boton_Distribuidores.destroy()
		self.Boton_Configuracion.config(state='normal')


	#Limpiar y Actualizar los datos del Arbol
	def Update_Arbol_Distribuidores(self):
		#Limpiando Arbol
		for x in self.ArbolDistribuidores.get_children():
			self.ArbolDistribuidores.delete(x)

		#Actualizando Arbol
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute("SELECT Empresa FROM Distribuidores;")
		
		for x in data:
			self.ArbolDistribuidores.insert('', END, text=x[0])
			
		self.Close_Data()

	
	#Plasmar informacion en la pantalla
	def Envio_informacion(self, recibir):
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute(f"SELECT * FROM Distribuidores WHERE Empresa = '{recibir}';")
		
		for x in data:
			self.Respuesta_Ubicacion.delete(1.0,END)
			self.Respuesta_Nombre['text'] = x[1]
			self.Respuesta_RIF['text'] = x[2]
			self.Respuesta_Ubicacion.insert(END,x[3])
			self.Respuesta_Contacto['text'] = x[4]

			
		self.Close_Data()


	#Bucle de informacion
	def Seleccion(self):
		select=self.ArbolDistribuidores.focus()

		row = self.ArbolDistribuidores.item(select, 'text')

		if row != '':
			self.Envio_informacion(row)
		
			self.Frame_Informacion.after(100, self.Seleccion)

		else:
		
			self.Frame_Informacion.after(100, self.Seleccion)


	#Ventana de agragar distribuidoras
	def Ventana_Agregar_Empresa(self):
		self.Boton_Agregar_D.config(state='disabled')	
		self.Boton_Modificar_D.config(state='disabled')
		self.Boton_Eliminar_D.config(state='disabled')


		self.ventana_Distribuidores = Frame(self.Frame_boton_Distribuidores, width=300, height=250, bg='#d7d7d7')
		self.ventana_Distribuidores.place(x=320, y=60)

		#Marco de ventana
		Label(self.ventana_Distribuidores, bd=1, height=250, bg='black').place(x=-3,y=0)
		Label(self.ventana_Distribuidores, bd=1, width=300, bg='black').place(x=0,y=-17)
		Label(self.ventana_Distribuidores, bd=1, height=300, bg='black').place(x=299,y=0)
		Label(self.ventana_Distribuidores, bd=1, width=300, bg='black').place(x=0,y=248)

		#Entrada de Datos
		Label(self.ventana_Distribuidores, text='Distribuidoras', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=93, y=2)
		self.Empresa_D = Entry(self.ventana_Distribuidores)
		self.Empresa_D.place(x=25, y=24, height=25, width=250)
		self.Empresa_D.focus()
		self.Empresa_D.bind('<Return>', lambda _:self.RIF_D.focus())	


		#Entrada de Datos
		Label(self.ventana_Distribuidores, text='RIF', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=133, y=50)
		self.RIF_D = Entry(self.ventana_Distribuidores)
		self.RIF_D.place(x=25, y=72, height=25, width=250)
		self.RIF_D.bind('<Return>', lambda _:self.Direccion_D.focus())


		#Entrada de Datos
		Label(self.ventana_Distribuidores, text='Dirección', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=109, y=98)
		self.Direccion_D = Entry(self.ventana_Distribuidores)
		self.Direccion_D.place(x=25, y=120, height=25, width=250)
		self.Direccion_D.bind('<Return>', lambda _:self.Contacto_D.focus())


		#Entrada de Datos
		Label(self.ventana_Distribuidores, text='Contacto', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=110, y=145)
		self.Contacto_D = Entry(self.ventana_Distribuidores)
		self.Contacto_D.place(x=25, y=167, height=25, width=250)
		self.Contacto_D.bind('<Return>', lambda _:self.Mandar_Distribuidoras())


		#Boton comprar
		Button(self.ventana_Distribuidores, text='Agregar', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Distribuidoras).place(x=35, y=214)
		
		#Boton Cancelar
		Button(self.ventana_Distribuidores, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_DA).place(x=200, y=214)
	

	def Activar_Botones_DA(self):
		
		self.Boton_Modificar_D.config(state='normal')

		self.Boton_Agregar_D.config(state='normal')	

		self.Boton_Eliminar_D.config(state='normal')

		self.ventana_Distribuidores.destroy()


	#Almacenar los datos en la base de datos
	def Mandar_Distribuidoras(self):
		if (self.Empresa_D.get() != '' and self.Contacto_D.get()):

			self.Boton_Modificar_D.config(state='normal')

			self.Boton_Agregar_D.config(state='normal')	

			self.Boton_Eliminar_D.config(state='normal')
			
			try:
				self.conn = sql.connect(self.__DB)		

				cursor = self.conn.cursor()
			
				cursor.execute(f"INSERT INTO Distribuidores (Empresa, RIF, Direccion, Contacto) VALUES ('{self.Empresa_D.get()}','{self.RIF_D.get()}','{self.Direccion_D.get()}','{self.Contacto_D.get()}')")
					
				self.conn.commit()

				self.Close_Data()

				self.Envio_informacion(self.Empresa_D.get())

				self.Update_Arbol_Distribuidores()

				self.ventana_Distribuidores.destroy()

			except:
				self.Close_Data()

		else:
			Label(self.ventana_Distribuidores, text='Minimo Empresa y Contacto', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=78, y=192)


	#Ventana modificar empleados	
	def ventana_Modificar_Distribuidores(self):

		select=self.ArbolDistribuidores.focus()

		row = self.ArbolDistribuidores.item(select, 'text')

		


		if row != '':
			#Insertores
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			data = cursor.execute(f"SELECT * FROM Distribuidores WHERE Empresa = '{row}';")
			

			for x in data:
				in_Empresa_DM = x[1]
				in_RIF_DM = x[2]
				in_Direccion_DM = x[3]
				in_Contacto_DM = x[4]

			
			self.Close_Data()

			#Ventana
			self.Mensaje_Distribuidores['text'] = ''

			self.Boton_Agregar_D.config(state='disabled')	
			self.Boton_Modificar_D.config(state='disabled')
			self.Boton_Eliminar_D.config(state='disabled')

			self.ventana_Modificar_Distribuidoras = Frame(self.Frame_boton_Distribuidores, width=300, height=250, bg='#d7d7d7')
			self.ventana_Modificar_Distribuidoras.place(x=320, y=60)

			#Marco de ventana
			Label(self.ventana_Modificar_Distribuidoras, bd=1, height=250, bg='black').place(x=-3,y=0)
			Label(self.ventana_Modificar_Distribuidoras, bd=1, width=300, bg='black').place(x=0,y=-17)
			Label(self.ventana_Modificar_Distribuidoras, bd=1, height=300, bg='black').place(x=299,y=0)
			Label(self.ventana_Modificar_Distribuidoras, bd=1, width=300, bg='black').place(x=0,y=248)

			#Entrada de Datos
			Label(self.ventana_Modificar_Distribuidoras, text='Distribuidoras', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=93, y=2)
			self.Empresa_DM = Entry(self.ventana_Modificar_Distribuidoras)
			self.Empresa_DM.place(x=25, y=24, height=25, width=250)
			self.Empresa_DM.focus()
			self.Empresa_DM.bind('<Return>', lambda _:self.RIF_DM.focus())
			self.Empresa_DM.insert(END, in_Empresa_DM)


			#Entrada de Datos
			Label(self.ventana_Modificar_Distribuidoras, text='RIF', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=133, y=50)
			self.RIF_DM = Entry(self.ventana_Modificar_Distribuidoras)
			self.RIF_DM.place(x=25, y=72, height=25, width=250)
			self.RIF_DM.bind('<Return>', lambda _:self.Direccion_DM.focus())
			self.RIF_DM.insert(END, in_RIF_DM)


			#Entrada de Datos
			Label(self.ventana_Modificar_Distribuidoras, text='Dirección', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=109, y=98)
			self.Direccion_DM = Entry(self.ventana_Modificar_Distribuidoras)
			self.Direccion_DM.place(x=25, y=120, height=25, width=250)
			self.Direccion_DM.bind('<Return>', lambda _:self.Contacto_DM.focus())
			self.Direccion_DM.insert(END, in_Direccion_DM)


			#Entrada de Datos
			Label(self.ventana_Modificar_Distribuidoras, text='Contacto', font=('Nexa Rust Slab Black 01', 12, 'bold'), bg='#d7d7d7').place(x=110, y=145)
			self.Contacto_DM = Entry(self.ventana_Modificar_Distribuidoras)
			self.Contacto_DM.place(x=25, y=167, height=25, width=250)
			self.Contacto_DM.bind('<Return>', lambda _:self.Mandar_Modificar_Distribuidores())
			self.Contacto_DM.insert(END, in_Contacto_DM)



			#Boton comprar
			Button(self.ventana_Modificar_Distribuidoras, text='Modificar', bg='#44ad5e', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Mandar_Modificar_Distribuidores).place(x=35, y=214)
			
			#Boton Cancelar
			Button(self.ventana_Modificar_Distribuidoras, text='Cancelar', bg='#e94548', fg='black', font=('Nexa Rust Slab Black 01', 9, 'bold'), command=self.Activar_Botones_DB).place(x=200, y=214)
		

		else:
			self.Mensaje_Distribuidores['text'] = 'Selecciones un elemento'

	
	#Activar Botones
	def Activar_Botones_DB(self):
		self.Boton_Modificar_D.config(state='normal')

		self.Boton_Agregar_D.config(state='normal')	

		self.Boton_Eliminar_D.config(state='normal')

		self.ventana_Modificar_Distribuidoras.destroy()


	#Actualizar los datos de la base de datos
	def Mandar_Modificar_Distribuidores(self):
		select=self.ArbolDistribuidores.focus()

		row = self.ArbolDistribuidores.item(select, 'text')

		

		if self.Empresa_DM.get() != '' and self.Contacto_DM.get():

			self.Boton_Modificar_D.config(state='normal')

			self.Boton_Agregar_D.config(state='normal')	

			self.Boton_Eliminar_D.config(state='normal')


			#Conectar Base de Datos			
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			cursor.execute(f"UPDATE Distribuidores SET Empresa='{self.Empresa_DM.get()}', RIF='{self.RIF_DM.get()}', Direccion='{self.Direccion_DM.get()}', Contacto='{self.Contacto_DM.get()}' WHERE Empresa='{row}'")
				
			self.conn.commit()

			#Actualizar la informacion de la base de Datos

			self.Envio_informacion(row)

			self.Update_Arbol_Distribuidores()

			self.ventana_Modificar_Distribuidoras.destroy()

			self.Close_Data()

			
		else:
			Label(self.ventana_Modificar_Distribuidoras, text='Minimo Empresa y Contacto', fg='red', font=('Nexa Rust Slab Black 01', 8), bg='#d7d7d7').place(x=78, y=192)
				

	#Eliminar Empleados
	def Eliminar_Distribuidora(self):
		select=self.ArbolDistribuidores.focus()

		row = self.ArbolDistribuidores.item(select, 'text')

		if row != '':
			self.conn = sql.connect(self.__DB)		

			cursor = self.conn.cursor()

			cursor.execute(f"DELETE FROM Distribuidores WHERE Empresa = '{row}'")

			self.conn.commit()

			self.Update_Arbol_Distribuidores()

			#Limpiar Texto
			self.Mensaje_Distribuidores['text'] = ''

			#Limpiar Ventana
			self.Respuesta_Ubicacion.delete(1.0,END)
			self.Respuesta_Nombre['text'] = ''
			self.Respuesta_RIF['text'] = ''
			self.Respuesta_Contacto['text'] = ''



		else:
			self.Mensaje_Distribuidores['text'] = 'Selecciones un elemento'

#---------------------------------------------Boton Estadisticas----------------------------------------------------

	def B_Estadisticas(self):
		self.Boton_Configuracion.config(state='disabled')


		#Frame Distribuidores
		self.Frame_boton_Estadisticas = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_boton_Estadisticas.place(x=0, y=101)

		Button(self.Frame_boton_Estadisticas, image=self.Image_back, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Destroy_Estadisticas).place(x=10, y=10)


		Button(self.Frame_boton_Estadisticas, image=self.Diario, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Grafica_Diaria).place(x=100, y=50)
		Button(self.Frame_boton_Estadisticas, text='Analisis Diario', font=('Nexa Rust Slab Black 01', 11, 'bold'), bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Grafica_Diaria).place(x=100, y=160)


		Button(self.Frame_boton_Estadisticas, image=self.Semana, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Grafica_Semanal).place(x=390, y=50)
		Button(self.Frame_boton_Estadisticas, text='Analisis Semanal', font=('Nexa Rust Slab Black 01', 11, 'bold'), bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Grafica_Semanal).place(x=380, y=160)


		Button(self.Frame_boton_Estadisticas, image=self.Mensual, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Grafica_Mensual).place(x=680, y=50)
		Button(self.Frame_boton_Estadisticas, text='Analisis Mensual', font=('Nexa Rust Slab Black 01', 11, 'bold'), bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Grafica_Mensual).place(x=672, y=160)


	def Destroy_Estadisticas(self):
		self.Frame_boton_Estadisticas.destroy()

		self.Boton_Configuracion.config(state='normal')

	#===========================Analisis Diario========================
	#Grafica Diaria
	def Grafica_Diaria(self):
		#Frame Distribuidores
		self.Frame_Diario = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_Diario.place(x=0, y=101)

		Button(self.Frame_Diario, image=self.Image_back, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Destroy_Frame_Diario).place(x=10, y=10)

		self.Producto_mas_V_Hoy()


	def Destroy_Frame_Diario(self):
		matplotlib.pyplot.close('all')
		self.Frame_Diario.destroy()


	def Producto_mas_V_Hoy(self):
		#==========================Toma de Datos==============================
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute("SELECT * FROM Venta ORDER BY Cantidad DESC ;")
		
		Top_producto_vendidos_Cantidad = []

		Top_producto_vendidos_nombre = []

		for x in data:
			if len(Top_producto_vendidos_nombre) == 10:
				break
			else:
				Top_producto_vendidos_Cantidad.append(x[3])
				Top_producto_vendidos_nombre.append(x[1])
	
			
		self.Close_Data()

		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Productos mas Vendidos del Dia')
		
		myexplode = []

		size = len(Top_producto_vendidos_nombre)
		
		for i in range(size):
			if i == 0:
				myexplode.append(0.1)
			else:
				myexplode.append(0)


		axs.pie(Top_producto_vendidos_Cantidad, labels = Top_producto_vendidos_nombre, startangle=0, shadow = True, explode = myexplode)
		

		canva= FigureCanvasTkAgg(fig, master=self.Frame_Diario)


		canva.draw()


		canva.get_tk_widget().place(x=-100,y=50)

		self.Gastos_Hoy()


	#Gastos mas Altos del dia 
	def Gastos_Hoy(self):
		#======================Segunda Toma de Datos========================
		self.conn = sql.connect(self.__DB)		

		cursor = self.conn.cursor()

		data = cursor.execute("SELECT * FROM Gastos ORDER BY Cantidad DESC ;")
		
		Top_producto_comprados_Cantidad = []

		Top_producto_comprados_nombre = []

		control = 0

		for x in data:
			if len(Top_producto_comprados_nombre) == 10:
				break
			else:
				Top_producto_comprados_Cantidad.append(x[3])
				Top_producto_comprados_nombre.append(x[1])
	
			
		self.Close_Data()

		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Gastos mas altos del Dia')
		
		myexplode = []

		size = len(Top_producto_comprados_nombre)
		
		for i in range(size):
			if i == 0:
				myexplode.append(0.1)
			else:
				myexplode.append(0)


		axs.pie(Top_producto_comprados_Cantidad, labels = Top_producto_comprados_nombre, startangle=0, shadow = True, explode = myexplode)
		

		canva= FigureCanvasTkAgg(fig, master=self.Frame_Diario)


		canva.draw()


		canva.get_tk_widget().place(x=500,y=50)

		self.Valor_T_Diario()


	#Grafica del Comparador de Gasto y ganancia
	def Valor_T_Diario(self):
		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Productos mas Vendidos del Dia')
		
		x = ['Ganancia', 'Perdida']
		colors = ['green', 'red']
		y = [self.Ganancia, self.Perdida]

		try:
			axs.bar(x, y, color = colors)

		except TypeError:
			pass
		

		canva= FigureCanvasTkAgg(fig, master=self.Frame_Diario)


		canva.draw()


		canva.get_tk_widget().place(x=320,y=25, height=350, width=310)


	#==========================Analisis Semanal========================
	#Grafica Semanal
	def Grafica_Semanal(self):
		#Frame Distribuidores
		self.Frame_Semanal = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_Semanal.place(x=0, y=101)

		Button(self.Frame_Semanal, image=self.Image_back, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Destroy_Frame_Semanal).place(x=10, y=10)

		self.Producto_mas_V_Semana()
		self.Valor_T_Ganancia_Semanal()


	def Destroy_Frame_Semanal(self):
		matplotlib.pyplot.close('all')
		self.Frame_Semanal.destroy()


	#Producto mas vendido de la semana
	def Producto_mas_V_Semana(self):
		#==========================Toma de Datos==============================
		ruta = r'{}\BD'.format(os.getcwd())
		
		archivero = [arch.name for arch in scandir(ruta) if arch.is_file()]

		today = date.today()

		d1 = int(today.strftime("%d"))

		Gestor_Semanal_Nombres = []

		Gestor_Semanal_Cantidad = []

		Control_Archivos = []

		#Toma de Archivos disponibles
		for x in archivero:
			#busqueda del Archivo numericos
			try:
				fecha_busqueda = int(x[0]+x[1])

			except ValueError:
				break

			#Rango de 7 por dias de la semana
			for i in range(7):

				if fecha_busqueda == d1-i :

					Control_Archivos.append(x)

					break


		#Busqueda de Datos
		for x in Control_Archivos:
			#Nombre de la base de Datos Encontrada
			Name = r'{}\BD\{}'.format(os.getcwd(), x)

			#Rango de 31 por dias del Mes
			for i in range(1,32):
				d5 = today.strftime(f'{i}_%m_%Y')

				ubi = f'{d5}_{self.User}.db'
				comparacion = r'{}\BD\{}'.format(os.getcwd(), ubi)

				if Name == comparacion:
					conn = sql.connect(Name)		

					cursor = conn.cursor()

					data = cursor.execute("SELECT * FROM Venta ORDER BY Cantidad DESC ;")


					#Pasar datos encontrados a una Lista
					for x in data:
							Gestor_Semanal_Nombres.append(x[1])
							Gestor_Semanal_Cantidad.append(x[3])

					conn.close()


		
		#Almacen de datos final
		dato_Semanal_cantidad = []

		dato_Semanal_Nombre = []

		#Control de los primeros 10 datos
		Control = 0

		#Obtener los primeros 10 Datos de los arrays Gestores
		for x in Gestor_Semanal_Nombres:

			if Control == 10:
				break
			else:
				dato_Semanal_Nombre.append(x)

			Control += 1

		#Reinicio del control para nuevas tomas de datos
		Control = 0


		#Obtener los primeros 10 Datos de los arrays Gestores
		for x in Gestor_Semanal_Cantidad:

			if Control == 10:
				break
			else:
				dato_Semanal_cantidad.append(x)

			Control += 1

		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Productos mas Vendidos de la Semana')
		
		myexplode = []

		size = len(dato_Semanal_Nombre)

		#Busca exactamente los datos extraidos para evitar errores
		for i in range(size):
			if i == 0:
				myexplode.append(0.1)
			else:
				myexplode.append(0)


		axs.pie(dato_Semanal_cantidad, labels = dato_Semanal_Nombre, startangle=0, shadow = True, explode = myexplode)
		
		canva= FigureCanvasTkAgg(fig, master=self.Frame_Semanal)

		canva.draw()

		canva.get_tk_widget().place(x=-100,y=50)


		self.Gasto_Semana()


	#Gasto mas alto de la semana
	def Gasto_Semana(self):
		#==========================Toma de Datos==============================
		ruta = r'{}\BD'.format(os.getcwd())
		
		archivero = [arch.name for arch in scandir(ruta) if arch.is_file()]

		today = date.today()

		d1 = int(today.strftime("%d"))

		Gestor_Semanal_Nombres = []

		Gestor_Semanal_Cantidad = []

		Control_Archivos = []

		#Toma de Archivos disponibles
		for x in archivero:
			#busqueda del Archivo numericos
			try:
				fecha_busqueda = int(x[0]+x[1])

			except ValueError:
				break

			#Rango de 7 por dias de la semana
			for i in range(7):

				if fecha_busqueda == d1-i :

					Control_Archivos.append(x)

					break


		#Busqueda de Datos
		for x in Control_Archivos:
			#Nombre de la base de Datos Encontrada
			Name = r'{}\BD\{}'.format(os.getcwd(), x)

			#Rango de 31 por dias del Mes
			for i in range(1,32):
				d5 = today.strftime(f'{i}_%m_%Y')

				ubi = f'{d5}_{self.User}.db'
				comparacion = r'{}\BD\{}'.format(os.getcwd(), ubi)

				if Name == comparacion:
					conn = sql.connect(Name)		

					cursor = conn.cursor()

					data = cursor.execute("SELECT * FROM Gastos ORDER BY Cantidad DESC ;")


					#Pasar datos encontrados a una Lista
					for x in data:
							Gestor_Semanal_Nombres.append(x[1])
							Gestor_Semanal_Cantidad.append(x[3])

					conn.close()

		
		#Almacen de datos final
		dato_Semanal_cantidad = []

		dato_Semanal_Nombre = []

		#Control de los primeros 10 datos
		Control = 0

		#Obtener los primeros 10 Datos de los arrays Gestores
		for x in Gestor_Semanal_Nombres:

			if Control == 10:
				break
			else:
				dato_Semanal_Nombre.append(x)

			Control += 1

		#Reinicio del control para nuevas tomas de datos
		Control = 0

		#Obtener los primeros 10 Datos de los arrays Gestores
		for x in Gestor_Semanal_Cantidad:

			if Control == 10:
				break
			else:
				dato_Semanal_cantidad.append(x)

			Control += 1

		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Productos mas Vendidos de la Semana')
		
		myexplode = []

		size = len(dato_Semanal_Nombre)

		#Busca exactamente los datos extraidos para evitar errores
		for i in range(size):
			if i == 0:
				myexplode.append(0.1)
			else:
				myexplode.append(0)


		axs.pie(dato_Semanal_cantidad, labels = dato_Semanal_Nombre, startangle=0, shadow = True, explode = myexplode)
		
		canva= FigureCanvasTkAgg(fig, master=self.Frame_Semanal)

		canva.draw()

		canva.get_tk_widget().place(x=500,y=50)

		self.Valor_Ganancia_Semanal()

		self.Valor_Perdida_Semanal()


	#Obtener suma total de datos de Ganancia de la semana
	def Valor_Ganancia_Semanal(self):
		#==========================Toma de Datos==============================
		ruta = r'{}\BD'.format(os.getcwd())
		
		archivero = [arch.name for arch in scandir(ruta) if arch.is_file()]

		today = date.today()

		d1 = int(today.strftime("%d"))

		Gestor_Semanal_Precio = []

		Control_Archivos = []

		#Toma de Archivos disponibles
		for x in archivero:
			#busqueda del Archivo numericos
			try:
				fecha_busqueda = int(x[0]+x[1])

			except ValueError:
				break

			#Rango de 7 por dias de la semana
			for i in range(7):

				if fecha_busqueda == d1-i :

					Control_Archivos.append(x)

					break


		#Busqueda de Datos
		for x in Control_Archivos:
			#Nombre de la base de Datos Encontrada
			Name = r'{}\BD\{}'.format(os.getcwd(), x)


			#Rango de 31 por dias del Mes
			for i in range(1,32):
				d5 = today.strftime(f'{i}_%m_%Y')

				ubi = f'{d5}_{self.User}.db'
				comparacion = r'{}\BD\{}'.format(os.getcwd(), ubi)

				if Name == comparacion:
					
									
					conn = sql.connect(Name)		
									
					cursor = conn.cursor()
									
					data = cursor.execute("SELECT sum(PrecioT) FROM Venta ORDER BY Cantidad DESC ;")
									
									
					#Pasar datos encontrados a una Lista
					for x in data:
						Gestor_Semanal_Precio.append(x[0])
															
									
					conn.close()
	

		self.Ganancia_Semanal = int()
		try:
			for x in Gestor_Semanal_Precio:
				self.Ganancia_Semanal += x
		except TypeError:
			pass


	#Obtener suma total de datos perdida de la semana
	def Valor_Perdida_Semanal(self):
		#==========================Toma de Datos==============================
		ruta = r'{}\BD'.format(os.getcwd())
		
		archivero = [arch.name for arch in scandir(ruta) if arch.is_file()]

		today = date.today()

		d1 = int(today.strftime("%d"))

		Gestor_Semanal_Precio = []

		Control_Archivos = []

		#Toma de Archivos disponibles
		for x in archivero:
			#busqueda del Archivo numericos
			try:
				fecha_busqueda = int(x[0]+x[1])

			except ValueError:
				break

			#Rango de 7 por dias de la semana
			for i in range(7):

				if fecha_busqueda == d1-i :

					Control_Archivos.append(x)

					break


		#Busqueda de Datos
		for x in Control_Archivos:
			#Nombre de la base de Datos Encontrada
			Name = r'{}\BD\{}'.format(os.getcwd(), x)


			#Rango de 31 por dias del Mes
			for i in range(1,32):
				d5 = today.strftime(f'{i}_%m_%Y')

				ubi = f'{d5}_{self.User}.db'
				comparacion = r'{}\BD\{}'.format(os.getcwd(), ubi)

				if Name == comparacion:
					
									
					conn = sql.connect(Name)		
									
					cursor = conn.cursor()
									
					data = cursor.execute("SELECT sum(PrecioT) FROM Compra ORDER BY Cantidad DESC ;")
									
									
					#Pasar datos encontrados a una Lista
					for x in data:
						Gestor_Semanal_Precio.append(x[0])
															
									
					conn.close()
					

		self.Perdida_Semanal = int()

		try:
			for x in Gestor_Semanal_Precio:
				self.Perdida_Semanal += x

		except TypeError:
			pass


	#Grafica del Comparador de Gastos y Ganancia Semanal
	def Valor_T_Ganancia_Semanal(self):
		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Productos mas Vendidos del Dia')
		
		x = ['Ganancia', 'Perdida']

		colors = ['green', 'red']

		y = [self.Ganancia_Semanal, self.Perdida_Semanal]

		try:
			axs.bar(x, y, color = colors)
		
		except TypeError:
			pass

		canva= FigureCanvasTkAgg(fig, master=self.Frame_Semanal)


		canva.draw()


		canva.get_tk_widget().place(x=320,y=25, height=350, width=310)


	#==========================Analisis Mensual========================
	#Grafica Mensual
	def Grafica_Mensual(self):
		#Frame Distribuidores
		self.Frame_Mensual = Frame(self.root, bg='#F2F2F2', height=412, width=900)
		self.Frame_Mensual.place(x=0, y=101)

		Button(self.Frame_Mensual, image=self.Image_back, bg='#F2F2F2', relief=FLAT, bd=0, activebackground='#F2F2F2', command=self.Destroy_Frame_Mensual).place(x=10, y=10)

		self.Producto_mas_V_Mensual()

		self.Valor_T_Ganancia_Mensual()


	def Destroy_Frame_Mensual(self):
		matplotlib.pyplot.close('all')
		self.Frame_Mensual.destroy()


	#Producto mas vendido del Me
	def Producto_mas_V_Mensual(self):
		#==========================Toma de Datos==============================
		ruta = r'{}\BD'.format(os.getcwd())
		
		archivero = [arch.name for arch in scandir(ruta) if arch.is_file()]

		today = date.today()

		d1 = int(today.strftime("%d"))

		Gestor_Mensual_Nombres = []

		Gestor_Mensual_Cantidad = []

		Control_Archivos = []

		#Toma de Archivos disponibles
		for x in archivero:
			#busqueda del Archivo numericos
			try:
				fecha_busqueda = int(x[0]+x[1])

			except ValueError:
				break

			#Rango de 7 por dias de la semana
			for i in range(31):

				if fecha_busqueda == d1-i :

					Control_Archivos.append(x)

					break


		#Busqueda de Datos
		for x in Control_Archivos:
			#Nombre de la base de Datos Encontrada
			Name = r'{}\BD\{}'.format(os.getcwd(), x)

			#Rango de 31 por dias del Mes
			for i in range(1,32):
				d5 = today.strftime(f'{i}_%m_%Y')

				ubi = f'{d5}_{self.User}.db'
				comparacion = r'{}\BD\{}'.format(os.getcwd(), ubi)

				if Name == comparacion:
					conn = sql.connect(Name)		

					cursor = conn.cursor()

					data = cursor.execute("SELECT * FROM Venta ORDER BY Cantidad DESC ;")


					#Pasar datos encontrados a una Lista
					for x in data:
							Gestor_Mensual_Nombres.append(x[1])
							Gestor_Mensual_Cantidad.append(x[3])

					conn.close()

		
		#Almacen de datos final
		dato_Mensual_cantidad = []

		dato_Mensual_Nombre = []

		#Control de los primeros 10 datos
		Control = 0

		#Obtener los primeros 10 Datos de los arrays Gestores
		for x in Gestor_Mensual_Nombres:

			if Control == 10:
				break
			else:
				dato_Mensual_Nombre.append(x)

			Control += 1

		#Reinicio del control para nuevas tomas de datos
		Control = 0

		#Obtener los primeros 10 Datos de los arrays Gestores
		for x in Gestor_Mensual_Cantidad:

			if Control == 10:
				break
			else:
				dato_Mensual_cantidad.append(x)

			Control += 1

		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Productos mas Vendidos de la Semana')
		
		myexplode = []

		size = len(dato_Mensual_Nombre)

		#Busca exactamente los datos extraidos para evitar errores
		for i in range(size):
			if i == 0:
				myexplode.append(0.1)
			else:
				myexplode.append(0)


		axs.pie(dato_Mensual_cantidad, labels = dato_Mensual_Nombre, startangle=0, shadow = True, explode = myexplode)
		
		canva= FigureCanvasTkAgg(fig, master=self.Frame_Mensual)

		canva.draw()

		canva.get_tk_widget().place(x=-100,y=50)


		self.Gastos_Mensual()


	#Gasto mas alto del Mes
	def Gastos_Mensual(self):
		#==========================Toma de Datos==============================
		ruta = r'{}\BD'.format(os.getcwd())
		
		archivero = [arch.name for arch in scandir(ruta) if arch.is_file()]

		today = date.today()

		d1 = int(today.strftime("%d"))

		Gestor_Mensual_Nombres = []

		Gestor_Mensual_Cantidad = []

		Control_Archivos = []

		#Toma de Archivos disponibles
		for x in archivero:
			#busqueda del Archivo numericos
			try:
				fecha_busqueda = int(x[0]+x[1])

			except ValueError:
				break

			#Rango de 31 por dias del Mes
			for i in range(31):

				if fecha_busqueda == d1-i :

					Control_Archivos.append(x)

					break


		#Busqueda de Datos
		for x in Control_Archivos:
			#Nombre de la base de Datos Encontrada
			Name = r'{}\BD\{}'.format(os.getcwd(), x)

			#Rango de 31 por dias del Mes
			for i in range(1,32):
				d5 = today.strftime(f'{i}_%m_%Y')

				ubi = f'{d5}_{self.User}.db'
				comparacion = r'{}\BD\{}'.format(os.getcwd(), ubi)

				if Name == comparacion:
					conn = sql.connect(Name)		

					cursor = conn.cursor()

					data = cursor.execute("SELECT * FROM Gastos ORDER BY Cantidad DESC ;")


					#Pasar datos encontrados a una Lista
					for x in data:
							Gestor_Mensual_Nombres.append(x[1])
							Gestor_Mensual_Cantidad.append(x[3])

					conn.close()


			

		
		#Almacen de datos final
		dato_Mensual_cantidad = []

		dato_Mensual_Nombre = []

		#Control de los primeros 10 datos
		Control = 0

		#Obtener los primeros 10 Datos de los arrays Gestores
		for x in Gestor_Mensual_Nombres:

			if Control == 10:
				break
			else:
				dato_Mensual_Nombre.append(x)

			Control += 1

		#Reinicio del control para nuevas tomas de datos
		Control = 0

		#Obtener los primeros 10 Datos de los arrays Gestores
		for x in Gestor_Mensual_Cantidad:

			if Control == 10:
				break
			else:
				dato_Mensual_cantidad.append(x)

			Control += 1

		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Productos mas Vendidos de la Semana')
		
		myexplode = []

		size = len(dato_Mensual_Nombre)

		#Busca exactamente los datos extraidos para evitar errores
		for i in range(size):
			if i == 0:
				myexplode.append(0.1)
			else:
				myexplode.append(0)


		axs.pie(dato_Mensual_cantidad, labels = dato_Mensual_Nombre, startangle=0, shadow = True, explode = myexplode)
		
		canva= FigureCanvasTkAgg(fig, master=self.Frame_Mensual)

		canva.draw()

		canva.get_tk_widget().place(x=500,y=50)

		self.Valor_Ganancia_Mensual()

		self.Valor_Perdida_Mensual()


	#Obtener suma total de datos de Ganancia del Mes
	def Valor_Ganancia_Mensual(self):
		#==========================Toma de Datos==============================
		ruta = r'{}\BD'.format(os.getcwd())
		
		archivero = [arch.name for arch in scandir(ruta) if arch.is_file()]

		today = date.today()

		d1 = int(today.strftime("%d"))

		Gestor_Mensual_Precio = []

		Control_Archivos = []

		#Toma de Archivos disponibles
		for x in archivero:
			#busqueda del Archivo numericos
			try:
				fecha_busqueda = int(x[0]+x[1])

			except ValueError:
				break

			#Rango de 31 por dias del Mes
			for i in range(31):

				if fecha_busqueda == d1-i :

					Control_Archivos.append(x)

					break


		#Busqueda de Datos
		for x in Control_Archivos:
			#Nombre de la base de Datos Encontrada
			Name = r'{}\BD\{}'.format(os.getcwd(), x)


			#Rango de 31 por dias del Mes
			for i in range(1,32):
				d5 = today.strftime(f'{i}_%m_%Y')

				ubi = f'{d5}_{self.User}.db'
				comparacion = r'{}\BD\{}'.format(os.getcwd(), ubi)

				if Name == comparacion:
					
									
					conn = sql.connect(Name)		
									
					cursor = conn.cursor()
									
					data = cursor.execute("SELECT sum(PrecioT) FROM Venta ORDER BY Cantidad DESC ;")
									
									
					#Pasar datos encontrados a una Lista
					for x in data:
						Gestor_Mensual_Precio.append(x[0])
															
									
					conn.close()


		self.Ganancia_Mensual = int()

		try:
			for x in Gestor_Mensual_Precio:
				self.Ganancia_Mensual += x

		except TypeError:
			pass


	#Obtener suma total de datos de Perdida del Mes
	def Valor_Perdida_Mensual(self):
		#==========================Toma de Datos==============================
		ruta = r'{}\BD'.format(os.getcwd())
		
		archivero = [arch.name for arch in scandir(ruta) if arch.is_file()]

		today = date.today()


		d1 = int(today.strftime("%d"))

		Gestor_Mensual_Precio = []

		Control_Archivos = []

		#Toma de Archivos disponibles
		for x in archivero:
			#busqueda del Archivo numericos
			try:
				fecha_busqueda = int(x[0]+x[1])

			except ValueError:
				break

			#Rango de 31 por dias del Mes
			for i in range(31):

				if fecha_busqueda == d1-i :

					Control_Archivos.append(x)

					break


		#Busqueda de Datos
		for x in Control_Archivos:
			#Nombre de la base de Datos Encontrada
			Name = r'{}\BD\{}'.format(os.getcwd(), x)


			#Rango de 31 por dias del Mes
			for i in range(1,32):
				d5 = today.strftime(f'{i}_%m_%Y')

				ubi = f'{d5}_{self.User}.db'
				comparacion = r'{}\BD\{}'.format(os.getcwd(), ubi)

				if Name == comparacion:
					
									
					conn = sql.connect(Name)		
									
					cursor = conn.cursor()
									
					data = cursor.execute("SELECT sum(PrecioT) FROM Compra ORDER BY Cantidad DESC ;")
									
									
					#Pasar datos encontrados a una Lista
					for x in data:
						Gestor_Mensual_Precio.append(x[0])
															
									
					conn.close()

									
		self.Perdida_Semanal = int()
									
		try:
			for x in Gestor_Mensual_Precio:
				self.Perdida_Semanal += x
									
		except TypeError:
			pass
				

	#Grafica del Comparador de Gastos y Ganancia Mensual
	def Valor_T_Ganancia_Mensual(self):
		#===============Creacion de la primera Grafica=======================

		fig, axs = plt.subplots( dpi=57, figsize=(9, 5), sharey=False, facecolor='#F2F2F2')

		fig.suptitle('Productos mas Vendidos del Dia')
		
		x = ['Ganancia', 'Perdida']

		colors = ['green', 'red']

		y = [self.Ganancia_Mensual, self.Perdida_Semanal]

		try:
			axs.bar(x, y, color = colors)
		
		except TypeError:
			pass

		canva= FigureCanvasTkAgg(fig, master=self.Frame_Mensual)


		canva.draw()


		canva.get_tk_widget().place(x=320,y=25, height=350, width=310)



#====================================================================================================================================================


#----------------------------------------------Base de Datos-------------------------------------------------------
class Craecion(object):

	def __init__(self, User):
		self.__Data_Base = f'{os.getcwd()}/BD/Datos_General.db'

		self.usuario = User

		self.ruta = r'{}\BD\{}'.format(os.getcwd(), f'{self.usuario}_Logistica.db')
	
		self.Check_ID_user()

	
	#Ver si el usuario tiene su tabla propia creada
	def Check_ID_user(self):
		self.conn = sql.connect(self.__Data_Base)		

		cursor = self.conn.cursor()

		data = cursor.execute(f'SELECT DB FROM Usuarios WHERE Nombre = "{self.usuario}"')

		for x in data:
			if x[0] == 1:
				self.Crear_Tabla_compra()
				
			else:
				pass


		self.Close_Data()
	

	#Eliminar identificador de usuario nuevo
	def Eliminar_Identificador(self):
		self.conn = sql.connect(self.__Data_Base)		

		cursor = self.conn.cursor()

		cursor.execute(f'UPDATE Usuarios SET DB = 0 WHERE Nombre = "{self.usuario}"')

		self.conn.commit()

		self.Close_Data()


	#Crear Tabla Compras
	def Crear_Tabla_compra(self):
		self.conn = sql.connect(self.ruta)		

		cursor = self.conn.cursor()
			
		cursor.execute("""CREATE TABLE "Gastos" (
			"ID"	INTEGER NOT NULL,
			"Gasto"	TEXT NOT NULL,
			"PrecioU"	NUMERIC NOT NULL,
			"Cantidad"	INTEGER NOT NULL,
			"PrecioT"	NUMERIC,
			"Fecha"	TEXT NOT NULL,
			PRIMARY KEY("ID" AUTOINCREMENT)
				);""")
				
		self.conn.commit()

		self.conn.close()

		self.Crear_Tabla_Ventas()


	#Crear Tabla Ventas
	def Crear_Tabla_Ventas(self):
		self.conn = sql.connect(self.ruta)		

		cursor = self.conn.cursor()

		cursor.execute('''CREATE TABLE "Venta" (
		"ID"	INTEGER NOT NULL,
		"Producto"	TEXT NOT NULL,
		"PrecioU"	NUMERIC NOT NULL,
		"Cantidad"	NUMERIC NOT NULL,
		"PrecioT"	NUMERIC,
		"Fecha"	TEXT NOT NULL,
		PRIMARY KEY("ID" AUTOINCREMENT)
			);''')

		self.conn.commit()

		self.Close_Data()

		self.Crear_Tabla_Inventario()


	#Crear Tabla de inventario
	def Crear_Tabla_Inventario(self):
		self.conn = sql.connect(self.ruta)		

		cursor = self.conn.cursor()

		cursor.execute('''CREATE TABLE "Inventario" (
		"ID"	INTEGER NOT NULL,
		"Producto"	TEXT NOT NULL,
		"PrecioU"	INTEGER NOT NULL,
		"Cantidad"	TEXT NOT NULL,
		"PrecioT"	NUMERIC,
		"Fecha"	TEXT NOT NULL,
		"Vendidos"	INTEGER,
		"Agregado"	INTEGER,
		PRIMARY KEY("ID" AUTOINCREMENT)
			);''')

		self.conn.commit()

		self.Close_Data()

		self.Crear_Tabla_Distribuidores()


	#Crear Tabla Distribuidores
	def Crear_Tabla_Distribuidores(self):
		self.conn = sql.connect(self.ruta)		

		cursor = self.conn.cursor()

		cursor.execute('''CREATE TABLE "Distribuidores" (
		"ID"	INTEGER NOT NULL,
		"Empresa"	TEXT NOT NULL,
		"RIF"	TEXT,
		"Direccion"	TEXT,
		"Contacto"	TEXT NOT NULL,
		PRIMARY KEY("ID" AUTOINCREMENT)
			);''')

		self.conn.commit()

		self.Close_Data()

		self.Crear_Tabla_Empleados()


	#Crear Tabla Empleados
	def Crear_Tabla_Empleados(self):
		self.conn = sql.connect(self.ruta)		

		cursor = self.conn.cursor()

		cursor.execute('''CREATE TABLE "Empleados" (
		"ID"	INTEGER NOT NULL,
		"Nombre"	TEXT NOT NULL,
		"Nacimiento"	TEXT NOT NULL,
		"Puesto"	TEXT NOT NULL,
		"Nomina"	TEXT NOT NULL,
		"Nota"		TEXT NOT NULL,
		PRIMARY KEY("ID" AUTOINCREMENT)
			);''')

		self.conn.commit()

		self.Close_Data()

		self.Eliminar_Identificador()


	#Cerrar bases de Datos
	def Close_Data(self):
		self.conn.close()



if __name__ == '__main__':
	Sension()