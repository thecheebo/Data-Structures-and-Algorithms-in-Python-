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
    
    def hash(self,key):
        hashsum= 0 
        for idx, c in enumerate(key):
            hashsum +=(idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum
    
    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)
        
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value
        
    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            prev = node  
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result

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
