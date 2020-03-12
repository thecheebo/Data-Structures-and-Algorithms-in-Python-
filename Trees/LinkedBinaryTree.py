class Tree:
    """Abstract base class representing a tree structure"""
    
    #nested Position class
    class Position:
        """An abstraction representing the location of a single element"""
        
        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')
            
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)     #opposite of __eq__
            
        # ---------- abstract methods that concrete subclass must support ----------  
       
        def root(self):
            """Return Position representing the tree s root (or None if empty)."""
            raise NotImplementedError('must be implemented by subclass')
            
        def parent(self, p):
            """Return Position representing p s parent (or None if p is root)."""
            raise NotImplementedError('must be implemented by subclass')
        
        def num_children(self, p):
            """Return the number of children that Position p has."""
            raise NotImplementedError('must be implemented by subclass')
            
        def children(self, p):
            """Generate an iteration of Positions representing p s children."""
            raise NotImplementedError('must be implemented by subclass')
            
        def len (self):
            """Return the total number of elements in the tree."""
            raise NotImplementedError('must be implemented by subclass')
            
        # ---------- concrete methods implemented in this class ----------
        
        def is_root(self, p):
            """Return True if Position P represents the root of the tree."""
            return self.root()==p
        
        def is_leaf(self, p):
            """Return true if Position p does not have any children."""
            return self.num_children(p)== 0
            
        def is_empty(self):
            """Return True if the tree is empty."""
            return len(self)== 0
        
        def depth(self, p):
            """Return the number of levels separating Position p from the root."""
            if self.is_root(p):
                return 0
            else:
                return 1 + self.depth(self.parent(p))
                
        def _height1(self):
            """Return the height of the tree"""
            return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
            
        def _height2(self, p):
            """"Return the heightof the subtree rooted at Position p"""
            if self.is_leaf(p):
                return 0
            else:
                return 1 +max(self.height2(c) for c in self.children(p))
                    
        def height(self, p=None):
            """Return the heigh of subtree rooted at Position P.  If P is none, return the height of the entire tree."""
            if p is None:
                p = self.root()
            return self.height2(p)

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    #--------------------------Additional Abstract methods-----------------------------------
    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child."""
        raise NotImplementedError('must be implemented by subclass')
        
    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have a left child."""
        raise NotImplementedError('must be implemented by subclass')
    
    #--------------------------Additional Abstract methods-----------------------------------
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                  #p must be the root, root has no sibling if none
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)   #possibly None
            else:
                return self.left(parent)    #possibly None
    
    
    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    """Simple Binary Tree ADT implemented with binary tree structure"""
    
    class _Node:
        # NOTE 'self' here is Node container
        __slots__ = ("_parent", "_left", "_right", "_elem")
        def __init__(self, element, parent=None, left=None, right=None):
            self._parent = parent
            self._left = left
            self._right = right
            self._element = element
        
        """def __str__(self):
            text = f"NODE<{id(self)}>::LF<{id(self._left)}>::"
            text += f"RT<{id(self._right)}>::PAR<{id(self._parent)}> : "
            text += f"ELEM<{self._elem}>"
            return text"""

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element"""
        # NOTE 'self' here is Position container
        def __init__(self, container: BinaryTree.Position, node):
            self._container = container
            self._node = node

        def element(self) -> BinaryTree.Position:
            # Return the element stored at this postion 
            return self._node._elem

        def __eq__(self, other: BinaryTree.Position):
            # Override Tree ABC
            # Equality here meant both types are the same type, 
            # and both node is the same node.
            return type(other) is type(self) and other._node is self._node



    def _validate(self, p):
        '''Convert Position object to Node object'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be of type Position')
        if p._container is not self:
            raise ValueError("p doesn't belong to this container")
        if p._node._parent is p._node: #invalidate for removed node
            raise ValueError("p has been removed and is no longer valid")
        return p._node

    def _make_position(self, node):
        '''Convert Node object to Position object'''
        return self.Position(self, node) if node else None

    #dunderinit
    
    def __init__(self):
        """Create an empty binary tree"""
        self._root = None
        self._size = 0

    #public accessors

    def len (self):
        """Return the total number of elements in the tree."""
        return self._size    
    
    def root(self):
        # Override Tree ABC
        return self._make_position(self._root)

    def parent(self, p):
        # Override Tree ABC
        node = self._validate(p)
        return self._make_position(node._parent)

    def left_child(self, p):
        # Override BinaryTree ABC
        node = self._validate(p)
        return self._make_position(node._left)

    def right_child(self, p):
        # Override BinaryTree ABC
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        # Override Tree ABC
        # num_children will be 0, 1, or 2 for BinaryTree
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
        
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty."""
        if self._root is not None:
            raise ValueError("Root already exists. Cannot add.")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child already exist. Cannot add.")
        self._size += 1
        node._left = self.Node(e, node)
        return self._make_position(node._left)

    def _add_right_child(self, p, e): 
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child already exist. Cannot add.")
        self._size += 1
        node._right = self.Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        '''Replacing elements of a node in tree without changing position.
           
           Return p's original element.
        '''
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        '''Remove node Position p (with at most 1 child) from the tree.
           Restriction of "at most one child" is due to the fact that binary 
           tree cannot have more than two children for each node.
           Return p's element.
        '''
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children. Cannot remove.")
        child = node._left if node._left else node._right # child could be None
        if child is not None:
            child._parent = node._parent # node._parent could be None
        if node is self._root: # root-node case
            self._root = child 
        else:  # leaf-node case
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        '''Attach BinaryTree t to node position p if child slot is available.
        '''
        node = self._validate(p) # additional verifications within
        if self.num_chilren(p) > 1:
            raise ValueError('Position p have no available slot.')
        if not type(self) is type(t):
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node # attach tree t to current position p
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node # attach tree t to current position p
            node._right = t2._root
            t2._root = None
            t2._size = 0 
