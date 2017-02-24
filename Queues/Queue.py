class Queue:

    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def is_empty(self):
        return self.items == []
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


#q = Queue()

#q.enqueue(99)
#q.enqueue('abc')
#q.enqueue(True)
#q.enqueue(324)

#print q.size()
#print q.dequeue()
#print q.dequeue()
#print q.is_empty()
#print q.size()