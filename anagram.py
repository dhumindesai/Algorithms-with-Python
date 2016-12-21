## anagram function with the complexity of O(n)

import timeit
from timeit import Timer

def isAnagram(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    i=0
    while i < len(s1):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos]+1
        i = i+1
    
    i=0
    while i < len(s2):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos]+1
        i = i+1

    j=0
    while j<26:
        if c1[j] != c2[j]: return False
        j = j+1
    
    return True

t1 = Timer("isAnagram('adssmjkhfjkdshkfjghsdkjhfksam','ssmasiuhhhggggghghghghhghghghghghghghhgdfjksdhfksdhfhdskfjdhsmda')", "from __main__ import isAnagram")
print t1.timeit(number=1000), "milliseconds"
#print isAnagram("adssmam","ssmamda")