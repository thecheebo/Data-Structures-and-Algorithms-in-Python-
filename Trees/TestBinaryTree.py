Class Tree:
    class Position:
        
        def element(self):
        
        def __eq__(self, other):
        
        def __ne__(self, other):
    
    def root(self):
    
    def parent(self):
    
    def num_children(self): 
    
    def children(self):
    
    def __len__(self):
    
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p)==0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self == 0
                   
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 +self.depth(self.parent(p))
    
    def height(self, p = None):
        '''Return the max height of current subtree rooted at Position p. '''
        def _height(p):
            '''Traverse to farthest leaf from current position p recursively'''
            if self.is_leaf(p):
                return 0
            else:
                return 1 + max(_height(p) for p in self.children(p))
        if p is None:
            # Allows us to get height of entire tree rather than just subtree
            p = self.root()
        return _height(p)
                   
class BinaryTree(Tree):
    def sibling(self, p):
        """Return a position representing p's sibling(or None if there isn't a sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p ==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def children(self, p):
                   
                   
                  
