from priority_queue import PriorityQueue

def test_priority_queue():
    pq = PriorityQueue()
    words = ["apple", "banana", "cherry", "date", "elderberry"]

    print("Adding words to the priority queue:")
    for word in words:
        pq.add(word)
        print(f"Added '{word}', heap: {pq.heap}")

    # Test size reporting
    print(f"\nSize of priority queue: {pq.size()}")  # Should be 5

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
    min_word = pq.remove_min()
    print(f"Removed '{min_word}', heap after removal: {pq.heap}")

    # Test size after removal
    print(f"Size of priority queue after removal: {pq.size()}")  # Should be 4

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
    while pq.size() > 0:
        word = pq.remove_min()
        print(f"Removed '{word}', heap: {pq.heap}")

if __name__ == "__main__":
    test_priority_queue()
