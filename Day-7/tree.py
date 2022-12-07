class Node:
	def __init__(self, data, parent):
		self._name = data
		self._parent = parent
		self._children = []
		self._fileSize = 0

	def addChild(self, node):
		self._children.append(node)

	def setFileSize(self, size):
		self._fileSize += size

	def getChildren(self):
		return self._children

	def getParent(self):
		return self._parent

	def getName(self):
		return self._name

	def getSize(self):
		return self._fileSize
