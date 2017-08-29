# binary: base 2
#1100
#1x2^3 + 1x2^2 + 0x2^1 + 1x2^0

#convert these binary numbers: 1,11,111,101,10101 to base 10
#1 -> 1
#11 -> 3
#111 -> 7
#101 -> 5
#10101 -> 21

#1 -> 1x2^0 = 1
#2 -> 1x2^1 x 1x2^0= 10
#7 -> 1x2^2 +  1x2^1 + 1x2^0= 111
#11 -> 1x2^3 + 0x2^2 + 1x^2^1 + 1x2^0 = 1011
#64 -> 1x2^6 = 1000000
#63 -> 111111
#128 -> 1x2^7 = 10000000
#129 -> 10000001

#how is memory structured? RAM
#what is a bit vs byte?
#bit: 0 or 1
#byte: 8 bits

#arrays 
#all items need to be next to each other in memory. 
#All data will need to be moved if there is not enough room for an element appeneded or an element is removed.
#constant time to access item
#at worst, linear time to insert/delete

#linked lists
#--singly
#--doubly
#each node has a value and the memory address of the next node
#to access a certain "index", you'll have to loop through and check each node to find your item
#constant time to insert and delete nodes
#at worst, linear time to access item

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

n1 = Node(5)
n2 = Node(4)
n1.next = n2
print(n1.next.value)        

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value): 
        #if head and tail or none, 
        # if true: assign head and tail to new value
        # if false: assign new node to current tail's next property and reassign current tail to new node
        
        pass
    
    def delete(self, value):
        pass
    
    def exists(self, value):
        pass  
