class Node:
    def __init__(self, value, previous = None):
        self.value = value
        self.previous = previous

#first in first out. enqueue end, dequeue beginning


class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def peek(self):
        #return next node
        return self.first
        

    def dequeue(self):
        #return next node and remove from queue
        node_to_remove = self.first
        if node_to_remove == self.last:
            self.last = None
            self.first = None
        else:
            self.first = self.first.previous
        return node_to_remove

    def enqueue(self, value):
        #add new node to end of queue
        new_node = Node(value)
        if self.first == None and self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.previous = new_node    
            self.last = new_node
        
queue = MyQueue()
queue.enqueue(1)
queue.enqueue(5)
print(queue.dequeue().value)
print(queue.dequeue().value)