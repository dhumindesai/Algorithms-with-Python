## Find k smallest numbers in the list 
## O(nk) complexity

def find(l,k):
    l2 = l
    ans = []
    for i in range(k):
        l1= l2[:k]
        minNum = l1[i]   
        j = i+1
        idx = i
        while j < len(l2):
            if l2[j] < minNum:
                minNum = l2[j]
                idx = j
            j = j+1
        
        l2[idx] = l1[i]
        ans.append(minNum)
    return ans

print find([2,7,4,1,4,9,0,5,7,9,7,5,3,2,5,8,9,5,3,2,6,8,9],3)