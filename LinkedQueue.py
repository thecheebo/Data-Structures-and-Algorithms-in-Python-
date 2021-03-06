"""
╔═══════════════╗
║  Description  ║
╚═══════════════╝
    > LinkedQueue w/Singly Linked Lists
        • First in - First out
╔══════════════╗
║  Attributes  ║
╚══════════════╝
    > Node
        • Data/Element
        • Next Linked Node
    > Linked Queue
        • Head Location
        • Tail Location
        • Size
╔══════════════╗
║  Operations  ║
╚══════════════╝
    > LinkedList
        • Add Node to top
        • Remove top node
        • Return top
        • Empty check
        • Size Of List
╔══════════════╗
║  Complexity  ║
╚══════════════╝
       { O(1), O(log(n)), O(n log(n)), O(n), O(n+k), O(n^2) }
    > Average 
        • Index - None
        • Search - None
        • Insertion - O(1)
        • Deletion - O(1)
    > Worst 
        • Index - None
        • Search - None
        • Insertion - O(1)
        • Deletion - O(1)
    > Memory
        • Space - O(n)
╔════════╗
║  Code  ║
╚════════╝
"""
class LinkedQueue:
    """LIFO Stack implementation using singly linked list for storage"""
    
    #Nested Node Class
    class _Node():
    
        def __init__(self, data, next_node): 
            self.data = data
            self.next_node = next_node
    
    #Stack Methods    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size
        
    def is_empty(self):
        """Return true if the stack is empty"""
        return self._size == 0  
    
    def first(self):
        """return but not remove element at the front of the queue"""
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element 
    
    def dequeue(self):
        """Remove and return the first element of the queue(FIFO)
        Raise empty exception if the stack is empty"""
        
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head.data
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
        
    def enqueue(self, element):
        """Add an element to the back of the queue (FIFO)"""
        
        newest = self._Node(element, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size +=1

a = LinkedQueue()
a.enqueue(5)
a.enqueue(10)
a.enqueue(7)
a.enqueue(9)
a.dequeue()

