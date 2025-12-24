#Deleting a node in Binary Tree
#Case 1: Deleting node with no child : Easiest
#Case 2: Delete node with one child : Remove and add the node below it in its place
#Case 3: Delete node with two children: Most difficult : Find minimum value from its right subtree and substitute in its place
#              OR Find maximum from left subtree and replace with deleted node.

class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else: # data > self.data
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit Node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        else: #val>self.data
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def delete(self, val):
        if val <  self.data:
            if self.left:
                self.left = self.left.delete(val)
            else:
                return None
        elif val > self.data:
            if self.right:
               self.right =  self.right.delete(val)
            else:
                return None
        else: # val = self.data
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])

        return root
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print(numbers_tree.in_order_traversal())










