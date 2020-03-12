def print_a_tree(self)
    if self._size == 0:
        print("There are no nodes in this tree")
    else:
        print(self.root()._node._element)
    if self.num_children(self.root()) > 0:
        print(self.left()._node._element)
