class MyNode:
    def __init__(self, value, n = None):
        self.value = value
        self.next = n


class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26
    
    def my_hash(self, word):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        return alpha.index(word[0])
    
    def insert(self, word):
        key = self.my_hash(word)
        newNode = MyNode(word)
        iterator = self.buckets[key]
        if self.buckets[key] == None:
            self.buckets[key] = newNode
        else:
            while iterator.next != None:
                iterator = iterator.next 
            iterator.next = newNode
        #use my_hash to find array index
        #create node, add node to head of linked list bucket
        

    def find(self,word):
        key = self.my_hash(word)
        iterator = self.buckets[key]
        while iterator!= None:
            if iterator.value == word:
                return key 
            iterator = iterator.next
        return None
        

        #use my_hash to find array index, save key
        #search through linked list bucket to find value
        #return key for that value if found
        #return [None]
        



h = MyHashTable()
h.insert('barry')
h.insert('bob')
h.insert('barb')
h.insert('adam')
h.insert('abby')

print h.buckets

print h.find('adam')
print h.find('abby')
print h.find('barb')
print h.find('bill')
print h.find('jill')