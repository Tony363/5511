
class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def tree_search(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node.count
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return 0

    def tree_insert(self, key):
        parent = None
        node = self.root
        while node is not None:
            parent = node
            if key == node.key:
                occurrences = node.count
                node.count += 1
                return occurrences
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        new_node = Node(key)
        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        return 0

    def tree_delete(self, key):
        self.root, occurrences = self._delete_rec(self.root, key)
        return occurrences

    def _delete_rec(self, node, key):
        if node is None:
            return node, 0
        if key < node.key:
            node.left, occurrences = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right, occurrences = self._delete_rec(node.right, key)
        else:
            occurrences = node.count
            if node.count > 1:
                node.count -= 1
            elif node.left is None:
                return node.right, occurrences
            elif node.right is None:
                return node.left, occurrences
            else:
                successor = self._min_value_node(node.right)
                node.key = successor.key
                node.count = successor.count
                node.right, _ = self._delete_rec(node.right, successor.key)
        return node, occurrences

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def tree_walk(self):
        self._inorder_walk(self.root)

    def _inorder_walk(self, node):
        if node:
            self._inorder_walk(node.left)
            if node.count > 1:
                print(f"{node.key}({node.count})")
            else:
                print(node.key)
            self._inorder_walk(node.right)

    def tree_print(self):
        self._print_tree(self.root, "", True)

    def _printTree(self, root, indent="", last='updown'):
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

# Interactive User Interface
def main():
    bst = BST()
    commands = {
        'search': bst.tree_search,
        'insert': bst.tree_insert,
        'delete': bst.tree_delete,
        'walk': bst.tree_walk,
        'print': bst.tree_print,
    }
    while True:
        cmd = input("Enter command (search, insert, delete, walk, print, exit): ").strip()
        if cmd == 'exit':
            break
        elif cmd in ('search', 'insert', 'delete'):
            word = input("Enter word: ").strip()
            if cmd == 'search':
                count = bst.tree_search(word)
                print(f"Occurrences of '{word}': {count}")
            elif cmd == 'insert':
                count = bst.tree_insert(word)
                print(f"Occurrences before insertion: {count}")
            elif cmd == 'delete':
                count = bst.tree_delete(word)
                print(f"Occurrences before deletion: {count}")
        elif cmd == 'walk':
            bst.tree_walk()
        elif cmd == 'print':
            bst.tree_print()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

