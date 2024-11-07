class BTreeNode:
    def __init__(self, m, is_leaf):
        self.m = m
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        
    def __str__(self, level=0):
        result = ""
        right_tree = self.children[len(self.children)//2:]
        left_tree = self.children[:len(self.children)//2]
        for child in right_tree:
            result += child.__str__(level + 1)

        result += "Level " + str(level) + " \t"*level + str(self.keys) + "\n"

        for child in left_tree:
            result += child.__str__(level + 1)
        return result

class BTree:
    def __init__(self, m):
        self.m = m
        self.root = BTreeNode(m, True)

    def search(self, k, x=None):
        if x is None:
            x = self.root
        i = 0
        n = len(x.keys)
        while i < n and k > x.keys[i]:
            i += 1
        if i < n and k == x.keys[i]:
            return (x, i)
        elif x.is_leaf:
            return None
        else:
            return self.search(k, x.children[i])

    def split_child(self, x, i):
        m = self.m
        y = x.children[i]
        z = BTreeNode(m, y.is_leaf)
        t = m // 2

        z.keys = y.keys[t:]
        y.keys = y.keys[:t]

        if not y.is_leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys.pop(-1))

    def insert(self, k):
        root = self.root
        if len(root.keys) == self.m - 1:
            s = BTreeNode(self.m, False)
            s.children.append(self.root)
            self.split_child(s, 0)
            self._insert_non_full(s, k)
            self.root = s
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.is_leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == self.m - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], k)

    def delete(self, k):
        self._delete(self.root, k)
        if len(self.root.keys) == 0 and not self.root.is_leaf:
            self.root = self.root.children[0]

    def _delete(self, x, k):
        i = 0
        n = len(x.keys)
        while i < n and k > x.keys[i]:
            i += 1

        if x.is_leaf:
            if i < n and x.keys[i] == k:
                x.keys.pop(i)
                return True
            return False
        else:
            if i < n and x.keys[i] == k:
                return self._delete_internal_node(x, k, i)
            elif len(x.children[i].keys) >= self.m // 2:
                return self._delete(x.children[i], k)
            else:
                if i != 0 and len(x.children[i - 1].keys) >= self.m // 2:
                    self._borrow_from_prev(x, i)
                elif i + 1 < len(x.children) and len(x.children[i + 1].keys) >= self.m // 2:
                    self._borrow_from_next(x, i)
                else:
                    if i + 1 < len(x.children):
                        self._merge_nodes(x, i)
                    else:
                        self._merge_nodes(x, i - 1)
                return self._delete(x.children[i if i < len(x.children) else i - 1], k)

    def _delete_internal_node(self, x, k, i):
        if len(x.children[i].keys) >= self.m // 2:
            pred = self._get_predecessor(x.children[i])
            x.keys[i] = pred
            return self._delete(x.children[i], pred)
        elif len(x.children[i + 1].keys) >= self.m // 2:
            succ = self._get_successor(x.children[i + 1])
            x.keys[i] = succ
            return self._delete(x.children[i + 1], succ)
        else:
            self._merge_nodes(x, i)
            return self._delete(x.children[i], k)

    def _merge_nodes(self, x, i):
        c1 = x.children[i]
        c2 = x.children[i + 1]
        c1.keys.append(x.keys[i])
        c1.keys.extend(c2.keys)
        if not c1.is_leaf:
            c1.children.extend(c2.children)
        x.keys.pop(i)
        x.children.pop(i + 1)

    def _borrow_from_prev(self, x, i):
        child = x.children[i]
        sibling = x.children[i - 1]
        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop(-1)
        if not sibling.is_leaf:
            child.children.insert(0, sibling.children.pop(-1))

    def _borrow_from_next(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]
        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)
        if not sibling.is_leaf:
            child.children.append(sibling.children.pop(0))

    def _get_predecessor(self, x):
        while not x.is_leaf:
            x = x.children[-1]
        return x.keys[-1]

    def _get_successor(self, x):
        while not x.is_leaf:
            x = x.children[0]
        return x.keys[0]

    def display(self):
        print(self.root)

def test_btree(m):
    print(f"Testing B-Tree of order {m}")
    btree = BTree(m)

    # Insert i = 1 to 20
    for i in range(1, 21):
        btree.insert(i)

    print("B-Tree after insertions:")
    btree.display()

    # Delete even numbers from 2 to 20
    for i in range(2, 21, 2):
        btree.delete(i)

    print("B-Tree after deletions:")
    btree.display()
    print("\n" + "#" * 50 + "\n")

if __name__ == "__main__":
    # Run tests for m = 4 and m = 5
    test_btree(4)
    test_btree(5)

