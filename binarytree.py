class Stack:

	def __init__(self):
		self.items = []
	
	def push(self, data):
		self.items.append(data)
	
	def pop(self):
		if self.is_empty():
			return []
		return self.items.pop()
	
	def peek(self):
		if self.is_empty():
			return []
		return self.items[-1]
		
	def is_empty(self):
		return self.items == []
	
	def __len__(self):
		return len(self.items)

class Queue:

	def __init__(self):
		self.items = []
	
	def enqueue(self, data):
		self.items.insert(0, data)
		
	def dequeue(self):
		if not self.is_empty():
			return self.items.pop()
		
	def is_empty(self):
		return self.items == []
		
	def peek(self):
		return self.items[-1]
		
	def __len__(self):
		return len(self.items)
	
class Node:
	
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class binarytree:
	
	def __init__(self, root):
		self.root = Node(root)
	
	def print_tree(self, root):
		if root is None:
			return
		
		queue = Queue()
		queue.enqueue(root)
		
		tranversal = ""
		while(len(queue) > 0):
			
			node = queue.dequeue()
			tranversal += str(node.data) + '-'
			
			if node.left:
				queue.enqueue(node.left)
			if node.right:
				queue.enqueue(node.right)
		
		return tranversal
		
		
tree = binarytree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.print_tree(tree.root))