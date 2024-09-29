from min_heap_pq import MinHeapPriorityQueue

def assertion_test():
    pq = MinHeapPriorityQueue()
    words = ["apple", "banana", "cherry", "date", "fig", "grape"]

    # Test adding words
    for word in words:
        pq.add(word)
    assert pq.get_size() == 6

    # Test duplicate addition
    pq.add("apple")
    assert pq.get_size() == 6  # Size should not increase

    # Test search
    assert pq.search("banana") != -1
    assert pq.search("kiwi") == -1

    # Test extract_min
    min_word = pq.extract_min()
    assert min_word == "apple"
    assert pq.get_size() == 5

    # Continue extracting
    expected_order = ["banana", "cherry", "date", "fig", "grape"]
    for expected_word in expected_order:
        min_word = pq.extract_min()
        assert min_word == expected_word

    # Heap should be empty now
    assert pq.get_size() == 0
    assert pq.extract_min() is None

    print("All tests passed.")


def test_priority_queue():
    pq = MinHeapPriorityQueue()
    words = ["apple", "banana", "cherry", "date", "elderberry"]

    print("Adding words to the priority queue:")
    for word in words:
        pq.add(word)
        print(f"Added '{word}', heap: {pq.heap}")

    # Test size reporting
    print(f"\nSize of priority queue: {pq.get_size()}")  # Should be 5

    # Test searching for words
    print("\nSearching for words:")
    for word in ["banana", "fig"]:
        index = pq.search(word)
        if index != -1:
            print(f"'{word}' found at index {index}")
        else:
            print(f"'{word}' not found in the priority queue")

    # Remove the min word
    print("\nRemoving words from the priority queue:")
    min_word = pq.extract_min()
    print(f"Removed '{min_word}', heap after removal: {pq.heap}")

    # Test size after removal
    print(f"Size of priority queue after removal: {pq.get_size()}")  # Should be 4

    # Add a duplicate word
    print("\nAdding a duplicate word 'banana':")
    pq.add("banana")  # Should do nothing since "banana" is already in the queue
    print(f"Heap after attempting to add duplicate 'banana': {pq.heap}")

    # Add a new word
    print("\nAdding a new word 'fig':")
    pq.add("fig")
    print(f"Added 'fig', heap: {pq.heap}")

    # Remove all words
    print("\nRemoving all words:")
    while pq.get_size() > 0:
        word = pq.extract_min()
        print(f"Removed '{word}', heap: {pq.heap}")
        
    assertion_test()
        
if __name__ == "__main__":
    test_priority_queue()