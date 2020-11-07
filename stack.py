class stack:
	def __init__(self):
		self.items = []
	
	def push(self, data):
		self.items.append(data)
	
	def pop(self):
		return self.items.pop()
	
	def get_stack(self):
		return self.items
	
	def is_empty(self):
		return self.items == []
	
	def peek(self):
		if not self.is_empty():
			return self.items[-1]

s = stack()
s.push("A")
s.push("B")
print(s.get_stack())		