# To communicate with other elves the device will lock on their signal, which is a series of random characters.

# Create a function for the device to detech a start-of-signal packet.
# The protocol defines these start signals as 4 unqiue characters.
# The subroutine will return how many characters need to be processed before the start marker is found.

def readInput():
	with open("Day-6/inputs.txt", "r") as file:
		return file.read()

def signalReceived(signal, current):
	current.append(signal)
	if len(current) > 4:
		del current[0]

	if len(current) == 4:
		if len(set(current)) == len(current):
			return current, True
	
	return current, False

def main():
	dataStream = readInput()
	current = []
	passes = 0
	found = False

	for signal in dataStream:
		current, found = signalReceived(signal, current)
		passes += 1
		if found:
			break

	print("The start marker was found after:", passes)

main()