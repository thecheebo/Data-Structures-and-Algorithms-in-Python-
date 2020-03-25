class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
        def insert(self, data):
            if self.value == data:
                return False
            elif self.value > data:
                if self.leftChild:
                    return self.leftChild.insert(data)
                else:
                    self.leftChild = Node(data)
                    return True
            else:
                if self.rightChild:
                    return self.rightChildinsert(data)
                else:
                    self.rightChild = Node(data)
                    return True
               

class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
