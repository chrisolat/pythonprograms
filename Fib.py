def F(n):
	
	if (n == 0) or (n == 1):
		return n
	else:
		print(n ,"-1 ", n, "-2 ")
		return F(n-1)+F(n-2)

def fibonacciVal(n):
	memo = []
	memo[0], memo[1] = 0, 1
	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[n]

n = int(input("Enter: "))
#print(F(n))
print(fibonacciVal(n))