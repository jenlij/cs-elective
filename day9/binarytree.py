# Binary search tree
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class MyBST:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = BSTNode(value)
        if self.root == None:
            self.root = new_node
        else:
            self.add_r(self.root, new_node)
            
    def add_r(self, node, new_node):
        if new_node.value < node.value:
            if node.left == None:
                new_node.parent = node
                node.left = new_node
            else:
                self.add_r(node.left, new_node)        
        else:
            if node.right == None:
                new_node.parent = node
                node.right = new_node
            else:
                self.add_r(node.right, new_node)     

    def print_preorder(self):
        if self.root is not None:
            self.print_preorder_r(self.root)

    def print_preorder_r(self, current_node):
        #root(current), left, right
        print current_node.value
        if current_node.left is not None:
            self.print_preorder_r(current_node.left)
        if current_node.right is not None:
            self.print_preorder_r(current_node.right)



tree = MyBST()
tree.add(50) 
tree.add(25)
tree.add(75)
tree.add(24)
tree.print_preorder()
#evaluate node, go left or righ
#assign parent of new node
#assign appropriate child of parent node