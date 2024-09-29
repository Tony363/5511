class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.position_map = {}  # word -> index in heap

    def size(self):
        """Report the number of words in the data structure."""
        return len(self.heap)

    def add(self, word):
        """Add a new word if it is not already in the queue."""
        if word in self.position_map:
            return  # Word already in the queue
        self.heap.append(word)
        index = len(self.heap) - 1
        self.position_map[word] = index
        self.__sift_up(index)

    def remove_min(self):
        """Remove the first word in dictionary order if the data structure is not empty."""
        if not self.heap:
            return None
        min_word = self.heap[0]
        last_word = self.heap.pop()
        del self.position_map[min_word]
        if self.heap:
            self.heap[0] = last_word
            self.position_map[last_word] = 0
            self.__sift_down(0)
        return min_word

    def search(self, word):
        """Search for a specific word and return its index or -1."""
        return self.position_map.get(word, -1)

    def __sift_up(self, index):
        """Maintain the heap property by moving the element at index up."""
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] >= self.heap[parent]:
                break
            self.__swap(index, parent)
            index = parent

    def __sift_down(self, index):
        """Maintain the heap property by moving the element at index down."""
        size = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self.__swap(index, smallest)
            index = smallest

    def __swap(self, i, j):
        """Swap elements at indices i and j in the heap and update the position map."""
        self.position_map[self.heap[i]], self.position_map[self.heap[j]] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
