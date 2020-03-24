INITIAL_CAPACITY = 20

class Node:
    def  __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def _hash(self,key):
        hashsum = 0                         #establish hashsum as integer
        for i, j in enumerate(key):
            hashsum += (i +len(key)) ** ord(j)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        """This method establishes the index with internal hash method
        Then it checks the linked list at the index/bucket and sees if the next
        pointer is empty, if it is, then it will create a node and point the previous
        node to the new node, if it is not it will iterate through each other node
        until it finds an empty pointer, then it will establish a new node"""     
        index = self._hash(key)          #use Hash method to save index of key
        node = self.buckets[index]      #establish pointer to node of index
        if node is None:                #if node is empty, then insert
            self.buckets[index] = Node(key, value) #instatiate node 
            return
        #if node is not none, then set it to prev as we will insert new node
        prev = node                     
        while node is not None:         #iterate through each node and setting the next node to prev, if it is not empty
            prev = node
            node = node.next
        #after an 'empty(none)' node is found, the prev or last node will point to a new node being established
        prev.next = Node(key, value)    
        self.size +=1                   #increase size of node count
        
    def find(self, key):
        """Similar to the insert, hash the key value, find the Linked list
        Then check if the node is not none and not equal to the key, iterate until
        you either find the end with no key, or find the key and return the value"""
        index = self._hash(key)          #use Hash method to save index of key
        node = self.buckets[index]      #establish pointer to node of index
        while node is not None and node.key != key:     #iterate non empty nodes and non value matching
            node = node.next
        if node is None:                #if the end is reached, return none
            return None
        else:                           #the node that is equal to key has been found, return value
            return node.value
        
    def remove(self, key):
        index = self._hash(key)          #use Hash method to save index of key
        node = self.buckets[index]      #establish pointer to node of index
        prev = None
        while node is not None and node.key != key:     #iterate non empty nodes and non value matching 
            prev = node                 #saving prev node
            node = node.next            
        if node is None:                #if the end is reached, return None
            return None
        else:
            result = node.value         #save the value of search function
            if prev is None:            #garbage collection if end of node
                self.buckets[index] = node.next
            else:                       #combine linked list so no gap
                prev.next = prev.next.next
            self.size -=1               #decrease size of node count
        
a = HashTable()
a.insert("card", "car")
a.insert("fable", "table")
a.insert("basil", "cat")
a.insert("card1", "car")
a.insert("fable1", "table")
a.insert("basil1", "cat")
a.insert("card2", "car")
a.insert("fable2", "table")
a.insert("basil2", "cat")
a.insert("card3", "car")
a.insert("fable3", "table")
a.insert("basil3", "cat")
