class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next
    
"""
n = Node(44)
print n.get_data()
print n.get_next()
 
n.set_data(13)
n.set_next(3)

print n.get_data()
print n.get_next()
"""