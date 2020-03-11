unfinished 
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

from algorithm.doublylinkedbase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):

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
        if not isinstance(p, self.Positon):
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
        return self._make_position(self.traier._prev)

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

