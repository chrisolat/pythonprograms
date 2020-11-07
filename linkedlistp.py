class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def printlist(self):
		curnode = self.head
		while(curnode):
			print(curnode.data)
			curnode = curnode.next
		
	def append(self, val):
		newnode = Node(val)
		if self.head is None:
			self.head = newnode
			return
		lastnode = self.head
		while(lastnode.next):
			
			lastnode = lastnode.next
		lastnode.next = newnode
	
	def push(self, val):
		newnode = Node(val)
		if(self.head is None):
			self.head = newnode
			return
		curnode = self.head
		newnode.next = curnode
		self.head = newnode
	
	def insert(self, prevnode, val):
		if not prevnode:
			print("previous node does not exist")
			return
		newnode = Node(val)
		newnode.next = prevnode.next
		prevnode.next = newnode
	
	def reverse(self):
		curnode = self.head
		prevnode = None
		while(curnode):
			nextnode = curnode.next
			
			curnode.next = prevnode
			prevnode = curnode
			
			curnode = nextnode
		self.head = prevnode
	
	def merge_lists(self, list1):
		newnode = Node(list1[0])
		self.head = newnode
		node = self.head
		for i in list1[1:]:
			newnode = Node(i)
		self.head.next = newnode
			
		
		
			
	

llist = LinkedList()
llist.append(5)
llist.append(6)
llist.push(4)
llist.insert(llist.head.next, 5)
#llist.reverse()
llist.merge_lists([1,2,3,4])
llist.printlist()
