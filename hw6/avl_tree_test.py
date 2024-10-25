class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New node is initially added at leaf

class AVLTree:
    def __init__(self):
        self.root = None

    # Utility function to get the height of the node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Utility function to get balance factor of node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotate subtree rooted with y
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))

        # Return new root
        return x

    # Left rotate subtree rooted with x
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return new root
        return y

    # Insert a key into the AVL tree
    def insert(self, key):
        inserted_before = self.search_count(self.root, key)
        if inserted_before > 0:
            # Duplicate found, ignore insertion
            return inserted_before
        self.root = self._insert(self.root, key)
        return 0  # Indicate that insertion was successful

    def _insert(self, node, key):
        # 1. Perform normal BST insertion
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            # Duplicate keys are not allowed
            return node

        # 2. Update height of this ancestor node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # 3. Get the balance factor
        balance = self.get_balance(node)

        # 4. If node is unbalanced, then try the four cases

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Return the unchanged node pointer
        return node

    # Function to delete a node
    def delete(self, key):
        deleted_before = self.search_count(self.root, key)
        if deleted_before == 0:
            # Key not found
            return deleted_before
        self.root = self._delete(self.root, key)
        return deleted_before

    def _delete(self, node, key):
        # Step 1: Perform standard BST delete
        if not node:
            return node

        elif key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with two children: Get the inorder successor
            temp = self.get_min_value_node(node.right)

            node.key = temp.key

            node.right = self._delete(node.right, temp.key)

        # If the tree had only one node then return
        if node is None:
            return node

        # Step 2: Update the height of the current node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # Step 3: Get the balance factor
        balance = self.get_balance(node)

        # Step 4: If node is unbalanced, then try the four cases

        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Function to search for a key and return count (0 or 1)
    def search_count(self, node, key):
        if not node:
            return 0
        if key == node.key:
            return 1
        elif key < node.key:
            return self.search_count(node.left, key)
        else:
            return self.search_count(node.right, key)

    # Function to perform in-order traversal
    def tree_walk(self):
        self._tree_walk(self.root)

    def _tree_walk(self, node):
        if node is not None:
            self._tree_walk(node.left)
            print(node.key)
            self._tree_walk(node.right)

    # Function to print the tree structure
    def tree_print(self):
        self._tree_print(self.root, "", True)

    def _tree_print(self, node, indent, last):
        if node is not None:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "
            print(node.key)
            self._tree_print(node.left, indent, False)
            self._tree_print(node.right, indent, True)

    # Function to get the node with the smallest key
    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Function to search for a key and return existence (1) or not (0)
    def tree_search(self, key):
        return self.search_count(self.root, key)

# Sample Run Demonstration
def main():
    avl = AVLTree()
    while True:
        command = input("Enter command (search, insert, delete, walk, print, exit): ").strip().lower()
        if command == "search":
            word = input("Enter word to search: ").strip()
            count = avl.tree_search(word)
            print(f"Occurrences of '{word}': {count}")
        elif command == "insert":
            word = input("Enter word to insert: ").strip()
            count_before = avl.tree_search(word)
            result = avl.insert(word)
            if result == 0:
                print(f"'{word}' inserted successfully.")
            else:
                print(f"'{word}' already exists in the tree.")
        elif command == "delete":
            word = input("Enter word to delete: ").strip()
            count_before = avl.tree_search(word)
            result = avl.delete(word)
            if result > 0:
                print(f"'{word}' deleted successfully.")
            else:
                print(f"'{word}' does not exist in the tree.")
        elif command == "walk":
            print("Tree Walk (In-order Traversal):")
            avl.tree_walk()
        elif command == "print":
            print("Tree Structure:")
            avl.tree_print()
        elif command == "exit":
            print("Exiting.")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
