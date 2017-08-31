class Node:
    def __init__(self, value, previous = None):
        self.value = value
        self.previous = previous


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
        self.first = self.first.previous
        return node_to_remove

    def enqueue(self, value):
        #add new node to end of queue
        new_node = Node(value)
        self.first = new_node
        return self

