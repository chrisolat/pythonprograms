def sum(L):
	print(L)
	if not L:
		return 0
	else:
		return L[0] + sum(L[1:])

print(sum([x for x in range(10)]))