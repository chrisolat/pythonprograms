class Stack:
	def __init__(self):
		self.items = []
	def push(self, data):
		self.items.append(data)
	def pop(self):
		return self.items.pop()
class Queue:

	def __init__(self):
		self.items = []
	
	def enqueue(self, data):
		self.items.insert(0, data)
	
	def dequeue(self):
		return self.items.pop()
		
	def peek(self):
		if len(self.items) != 0:
			return self.items[-1]
		return []
class Node:
	
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
class Binarytree:
	def __init__(self, data):
		self.root = Node(data)
		
		
	def printsizetree(self):
		queue = Stack()
		count = 1
		nextout = self.root
		queue.push(nextout)
		
		
		
		while(queue.items):
			nextout = queue.pop()
			
			if(nextout.left):
				count += 1
				queue.push(nextout.left)
			if(nextout.right):
				count += 1
				queue.push(nextout.right)
		return count

tree = Binarytree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.printsizetree())