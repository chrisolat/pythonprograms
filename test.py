"""x = 99
def f1():
	x = 88
	def f2():
		print(x)
	return f2()
f1()"""

"""def maker(n):
	def action(x):
		return x ** n
	return action"""
	
def maker(n):
	return def action(x):
				x ** n
maker(4)