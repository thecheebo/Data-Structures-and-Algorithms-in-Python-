"""
╔═══════════════╗
║  Description  ║
╚═══════════════╝
    > Linked List
        • First In - Last Out
╔══════════════╗
║  Attributes  ║
╚══════════════╝
    > Node
        • Data
        • Next Linked Node
    > Linked List
        • Root Location
        • Size
╔══════════════╗
║  Operations  ║
╚══════════════╝
    > Node
        • Get Data
        • Set Data
        • Get Node
        • Set Node
    > LinkedList
        • Add Node
        • Remove Node
        • Search Node
        • Print All Node
        • Size Of List
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
"""

class Node():
    def __init__(self, data, next_node = None): 
        self.data = data
        self.next_node = next_node
    def get_next(self):
        return self.next_node
    def set_next(self, next_node):
        self.next_node = next_node
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data

class LinkedList():
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    def add_node(self, data):
        if self.root = None:
            new_node = Node(data)
            self.root = new_node
            self.size +=1
        while self.next_node != None:
            
        else:
            new_node = Node(data)
            
    def remove_node(self, data):
        if self.data == data:
            
    def search_node(self, data):
    
    def print_nodes(self):
    
    def size(self):
