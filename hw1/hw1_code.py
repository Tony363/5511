import random
import time
import numpy as np

def insertion_sort(
    a:list,
    n:int,
)->list:
    omega = phi = 0
    for i in range(1,n):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            omega += 1
            j = j - 1
        a[j + 1] = k
        phi += 1 
    print(omega,phi)
    return a

def merge(
    a:list, 
    p:int, 
    q:int, 
    r:int
)->None:
    nl = q - p + 1  # Number of elements in left subarray
    nr = r - q      # Number of elements in right subarray
    left = [0] * nl
    right = [0] * nr

    for i in range(nl):
        left[i] = a[p + i]
    for j in range(nr):
        right[j] = a[q + j + 1]

    i = j = 0
    k = p
    while i < nl and j < nr:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left, if any
    while i < nl:
        a[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements of right, if any
    while j < nr:
        a[k] = right[j]
        j += 1
        k += 1

def merge_sort(a:list, p:int, r:int):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(a, p, q)
    merge_sort(a, q + 1, r)
    merge(a, p, q, r)
    return a

def time_complexity_and_operations(sort_func, arr):
    start_time = time.time()
    if sort_func == merge_sort:
        result = sort_func(arr.copy())
        end_time = time.time()
        return end_time - start_time, result
    else:
        comparisons, swaps = sort_func(arr.copy())
        end_time = time.time()
        return end_time - start_time, comparisons, swaps

if __name__ == "__main__":
    n = 10
    arr = [random.randint(0, n) for i in range(n)]
    print(insertion_sort(arr, n))
    print(merge_sort(arr, 0, n - 1))
    # print(time_complexity_and_operations(insertion_sort, arr))
    # print(time_complexity_and_operations(merge_sort, arr))