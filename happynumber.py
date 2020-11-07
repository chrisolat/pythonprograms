def isHappy(n) -> bool:
        ns = str(n)
        array = []
        sum = 0
        isfound = False
        count = 1
        while(not isfound):
            for i in ns:
                sum += int(i)**2
            if sum == 1:
                isfound = True
            ns = str(sum)
            #print(ns)
            sum = 0
            count += 1
            if(count == 100): break

        return isfound
for i in range(1000):
	if(isHappy(i)): print("Happy Number: ",i)
