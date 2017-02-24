# Abstracr Impletation of Deque

class Deque:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0,item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
"""
d = Deque()
d.add_front(1)
d.add_front(2)
d.add_front(3)
d.add_rear(4)
d.add_rear(5)

print d.items
print d.size()
print d.is_empty()

d.remove_front()
d.remove_rear()

print d.items
"""