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
    r:int,
)->list:
    nl = q - p + 1
    nr = r - q 
    l = [0] * (nl - 1)
    r = [0] * (nr - 1)
    for i in range(0, nl - 1):
        l[i] = a[p + i]
    i = j = 0
    k = p
    while i < nl and j < nr:
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        elif a[k] == r[j]:
            j += 1
        k += 1
    
    while i < nl:
        a[k] = l[i]
        i += 1
        k += 1
    while j < nr:
        a[k] = r[j]
        j += 1
        k += 1
    return a

def merge_sort(
    a:list,
    p:int,
    r:int,
)->list:
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