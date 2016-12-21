import time
def findMin_1(lNum):
    if len(lNum) == 0:
        return "there is no element"
    min = lNum[0]
    for i in range(len(lNum)):
        if lNum[i] < min: min = lNum[i]
    
    return min

def findMin_2(lNum):
    if len(lNum) == 0:
        return "there is no element"
    for i in range(len(lNum)):
        flag = 0
        for j in range(len(lNum)):
            if lNum[i] <= lNum[j]: flag = flag + 1
        if flag == len(lNum): return lNum[i]

print findMin_2([4,4,4,4,4,4,4,44,4,4,4,4])