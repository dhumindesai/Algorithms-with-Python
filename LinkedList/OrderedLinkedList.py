from Node import Node

class OrderedLinkedList:

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.get_next()
        
        return count
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        
        temp = Node(item)
        if previous == None:
            self.head = temp
            temp.set_next(current)
        else:
            previous.set_next(temp)
            temp.set_next(current)

    
    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() > item:
                stop = True
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() > item:
                stop = True
            elif current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if stop:
            print "The Given item is not in the list"
        elif not found:
            print "The Given item is not in the list"
        elif previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            

#######################################################################################
"""
def print_list(current):
    print "Head = ", current.get_data()
    while current != None:
        print "-> ",current.get_data()
        current = current.get_next()
    print "-> None"

ol = OrderedLinkedList()

ol.add(55)
ol.add(33)
ol.add(22)
ol.add(44)
ol.add(1)
ol.add(46)
ol.add(30)

print_list(ol.head)

ol.remove(55)

print_list(ol.head)

print ol.size()
"""