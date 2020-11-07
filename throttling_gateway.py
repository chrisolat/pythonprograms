import collections
a = [1,1,1,1,2,2,2,3,3,3,4,4,4,11,11,11,6,6,6,5,5,5]
def droppedRequests(requestTime):
    if len(requestTime) <= 3: return 0
    count = collections.Counter(requestTime)
    
    lookup = collections.defaultdict(int)
    
    for i in range(requestTime[0], requestTime[-1]+1):
        
        lookup[i] = lookup[i-1] + count[i]
    
    for i in range(3, len(requestTime)):
        #print(requestTime)
        temp1 , temp2 = 0, 0
        if requestTime[i]-10 in lookup: temp1 = lookup[requestTime[i]-10]; print(requestTime[i]-10)#;print(lookup); print(temp1)
        if requestTime[i]-60 in lookup: temp2 = lookup[requestTime[i]-60]
        if requestTime[i-3] == requestTime[i]: requestTime[i-3] = '$'
        elif i+1 - temp1 > 20: requestTime[i] = '$'
        elif i+1 - temp2 > 60: requestTime[i] = '$'
    
    return requestTime.count('$')
	
	
print(droppedRequests(a))