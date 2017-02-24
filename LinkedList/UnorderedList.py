from Node import Node

class UnoderedList:

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.get_next()
        
        return count
    
    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        
        return found
    
    def remove(self, item):
        current = self.head
        found = False 
        previous = None

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if not found:
            print "No item found to be romoved"
        elif previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


##################################
"""
def print_list(current):
    print "Head = ", current.get_data()
    while current != None:
        print "-> ",current.get_data()
        current = current.get_next()
    print "-> None"

ul = UnoderedList()

ul.add(8)
ul.add(5)
ul.add(3)
ul.add(1)
ul.add(23)

print_list(ul.head)
print ul.search(5)
print ul.search(39)
ul.remove(23)
print_list(ul.head)
ul.remove(8)
print_list(ul.head)
"""


    
