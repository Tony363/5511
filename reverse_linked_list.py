
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
def reverse_linked_list(root:object):
    """_summary_

    Args:
        root (object): _description_

    Returns:
        _type_: _description_
    
    how does this algorithm work?
    
    1. If the root is None, return None.
    2. If the root.next is None, return the root.
    3. Recursively reverse the linked list starting from root.next.
    4. Set root.next.next to root.
    5. Set root.next to None.
    6. Return the new root.
    
    
    """
    if root is None:
        return None
    
    if root.next is None:
        return root
    
    new_root = reverse_linked_list(root.next)
    root.next.next = root
    root.next = None
    return new_root



# Test the function
def test_reverse_linked_list():
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)
    
    # Reverse the linked list
    new_root = reverse_linked_list(root)
    
    # Check the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
    assert new_root.data == 5
    assert new_root.next.data == 4
    assert new_root.next.next.data == 3
    assert new_root.next.next.next.data == 2
    assert new_root.next.next.next.next.data == 1
    assert new_root.next.next.next.next.next is None
    print("All tests passed.")

def find_first_occurrence(array, length, target):
    low = 0
    high = length - 1
    first_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            first_occurrence = mid
            high = mid - 1  # Continue searching to the left
    return first_occurrence

def find_last_occurrence(array, length, target):
    low = 0
    high = length - 1
    last_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            last_occurrence = mid
            low = mid + 1  # Continue searching to the right
    return last_occurrence

def count(array, length, target):
    first = find_first_occurrence(array, length, target)
    if first == -1:
        return 0  # Target not found
    last = find_last_occurrence(array, length, target)
    return last - first + 1

if __name__ == "__main__":
    test_reverse_linked_list()
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)
    new_root = reverse_linked_list(root)
    while new_root is not None:
        print(new_root)
        new_root = new_root.next