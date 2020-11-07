def tester(start):
	def nested(label):
		nested.state = start
		print(label, nested.state)
		nested.state += 1
	
	return nested