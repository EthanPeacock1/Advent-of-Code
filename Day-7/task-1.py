# Given a set of instructions, the inputs.txt, create the file structure.
# Directories have no file size, other files do.

# Find the directories with at most 100,000 file size, and sum all the directories that meet this.

from tree import Node

def readInputs():
    with open("Day-7/inputs.txt", "r") as file:
        data = file.read().replace("$ ", "").splitlines()
    return data

def createTree(data):
    root = None
    currentNode = None
    createdDirNodes = []
    createdNodes = []

    for d in data:
        instruction = d.split(" ")
        # print(d)
        match instruction[0]:
            case "cd":
                if instruction[1] == "..":
                    if currentNode.getName() != "/":
                        currentNode = currentNode.getParent()
                else:
                    if instruction[1] not in createdDirNodes:
                        if currentNode == None:
                            newNode = Node(instruction[1], None)
                        else:
                            newNode = Node(instruction[1], currentNode.getParent())
                        if root == None:
                            root = newNode
                        if currentNode != None:
                            currentNode.addChild(newNode)
                        createdDirNodes.append(instruction[1])
                        createdNodes.append(newNode)
                        currentNode = newNode
                        # print(newNode)
                    else:
                        currentNode = createdNodes[createdDirNodes.index(instruction[1])]
                        # print("-- test --")
                        # print(d)
                        # print(currentNode._name)
                        # print(len(createdDirNodes))
                        # print(len(createdNodes))
                        # print("----------")
            case "ls":
                pass
            case _:
                if instruction[0] == "dir":
                    if instruction[1] not in createdDirNodes:
                        newNode = Node(instruction[1], currentNode)
                        currentNode.addChild(newNode)
                        createdDirNodes.append(instruction[1])
                        createdNodes.append(newNode)
                else:
                    newNode = Node(instruction[1], currentNode)
                    currentNode.addChild(newNode)
                    newNode.setFileSize(instruction[0])
    
    return root

total = 0
totals = []

def postOrder(root):
    global total
    global totals
    for child in root.getChildren():
        postOrder(child)
    if (total + int(root.getSize())) > 100000:
        totals.append(total)
        total = int(root.getSize())
    else:
        total += int(root.getSize())
        print(total)

def main():
    global total
    global totals
    instructions = readInputs()   
    root = createTree(instructions)
    postOrder(root)
    endTotal = total
    for t in totals:
        endTotal += t
    print(endTotal)

main()