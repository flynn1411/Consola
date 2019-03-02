# -*- coding: utf-* -*-

"""
[Versión 2.0]: 
     -Se le cambia el idioma de las funciones de español a ingles para
      que todo el programa sea coherente con las otras clase.
     -Se implementan funciones con la clase Arbol.
     -Mejor manejo de impresión de errores.
     -Creación de funciones extra para alivianar otras funciones con 
      la repetición de instrucciones

[Versión 2.5]:
    -Algunos cambios en base a prueba y error.
    -Reestructuración de algunas funciones y sus operaciones en base
     a recomendaciones dadas.
    -Trabajé esto en Windows y no en la maquina virtual asi que por eso
     hago este commit, para poder seguir trabajando en Ubuntu.

[Versión 3.0]:
    -Completación de la función execute(), lista para ser implementada
     con clase arbol.
    -Adición de función exitMessage(), para dar un mensaje de salida.
     En esta se agregó un arreglo con diferentes mensajes de salida para 
     que no sea lo mismo.
    -Adición de mensaje de bienvenida al usuario.
"""
from tempArbol import *
import random

class Console:
	# Crea las variables seguirCorriendo y pone el primer directorio
	def __init__(self):
		self.keepRunning = True
		self.currentDirectory = "~"
		self.tree = Arbol()
		self.command = None
		self.value = None

	"""
       Setters y getters del directorio actual. Esto se pensó asi para que la función run
       sea más dinamica en cuanto a lo que se muestre en la consola.
    """
	def setCurrentDirectory(self, currentDirectory):
		self.currentDirectory = tree.getBranches() #Aun no está en su uso optimo

	def getCurrentDirectory(self):
		return self.currentDirectory

	"""
	   Esta es la función que se correrá desde main.py, no ocupa parametros y le agrega el
	   parametro a la función run()
	"""
	def start(self):

		bootMessage = """/
		:'######:::'#######::'##::: ##::'######:::'#######::'##::::::::::'###::::
		'##... ##:'##.... ##: ###:: ##:'##... ##:'##.... ##: ##:::::::::'## ##:::
		 ##:::..:: ##:::: ##: ####: ##: ##:::..:: ##:::: ##: ##::::::::'##:. ##::
		 ##::::::: ##:::: ##: ## ## ##:. ######:: ##:::: ##: ##:::::::'##:::. ##:
		 ##::::::: ##:::: ##: ##. ####::..... ##: ##:::: ##: ##::::::: #########:
		 ##::: ##: ##:::: ##: ##:. ###:'##::: ##: ##:::: ##: ##::::::: ##.... ##:
		. ######::. #######:: ##::. ##:. ######::. #######:: ########: ##:::: ##:
		:......::::.......:::..::::..:::......::::.......:::........::..:::::..::
		"""

		print bootMessage

		self.run("~")

	"""
	   La consola siempre debe de ser llamada al final de cada función para que siga corriendo.
       Esta función revisa constantemente que el comando ingresado no sea 'exit'. Si un comando 
       es ingresado, este pasará a la función process()
     """
	def run(self, currentDirectory):
		while self.keepRunning:
			#self.currentDirectory = arbol.getAbsolutePath()
			command = raw_input("\n  H4ck3rM4n@NASA:%s$ " %(self.currentDirectory))

			if command == 'exit':
				self.keepRunning = False
				self.exitMessage()

			elif not command:
				self.keepRunning = True

			else:
				self.process(command)

	"""
	   process() obtiene el comando ingresado por el usuario, verifica si es un comando valido y 
	   procede a 'empaquetar' la instrucción junto con el valor(o parametro o path) para su debida
	   ejecución
	"""
	def process(self, command):

		self.commandParts = command.split(" ")

		#Lo ingresado por el usuario tiene mas de una palabra?
		if (len(self.commandParts) > 1):
			#¿Existe?
			if self.commandExists(self.commandParts[0]):
				#¿Es 'ls -l' con parametros o es 'rm -r' con parametros?
				if (len(self.commandParts) > 2) and (((self.commandParts[1] == "-l") or (self.commandParts[1] == "-r"))):
					self.command = self.commandParts[0] + " " + self.commandParts[1]
					self.value = self.commandParts[2]

				#¿Es 'ls -l' sin parametros?
				elif (len(self.commandParts) == 2) and (self.commandParts[1] == "-l"):
					self.command = self.commandParts[0] + " " + self.commandParts[1]
					self.execute(command)

				#¿Es 'rm -r' y no tiene parametros? Entonces tirar error.
				elif (len(self.commandParts) == 2) and (self.commandParts[1] == "-r"):
					self.printException("rm -r no param")#Se necesita un parametro y se le indica al usuario

				#Si existe el comando y no son los otros casos, pasa a ejecución
				else:
					self.command = self.commandParts[0]
					self.value = self.commandParts[1]
					self.execute(self.command, self.value)

			#Si no existe el comando se le indica al usuario
			else:
				printException(self.commandParts[0], "Inexistente")

		#Si lo dado por el usuario es solamente un comando, se verifica que existe y se ejecuta
		else:
			if self.commandExists(self.commandParts[0]):
				self.execute(command)

			else:
				self.printException(command, "Inexistente")

	"""
	   execute() puede o no puede recibir el parametro valor, esto depende del comando dado.
	   las funciones ya vienen "empaquetadas" por la funcion process(). Dependiendo del comando
	   que el usuario escribe, se revisará si los parametros son los indicados (si fueron dados)
	   y al final dará un mensaje de exito o de error para hacerle saber al usuario del estado
	   de su instrucción.
	"""
	def execute(self, command, value = None):
		self.value = value

		if (self.command == "pwd"):
			self.tree.getBranches()
			print "Completado"

		elif (self.command == "cd"):
			pass

		elif (self.command == "ls"):
			pass

		elif (self.command == "ls -l"):
			pass

		elif (self.command == "touch"):
			self.tree.add(value, "-a")
			print ("Archivo %s exitosamente creado.")%(value)

		elif (self.command == "mkdir"):
			self.tree.add(value, "-c")
			print ("Carpeta %s exitosamente creada.")%(value)


		elif (self.command == "mv"):
			pass

		elif (self.command == "rm"):
			pass

		elif (self.command == "rm -r"):
			pass

		elif (self.command == "find"):
			pass

	"""
	   printException() recibe el comando (si este no existe incluso) y el tipo de error.
	   al encontrar el caso especifico, se le da un mensaje especifico al error, simulando
	   una terminal de Linux
	"""
	def printException(self, command, exception):
		#Aun en construcción
		if (exception == "Inexistente"):
			print ("%s: comando no encontrado.")%(command)

		elif (exception == "rm -r no param"):
			print ("%s: operando restante. Ingrese parametros si desea utilizar rm -r.")%(command)

	"""
	   commandExists() revisa si el comando dado por el usuario es un comando existente
	   y disponible para su uso. Comandos existentes están ubicados en un arreglo para 
	   mayor conveniencia.
	"""
	def commandExists(self, command):
		existingCommands = ["pwd", "cd", "ls", "ls -l", "touch", "mkdir", "mv", "rm", "rm -r", "find"]

		for i in range (len(existingCommands)):

			if (existingCommands[i] == command):
				return True

	def exitMessage(self):
		messages = ["Enviando misiles nucleares, gracias por hackear con nostros :v",
		            "End of Line.", "Mission Failed. We'll get them next time.",
		            "All you had to do was follow the damn train, CJ!"
		           ]

		pick = random.randrange(4)

		print ("\n*\ %s \*\n\n")%(messages[pick])
