class SkipListNode():
    def __init__(self, value=None, next=None, previous=None)
        self.value = value
        self.next = next
        self.previous = previous
    
class SkipList():
    """
    Implements a simple Skip List.  
    """
    list_class = SortedLinkedList
    node_class = SkipListNode
    max_layers = 64
    
    def __init__(self, 
    
    def _rand_height(self):
        return random.randint(2, self.max_layers)
    
    def find(self, value):
        layer_offset = 0
        current
