# To get your stuff back you need to predict where the monkeys will throw your items.
# You observe they operate based on how worried you are about the item.
# You make notes, the inputs, on the items the monkey has, how worried you are about them, and how they make the decisions based on your worry level

# Each monkey has several attributes:
	# Starting items: lists your worry level for each item the monkey is holding, in the order they are inspected
	# Operation: shows how your worry level changes as that monkey inspects the item
	# Test: shows how the monkey will use your worry level to throw the item to another monkey

# After each monkey inspects an item, but before it tests your owrry level, your worry level is divided by 3 rounded down to the nearest int
# Monkeys take turns, rounds, to inspect and throw all items in the given order.
# When a monkey throws to another, it is added to the end of the recieving monkeys list.
# If a monkeys turn comes and it has no items, the next round begins

# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds.
# Multiply the most 2 active monkeys total items inspected.

from math import trunc

monkeys = []

class Monkey:
	def __init__(self, items, opVal, op, test, testTrue, testFalse):
		self._items = [int(item) for item in items]
		self._opVal = opVal
		self._operation = op
		self._test = test
		self._testTrue = testTrue
		self._testFalse = testFalse
		self.inspected = 0
	
	def inspectItems(self):
		index = 0
		for item in self._items:
			item = self._calcWorryLevel(item)
			item = self._boredDivide(item)
			newMonkey = self._testWorryLevel(item)
			monkeys[newMonkey].addItem(item)
			index += 1
			self.inspected += 1
		self._items = []

	def _calcWorryLevel(self, item):
		match self._operation:
			case "+":
				if self._opVal == "old":
					item += item
				else:
					item += int(self._opVal)
			case "-":
				if self._opVal == "old":
					item -= item
				else:
					item -= int(self._opVal)
			case "*":
				if self._opVal == "old":
					item *= item
				else:
					item *= int(self._opVal)
			case "/":
				if self._opVal == "old":
					item = item / item
				else:
					item = item / int(self._opVal)
		return item

	def _boredDivide(self, item):
		return trunc(item / 3)

	def _testWorryLevel(self, item):
		if (item % self._test) == 0:
			return self._testTrue
		else:
			return self._testFalse

	def addItem(self, item):
		self._items.append(item)

	def getItems(self):
		return self._items

def readInputs():
	global monkeys
	with open("Day-11/inputs.txt", "r") as file:
		data = file.read().split("\n\n")
	temp = []
	for d in data:
		tempMonkey = []
		lines = d.split("\n")
		for line in lines:
			line = line.strip()
			words = line.split(" ")
			match words[0]:
				case "Monkey":
					pass
				case "Starting":
					line = line.replace("Starting items: ", "")
					tempMonkey.append(line.split(", "))
				case "Operation:":
					line = line.replace("Operation: new = old ", "").split(" ")
					tempMonkey.append(line[1])
					tempMonkey.append(line[0])
				case "Test:":
					line = line.replace("Test: divisible by ", "")
					tempMonkey.append(int(line))
				case "If":
					if words[1] == "true:":
						line = line.replace("If true: throw to monkey ", "")
						tempMonkey.append(int(line))
					else:
						line = line.replace("If false: throw to monkey ", "")
						tempMonkey.append(int(line))
		newMonkey = Monkey(tempMonkey[0], tempMonkey[1], tempMonkey[2], tempMonkey[3], tempMonkey[4], tempMonkey[5])
		monkeys.append(newMonkey)

def main():
	global monkeys
	readInputs()

	for r in range(20):
		for monkey in monkeys:
			monkey.inspectItems()

	total = 0
	monkeyInspections = []
	for monkey in monkeys:
		print(monkey.getItems())
		monkeyInspections.append(monkey.inspected)
	
	monkeyInspections.sort(reverse=True)
	total = monkeyInspections[0] * monkeyInspections[1]

	print("Monkey business: ", total)

main()