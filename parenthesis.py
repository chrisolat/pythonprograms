s = "{[]}()"
def parenthesis(s):
	openp = []
	open = "{[("
	index = 0
	while(index < (len(s))):
		print(s[index])
		if s[index] in open:
			openp.append(s[index])
		else:
			if (openp == []):
				return False
			else:
				popped = openp.pop()
				if popped == "(" and s[index] == ")":
					pass
				elif popped == "{" and s[index] == "}":
					pass
				elif popped == "[" and s[index] == "]":
					pass
				else:
					return False
		
		index += 1
	
	if openp == []:
		return True
	return False

print(parenthesis(s))