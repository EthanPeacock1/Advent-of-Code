from tree import Node

def readInputs():
	with open("Day-7/inputs.txt", "r") as file:
		data = file.read().replace("$ ", "").splitlines()
	return data

def createTree(data):
	rootNode = Node("/", None)
	currentNode = rootNode
	first = True

	for d in data:
		if first:
			first = False
		else:
			instruction = d.split(" ")
			match instruction[0]:
				case "cd":
					if instruction[1] == "..":
						currentNode = currentNode.getParent()
					else:
						childNode = Node(instruction[1], currentNode)
						currentNode.addChild(childNode)
						currentNode = childNode
				case "ls":
					pass
				case "dir":
					pass
				case _:
					currentNode.setFileSize(int(instruction[0]))
	
	return rootNode

answer = 0
def postOrder(node):
	global answer
	
	nodeChildren = node.getChildren()
	nodeSize = node.getSize()
	nodeParent = node.getParent()

	if len(nodeChildren) > 0:
		for child in nodeChildren:
			postOrder(child)

	if nodeSize <= 100000:
		answer += nodeSize
	
	if nodeParent != None:
		nodeParent.setFileSize(nodeSize)

def main():
	global answer

	instructions = readInputs()
	root = createTree(instructions)

	postOrder(root)

	print(answer)

main()