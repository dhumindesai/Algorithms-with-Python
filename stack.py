class Stack:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

s = Stack()

#print s.isEmpty()

s.push("abc")
s.push(123)
s.push("hello")

#print s.pop()

#print s.peek()

#print s.size()


## Function to reverse a string using Stack
def rev_string(s):
    chars = list(s)
    s = Stack()
    rev = []

    for c in chars:
        s.push(c)
    
    for i in range(s.size()):
        rev.append(s.pop())
    
    return ''.join(rev)

#print rev_string("Dhrumin")