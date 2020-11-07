class Queue:

	def __init__(self):
		self.items = []
	
	def enqueue(self, data):
		self.items.insert(0, data)
	
	def dequeue(self):
		return self.items.pop()
		
	
	
	
class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class Binarytree:
	
	def __init__(self, root):
		self.root = Node(root)
	
	def printtree(self):
		queue = Queue()
		queue.enqueue(self.root)
		tranversal = ''
		
		while(len(queue.items) > 0):
			nextout = queue.dequeue()
			tranversal += str(nextout.data) + '-'
			if(nextout.left):
				queue.enqueue(nextout.left)
			if(nextout.right):
				queue.enqueue(nextout.right)
		return tranversal
		
tree = Binarytree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.printtree())