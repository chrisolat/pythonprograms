
def ispalindrom():
	s = "Was t a cat I saw?"
	s = s.lower().replace(" ", "")
	s = [i for i in s if i.isalpha()]
	s = "".join(s)
	low = 0
	high = len(s) - 1
	for i in range(len(s)):
		if(s[i] != s[~i]):
			return "Not palindrome"
	return "palindrome"
	
#print(ispalindrom(s))

def isanagram():
	s1 = "fairy tales"
	s2 = "rail safety"
	s1 = s1.lower().replace(" ", "")
	s2 = s2.lower().replace(" ", "")
	s1 = sorted(s1)
	s2 = sorted(s2)
	if s1 != s2:
		print("not anagram")
	else:
		print("anagram")
		
isanagram()