
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)


    def find_max_value(self):
        if self.root is None:
            return None
        
        current = self.root

        while current.right is not None:
            current = current.right

        return current.key
    

# if __name__ == "__main__":
#     bst = BST()
#     bst.insert(50)
#     bst.insert(30)
#     bst.insert(70)
#     bst.insert(20)
#     bst.insert(40)
#     bst.insert(60)
#     bst.insert(80)
#     bst.insert(75)
#     bst.insert(90) 

#     max_val = bst.find_max_value()
#     print(f"Найбільше значення у дереві: {max_val}") 

    