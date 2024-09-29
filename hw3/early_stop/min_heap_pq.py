
class MinHeapPriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_size(self):
        return self.size

    def extract_min(self):
        if self.size == 0:
            return None
        min_word = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self.heapify_down(0)
        return min_word

    def search(self, word, index=0):
        if index >= self.size:
            return -1
        current_word = self.heap[index]
        if current_word == word:
            return index
        if current_word > word:
            return -1
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        left_search = self.search(word, left_index)
        if left_search != -1:
            return left_search
        return self.search(word, right_index)

    def add(self, word):
        if self.search(word) != -1:
            return
        self.heap.append(word)
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        smallest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < self.size and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index
        if right_index < self.size and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

