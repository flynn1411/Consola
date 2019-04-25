from branches import*

class Arbol:

	def __init__(self):
		self.root = Node(Carpeta("/"))
		self.currentNode= self.root
		self.currentPath= self.getRoot()

	def getRoot(self):
		return self.root.getName()

	def add(self, addValue, _type):
		new= None

		if _type == "-c":
			new= Node(Carpeta(addValue))
		else:
			new= Node(Archivo(addValue))

		self.currentNode.getValue().add(new)

	def setCurrent


def loadTreeStructure(self, path, treeWidget):
	tree = Arbol()

		# Para cada cosa que exista en path
	try:
		for file in os.listdir(path):
			file_path= path + '/' + file

			if os.path.isdir(file_path):
				tree.add(file, "-c")
				tree.setCurrent(file)
				self.loadTreeStructure(file_path, treeItem)
			
			else:
				tree.add(file, "-a")

		except Exception as e:
			print 'Exception: ', e
			# Nada mas para evitar que no se muera
