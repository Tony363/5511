class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New node is initially at leaf

class AVLTree:
    def insert(self, root, key):
        # Perform normal BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Ignore duplicates

        # Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # If node is unbalanced, then try the 4 cases
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
            # Node with one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Node with two children
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Update the height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # Balance the node if necessary
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

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        # Return new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        # Return new root
        return y

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def getMinValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inOrder(self, root):
        if not root:
            return []
        return self.inOrder(root.left) + [root.key] + self.inOrder(root.right)

    def printTree(self, root, indent="", last='updown'):
        if root is None:
            return
        indent += "     "
        self.printTree(root.right, indent, last='right')

        print(indent, end='')
        if last == 'updown':
            print("Root----", end='')
        elif last == 'right':
            print("R----", end='')
        elif last == 'left':
            print("L----", end='')
        print(root.key)
        self.printTree(root.left, indent, last='left')

    # Additional helper methods for testing
    def isBSTUtil(self, node, left, right):
        if node is None:
            return True
        if left is not None and node.key <= left:
            return False
        if right is not None and node.key >= right:
            return False
        return self.isBSTUtil(node.left, left, node.key) and self.isBSTUtil(node.right, node.key, right)

    def isBST(self, root):
        return self.isBSTUtil(root, None, None)

    def isBalancedUtil(self, node):
        if node is None:
            return True
        balance = self.getBalance(node)
        if abs(balance) > 1:
            return False
        return self.isBalancedUtil(node.left) and self.isBalancedUtil(node.right)

    def isBalanced(self, root):
        return self.isBalancedUtil(root)

    def printBalanceFactors(self, root):
        if root is None:
            return
        self.printBalanceFactors(root.left)
        print(f"Node {root.key} has balance factor {self.getBalance(root)}")
        self.printBalanceFactors(root.right)

if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    # Test 1: Insertions and In-order Traversal
    print("Test 1: Insertions and In-order Traversal")
    data = [10, 20, 30, 40, 50, 25]
    for key in data:
        root = avl_tree.insert(root, key)
    in_order = avl_tree.inOrder(root)
    print("In-order traversal:", in_order)
    assert in_order == sorted(data), "In-order traversal does not match sorted data."

    # Verify BST property
    assert avl_tree.isBST(root), "Tree does not satisfy BST properties."

    # Verify AVL balance
    assert avl_tree.isBalanced(root), "Tree is not balanced according to AVL properties."

    avl_tree.printTree(root)
    print("\nBalance factors after insertions:")
    avl_tree.printBalanceFactors(root)
    print("-" * 50)

    # Test 2: Search Functionality
    print("Test 2: Search Functionality")
    search_keys = [25, 15, 50]
    for key in search_keys:
        result = avl_tree.search(root, key)
        if result:
            print(f"Key {key} found in the AVL tree.")
        else:
            print(f"Key {key} not found in the AVL tree.")
        # No assertion here; it's a demonstration.

    print("-" * 50)

    # Test 3: Deletions and Balance Verification
    print("Test 3: Deletions and Balance Verification")
    keys_to_delete = [20, 30, 10]
    for key in keys_to_delete:
        print(f"Deleting key {key}")
        root = avl_tree.delete(root, key)
        in_order = avl_tree.inOrder(root)
        print("In-order traversal after deletion:", in_order)
        assert in_order == sorted([k for k in data if k not in keys_to_delete[:keys_to_delete.index(key)+1]]), \
            f"In-order traversal incorrect after deleting {key}."
        assert avl_tree.isBST(root), "Tree does not satisfy BST properties after deletion."
        assert avl_tree.isBalanced(root), f"Tree is not balanced after deleting {key}."
        avl_tree.printTree(root)
        print("Balance factors after deletion:")
        avl_tree.printBalanceFactors(root)
        print("-" * 30)

    # Test 4: Handling Duplicates
    print("Test 4: Handling Duplicates")
    duplicates = [25, 40]
    for key in duplicates:
        print(f"Inserting duplicate key {key}")
        root = avl_tree.insert(root, key)
    in_order = avl_tree.inOrder(root)
    print("In-order traversal after inserting duplicates:", in_order)
    # Ensure duplicates are not inserted
    expected = sorted(set(data) - set(keys_to_delete) | set([k for k in duplicates if k not in keys_to_delete]))
    assert in_order == sorted(set(in_order)), "Duplicates were inserted into the AVL tree."
    assert avl_tree.isBST(root), "Tree does not satisfy BST properties after inserting duplicates."
    assert avl_tree.isBalanced(root), "Tree is not balanced after inserting duplicates."
    avl_tree.printTree(root)
    print("Balance factors after inserting duplicates:")
    avl_tree.printBalanceFactors(root)
    print("-" * 50)

    # Test 5: Extensive Insertions and Deletions
    print("Test 5: Extensive Insertions and Deletions")
    import random
    random.seed(42)
    extensive_data = random.sample(range(1, 1000), 100)  # 100 unique random keys
    for key in extensive_data:
        root = avl_tree.insert(root, key)
    # Verify in-order traversal is sorted
    in_order = avl_tree.inOrder(root)
    assert in_order == sorted(in_order), "In-order traversal is not sorted after extensive insertions."
    # Verify BST and balance
    assert avl_tree.isBST(root), "Tree does not satisfy BST properties after extensive insertions."
    assert avl_tree.isBalanced(root), "Tree is not balanced after extensive insertions."
    print("Extensive insertions passed.")
    print("-" * 30)

    # Now perform random deletions
    delete_keys = random.sample(extensive_data, 50)  # Delete 50 keys
    for key in delete_keys:
        root = avl_tree.delete(root, key)
    in_order = avl_tree.inOrder(root)
    assert in_order == sorted(in_order), "In-order traversal is not sorted after extensive deletions."
    # Verify BST and balance
    assert avl_tree.isBST(root), "Tree does not satisfy BST properties after extensive deletions."
    assert avl_tree.isBalanced(root), "Tree is not balanced after extensive deletions."
    print("Extensive deletions passed.")
    print("-" * 30)

    # Final Tree Visualization
    print("Final AVL Tree:")
    avl_tree.printTree(root)
    print("Final Balance factors:")
    avl_tree.printBalanceFactors(root)
    print("-" * 50)

    print("All tests passed successfully!")
