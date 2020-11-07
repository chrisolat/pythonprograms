array = [1,4,52,1,5,624,56,7,42,5,67,3,23,6,7,3,13,35,5,6,7,68,9,7,564,54,23,6,4]
target = int(input("Enter Target: "))
array = sorted(array)

def binary_search(array, target):
	low = 0
	high = (len(array) - 1)
	while(low <= high):
		mid = (low + high) // 2
		if target == array[mid]:
			return "Found"
		elif target < array[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return "Not Found"

#not binary search	
def finduppercase():
	string = input("Enter String: ")
	for i in range(len(string)):
		if(string[i].isupper()):
			return "Found " + string[i]
	return "Not Found"
	

def closestnumber(array, target):
	print(array)
	low = 0
	high = len(array) - 1
	clsnum = array[high]
	if target > array[high]:
		return array[high]
	if target < low:
		return low
	while(low <= high):
		mid = (low+high) // 2
		mindiff = 10000
		if(target == array[mid]):
			return "Found perfect"
		left = array[mid-1]
		right = array[mid+1]
		if((abs(left-target))<mindiff):
			mindiff = abs(left-target)
			clsnum = left
			
		if((abs(right-target)) < mindiff):
			mindiff = abs(right - target)
			clsnum = right
		if(target < array[mid]):
			high = mid - 1
		elif(target > array[mid]):
			low = mid + 1
	return clsnum
		
#print(binary_search(array, target))
#print(finduppercase())
#print(closestnumber(array, target))

def fixedpoint():
	A = [0,2,5,8,17]
	A = sorted(A)
	low = 0
	high = len(A) - 1
	while(low <= high):
		mid = (low+high) // 2
		if mid == A[mid]:
			return mid
		if(mid < A[mid]):
			high = mid - 1
		else:
			low = mid + 1
	return "False"

#print(fixedpoint())

def bitonicpeak():
	A = [1,2,3,4,3,2,1]
	low = 0
	high = len(A) - 1
	while(low <= high):
		mid = (low+high) // 2
		
		if(A[mid] > A[mid - 1] and A[mid] > A[mid + 1]):
			return A[mid]
		elif(A[mid - 1] > A[mid]):
			high = mid - 1
		else:
			low = mid + 1
	return False
print(bitonicpeak())