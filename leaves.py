class Node:

	def __init__(self, value):
		self.value = value
		self.next = None

	def getValue(self):
		return self.value

	def getType(self):
		return self.value.__class__.__name__

	def getName(self):
		return self.value.name

	def setNext(self, nextNode):
		self.next= nextNode

	def getNext(self):
		return self.next

class Carpeta:

	def __init__(self, name):
		self.name = name
		self.branches = ListaEnlazada()

	def add(self, addValue):
		self.branches.add(addValue)

class Archivo:

	def __init__(self, name):
		self.name = name

class ListaEnlazada:

	def __init__(self):
		self.first= None
	
	def add(self, newValue):
		current = self.first
		if current is None:
			self.first = newValue
		else:
			exist= True
			while exist:
				if current.getNext() is None:
					current.setNext(newValue)
					exist= False

				else:
					current = current.getNext()