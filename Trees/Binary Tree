class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    def left(self, p):
    
    def right(self, p):
    
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
        """Generate an iteration of Positions representing p s children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
