import unittest
from typing import Callable

def quicksort(
    A:list, 
    p:int, 
    r:int, 
    partition_fn:Callable[[list, int, int], int],
)->None:
    if p < r:
        q = partition_fn(A, p, r)
        quicksort(A, p, q - 1 if partition_fn == lomuto_partition else q, partition_fn)
        quicksort(A, q + 1, r, partition_fn)

def lomuto_partition(
    A:list, 
    p:int, 
    r:int
)->int:

    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def hoare_partition(
    A:list, 
    p:list, 
    r:list
)->int:
    pivot = A[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while A[j] > pivot:
            j -= 1
        i += 1
        while A[i] < pivot:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j



class TestQuicksort(unittest.TestCase):
    
    def test_quicksort_with_lomuto(self):
        A = [10, 80, 30, 90, 40, 50, 70]
        quicksort(A, 0, len(A) - 1, lomuto_partition)
        self.assertEqual(A, [10, 30, 40, 50, 70, 80, 90])
    
    def test_quicksort_with_hoare(self):
        A = [10, 80, 30, 90, 40, 50, 70]
        quicksort(A, 0, len(A) - 1, hoare_partition)
        self.assertEqual(A, [10, 30, 40, 50, 70, 80, 90])

    def test_quicksort_lomuto_with_user_input(self):
        A = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
        quicksort(A, 0, len(A) - 1, lomuto_partition)
        print("Sorted array using Lomuto partition:", A)
    
    def test_quicksort_hoare_with_user_input(self):
        A = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
        quicksort(A, 0, len(A) - 1, hoare_partition)
        print("Sorted array using Hoare partition:", A)

if __name__ == "__main__":
    unittest.main()
