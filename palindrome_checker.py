# Pelindrome Cheker with Deque
from deque import Deque

def check_pal(words):

    pal_d = Deque()

    for word in words:
        pal_d.add_front(word)

    while pal_d.size() > 1:
        if pal_d.remove_front() != pal_d.remove_rear():
            return False
    
    return True


print check_pal("aaaaaaaabbbbbbbbb")
print check_pal("radar")
print check_pal("aabcbaa")

