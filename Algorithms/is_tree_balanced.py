def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))
    
    #First value of the return value indicatres if tree is balanced, and if balanced the 2nd value of the return value is the height of tree
    
    def check_balanced(tree)
