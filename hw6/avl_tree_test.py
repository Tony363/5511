class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New node is initially added at leaf

class AVLTree:
    def insert(self, root, key):
        # Perform the normal BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            # Duplicate keys are ignored
            return root

        # Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # Balance the tree
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, root, key):
        # Perform standard BST delete
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        # Update the height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Balance the node
        balance = self.getBalance(root)

        # Left Left Case
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Left Right Case
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Right Left Case
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        return y

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        # Rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left),
                           self.getHeight(x.right))

        return x

    def preOrder(self, root):
        if root:
            print("{0} ".format(root.key), end="")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print("{0} ".format(root.key), end="")
            self.inOrder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print("{0} ".format(root.key), end="")

# Testing the AVL Tree implementation
if __name__ == '__main__':
    avl_tree = AVLTree()
    root = None

    # Insert nodes into the AVL tree
    nodes_to_insert = [10, 20, 30, 40, 50, 25]
    print("Inserting nodes:", nodes_to_insert)
    for node in nodes_to_insert:
        root = avl_tree.insert(root, node)

    # Display the tree traversals
    print("\nPreorder traversal after insertions:")
    avl_tree.preOrder(root)
    print("\nInorder traversal after insertions:")
    avl_tree.inOrder(root)
    print("\nPostorder traversal after insertions:")
    avl_tree.postOrder(root)

    # Search for a node
    key_to_search = 25
    found_node = avl_tree.search(root, key_to_search)
    print("\n\nSearching for key {}:".format(key_to_search))
    if found_node:
        print("Key {} found in the AVL tree.".format(key_to_search))
    else:
        print("Key {} not found in the AVL tree.".format(key_to_search))

    # Delete a node
    key_to_delete = 30
    print("\nDeleting key {} from the AVL tree.".format(key_to_delete))
    root = avl_tree.delete(root, key_to_delete)

    # Display the tree after deletion
    print("\nPreorder traversal after deletion:")
    avl_tree.preOrder(root)
    print("\nInorder traversal after deletion:")
    avl_tree.inOrder(root)
    print("\nPostorder traversal after deletion:")
    avl_tree.postOrder(root)

