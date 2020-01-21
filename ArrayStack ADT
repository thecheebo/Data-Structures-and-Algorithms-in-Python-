╔═══════════════╗
║  Description  ║
╚═══════════════╝
    > ArrayStack
        • Last In - First Out
╔══════════════╗
║  Attributes  ║
╚══════════════╝
    > ArrayStack
        • Data

╔══════════════╗
║  Operations  ║
╚══════════════╝
    > Node
        • Get length
        • Check if empty
        • Add to top 
        • Return top
        • Pop top
        • Return reverse

╔══════════════╗
║  Complexity  ║
╚══════════════╝
       { O(1), O(log(n)), O(n log(n)), O(n), O(n+k), O(n^2) }
    > Average 
        • Index 
        • Search
        • Insertion
        • Deletion
    > Worst 
        • Index
        • Search
        • Insertion
        • Deletion
    > Memory
        • Space
╔════════╗
║  Code  ║
╚════════╝

class ArrayStack:
    """LIFO Stack implementation using a python list as underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = []                  #nonpublic list instance
        
    def __len__(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty mofo')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty mofo')
        return self._data.pop()
