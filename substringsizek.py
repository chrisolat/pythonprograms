
def Substrings(s, k):
	ans = []
	if s == "" or k < 1:
		return []
	for i in range(2):
		
		c1 = 0
		c2 = k 
		while(c2 < len(s)):
			substring = s[c1:c2]
			
					
			if substring not in ans:
			
				ans.append(substring)
			
			
			c1+=1
			c2+=1
	return ans
	

s = "awaglknagawunagwkwagl"
k = 4
print(Substrings(s,k))
				
		
		