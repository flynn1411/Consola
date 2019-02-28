# -*- coding: utf-* -*-
from tempArbol import *

class Console:
	# Crea las variables seguirCorriendo y pone el primer directorio
	def __init__(self):
		self.continuar = True
		self.directorioActual = "~"
		self.arbol = Arbol()

    #Setters y getters del directorio actual. Esto se pensó asi para que la función correr
    #sea más dinamica en cuanto a lo que se muestre en la consola.
	def setCurrentDirectory(self, directorioActual):
		self.directorioActual = directorioActual

	def getCurrentDirectory(self):
		return self.directorioActual

	#Esta es la función que se correrá desde main.py, no ocupa parametros y le agrega el
	#parametro a la función correr
	def iniciar(self):
		self.correr("~")

    #La consola siempre debe de ser llamada al final de cada función para que siga corriendo.
    #Esta función revisa constantemente que el comando ingresado no sea 'exit'. Si un comando 
    #es ingresado, este pasará a la función procesar
	def correr(self, directorioActual):
		while self.continuar:
			comando = raw_input("_H4ck3rM4n@NASA:%s$ " %(self.directorioActual))

			if comando == 'exit':
				self.continuar = False

			elif not comando:
				self.continuar = True

			else:
				self.procesar(comando)

	def procesar(self, comando):

		if ' ' in comando:
			partesComando = comando.split(" ")
			self.comando = partesComando[0]

			if self.comandoExiste(comando):
				if (len(partesComando) > 2) and ((partesComando[1] == "-l") or (partesComando[1] == "-r") ):
					self.comando = comando + " " + partesComando[1]
					self.valor = partesComando[2]

				else:
					self.valor = partesComando[1]

			else:
				self.imprimirError(comando, "Inexistente")

		else:
			if self.comandoExiste(comando):
				print "Comando encontrado." #ejecutar(comando) #Aun en construcción
			else:
				self.imprimirError(comando, "Inexistente")

	def imprimirError(self, comando, error):
		#Aun en construcción
		if (error == "Inexistente"):
			print ("%s: comando no encontrado.")%(comando)

	def comandoExiste(self, comando):
		comandosExistentes = ["pwd", "cd", "ls", "ls -l", "touch", "mkdir", "mv", "rm", "rm -r", "find"]

		for i in range (len(comandosExistentes)):

			if (comandosExistentes[i] == comando):
				return True