with open('Day-7/inputs.txt', 'r') as file:
    lines = file.read().splitlines()

def part1():

    directories = {}
    listOfDirectories = []
    currentDirectory = ''
    total = 0

    for line in lines:

        if '$ cd' in line and '..' not in line:
            dir = line.removeprefix('$ cd ')
            currentDirectory += dir
            if currentDirectory not in directories:
                directories[currentDirectory] = []
            listOfDirectories.append(dir)

        elif '$ cd' in line and '..' in line:
            currentDirectory = currentDirectory.removesuffix(listOfDirectories[len(listOfDirectories)-1])
            listOfDirectories.pop(len(listOfDirectories)-1)

        elif '$ cd' not in line and '$ ls' not in line:
            if 'dir' in line:
                dir = line.removeprefix('dir ')
                directories[currentDirectory + dir] = []
            else:
                size, name = line.split()
                directories[currentDirectory].append((int(size), name))

    totalSize = {directory : 0 for directory in directories}

    for directory in directories:
        for item in directories[directory]:
            if type(item) == tuple:
                totalSize[directory] += item[0]

    for key in totalSize.keys():
        for directory in directories:
            if key in directory and key != directory:
                totalSize[key] += totalSize[directory]

    for directory in totalSize:
        if totalSize[directory] < 100000:
            total += totalSize[directory]

    print(f"Part 1 result : {total}")
    return totalSize
    
def part2(totalSize):

    emptySpace = 70000000 - max(totalSize.values())
    spaceNeeded = 30000000 - emptySpace

    temp = []
    
    for directory in totalSize:
        if totalSize[directory] >= spaceNeeded:
            temp.append(totalSize[directory])

    print(f"Part 2 result : {min(temp)}")

part2(part1())