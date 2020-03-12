╔═══════════════╗
║  Description  ║
╚═══════════════╝
    > Doubly Linked List (BASE CLASS)
        • Has a header and a trailer, which never change, only nodes inbetween
        • all new nodes are placed inbetween existing nodes
        • all deleted nodes have neigbhors
╔══════════════╗
║  Attributes  ║
╚══════════════╝

  >LinkedDeque(Doubly Linked)
    > Doubly Linked Base Class
        • Header
        • Trailer
        • Header._next is trailer
        • Trailer._prev is header
        • Size
       > Node
          • Data
          • Previous Linked Node
          • Next Linked Node
╔══════════════╗
║  Operations  ║
╚══════════════╝
  > Linked Deque (Doubly Linked List)
    • Return first element
    • Return last element
    • Insert at front of deque
    • Insert at back of deque
    • Delete first
    • Delete last
    > Doubly Linked List
        • Return Length
        • Check if empty
        • _Insert between (prev, next
        • _Delete Node
        
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

c__author__ = 'tnb'


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""
                           
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
                           
class _DoublyLinkedBase:
    """A base clss providing a doubly linked list representation."""
    
    class _Node:
        #__slots__ = '_element','_prev','_next'      #streamline memory
    
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
        
    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, sucessor):
        """Add element e between 2 nodes and return new node"""
        newest = self._Node(e, predecessor, sucessor)   #linked to neighbors
        predecessor._next = newest
        sucessor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsentinel node from teh list and return its element"""
        predecessor = node._prev
        sucessor = node._next
        predecessor._next = sucessor
        sucessor._prev = predecessor
        self._size -= 1
        element = node._element                     #record deleted node
        node._prev = node._next = node._element = None #deprecate node
        return element                              #return deleted node


                           trial code:
                           a= PositionalList()
root = a.add_first(10)
p20 = a.add_after(root, 20)
p30 = a.add_after(p20, 30)
a.add_last(40)
a.add_last(50)
                           
                           
