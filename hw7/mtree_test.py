class BTreeNode:
    def __init__(self, m, leaf=False):
        self.m = m  # Order of B-tree
        self.keys = []  # List of keys
        self.children = []  # List of child pointers
        self.leaf = leaf  # Is true when node is leaf
    
    def display(self, level=0):
        result = ""
        if not self.children:
            result += "        " + "\t"*level + "--\n"
            for key in self.keys[::-1]:
                result += "Level " + str(level) + " " + "\t"*level + str(key) + "\n"
            result += "        " + "\t"*level + "--\n"
            return result
        
        right_tree = self.children[len(self.children)//2:]
        left_tree = self.children[:len(self.children)//2]

        idx = -1
        for child in right_tree[::-1]:
            if child.keys and self.keys and  child.keys[-1] < self.keys[-1]:
                result += "Level " + str(level) + " " + "\t"*level + str(self.keys[idx]) + "\n"
                idx -= 1
            result += child.display(level + 1)
            result += "        " + "\t"*(level) + "--\n" if idx == -1 else ""

        for child in left_tree[::-1]:
            if child.keys and self.keys and child.keys[-1] < self.keys[-1]:
                result += "Level " + str(level) + " " + "\t"*level + str(self.keys[idx]) + "\n"
                result += "        " + "\t"*level + "--\n" if abs(idx) == len(self.keys) else ""
                idx -= 1
            result += child.display(level + 1)
        return result
    
    


class BTree:
    def __init__(self, m):
        self.m = m  # Order of B-tree
        self.root = BTreeNode(m, leaf=True)

    def search(self, k, x=None):
        """Search key k in subtree rooted with x"""
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return (x, i)
        elif x.leaf:
            return None
        else:
            return self.search(k, x.children[i])
        
    def insert(self, k):
        """Insert key k into B-tree"""
        root = self.root
        if len(root.keys) == self.m - 1:
            s = BTreeNode(self.m)
            s.children.insert(0, root)
            s.leaf = False
            self.root = s
            self.split_child(s, 0)
            self._insert_non_full(s, k)
        else:
            self._insert_non_full(root, k)
            
    def delete(self, k):
        """Delete key k from B-tree"""
        self._delete(self.root, k)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def split_child(self, x, i):
        """Split the child x.children[i] of node x"""
        t = (self.m + 1) // 2
        y = x.children[i]
        z = BTreeNode(self.m, leaf=y.leaf)
        mid_key = y.keys[t - 1]
        # z gets the last t - 1 keys
        z.keys = y.keys[t:]
        # y retains the first t - 1 keys
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        x.children.insert(i + 1, z)
        x.keys.insert(i, mid_key)
        # No need to update num_keys, as we're using len(x.keys)


    def _insert_non_full(self, x, k):
        """Insert key k into non-full node x"""
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
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

    def _delete(self, x, k):
        t = (self.m + 1) // 2
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and x.keys[i] == k:
            if x.leaf:
                x.keys.pop(i)
            else:
                if len(x.children[i].keys) >= t:
                    pred = self._get_pred(x, i)
                    x.keys[i] = pred
                    self._delete(x.children[i], pred)
                elif len(x.children[i + 1].keys) >= t:
                    succ = self._get_succ(x, i)
                    x.keys[i] = succ
                    self._delete(x.children[i + 1], succ)
                else:
                    self._merge(x, i)
                    self._delete(x.children[i], k)
        else:
            if x.leaf:
                return
            flag = i == len(x.keys)
            if len(x.children[i].keys) < t:
                self._fill(x, i)
            if flag and i > len(x.keys):
                self._delete(x.children[i - 1], k)
            else:
                self._delete(x.children[i], k)

    def _get_pred(self, x, idx):
        current = x.children[idx]
        while not current.leaf:
            current = current.children[-1]
        return current.keys[-1]

    def _get_succ(self, x, idx):
        current = x.children[idx + 1]
        while not current.leaf:
            current = current.children[0]
        return current.keys[0]

    def _fill(self, x, idx):
        t = (self.m + 1) // 2
        if idx != 0 and len(x.children[idx - 1].keys) >= t:
            self._borrow_from_prev(x, idx)
        elif idx != len(x.keys) and len(x.children[idx + 1].keys) >= t:
            self._borrow_from_next(x, idx)
        else:
            if idx != len(x.keys):
                self._merge(x, idx)
            else:
                self._merge(x, idx - 1)

    def _borrow_from_prev(self, x, idx):
        child = x.children[idx]
        sibling = x.children[idx - 1]
        child.keys.insert(0, x.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        x.keys[idx - 1] = sibling.keys.pop()
        # No need to update num_keys, as we're using len(x.keys)

    def _borrow_from_next(self, x, idx):
        child = x.children[idx]
        sibling = x.children[idx + 1]
        child.keys.append(x.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        x.keys[idx] = sibling.keys.pop(0)
        # No need to update num_keys, as we're using len(x.keys)

    def _merge(self, x, idx):
        child = x.children[idx]
        sibling = x.children[idx + 1]
        t = (self.m + 1) // 2
        child.keys.append(x.keys.pop(idx))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        x.children.pop(idx + 1)
        # No need to update num_keys, as we're using len(x.keys)

    def display(self):
        print(self.root.display())


# Testing the B-tree implementation

def test_btree(m):
    print(f"\nTesting B-tree with order m = {m}")
    btree = BTree(m)

    # Insert integers from 1 to 20
    for i in range(1, 21):
        btree.insert(i)

    print("\nB-tree structure after insertions:")
    btree.display()

    # Delete even integers from 2 to 20
    for i in range(2, 21, 2):
        btree.delete(i)

    print("\nB-tree structure after deletions:")
    btree.display()


if __name__ == "__main__":
    test_btree(4)
    test_btree(5)
