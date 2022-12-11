# Worry levels no longer divided by 3
# 10,000 rounds

from math import trunc, prod

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
			modulo = prod(m._test for m in monkeys)
			item = self._calcWorryLevel(item, modulo)
			newMonkey = self._testWorryLevel(item)
			monkeys[newMonkey].addItem(item)
			index += 1
			self.inspected += 1
		self._items = []

	def _calcWorryLevel(self, item, modulo):
		operation = "old " + self._operation + " " + self._opVal
		return eval(operation, {"old": item}) % modulo

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

	for r in range(10000):
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