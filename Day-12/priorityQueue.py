class PriorityQueue(object):
	def __init__(self):
		self.queue = []
 
	def isEmpty(self):
		return len(self.queue) == 0
 
	def insert(self, data):
		self.queue.append(data)
 
	def delete(self):
		min_val = 0
		for i in range(len(self.queue)):
			if self.queue[i][2] < self.queue[min_val][2]:
				min_val = i
		item = self.queue[min_val]
		del self.queue[min_val]
		return item