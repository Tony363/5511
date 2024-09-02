import random


def insertion_sort(
    a:list,
    n:int,
)->list:
    global ops_insert
    for i in range(1,n):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            ops_insert += 1
            j = j - 1
        a[j + 1] = k
    return a

def merge(
    a:list, 
    p:int, 
    q:int, 
    r:int,
)->None:
    global ops_merge
    nl = q - p + 1  # Number of elements in left subarray
    nr = r - q      # Number of elements in right subarray
    left = [0] * nl
    right = [0] * nr

    for i in range(nl):
        left[i] = a[p + i]
        ops_merge += 1
    for j in range(nr):
        right[j] = a[q + j + 1]
        ops_merge += 1

    i = j = 0
    k = p
    while i < nl and j < nr:
        ops_merge += 1
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



if __name__ == "__main__":
    ops_insert = ops_merge = 0
    n = 100
    arr = [random.randint(0, n) for i in range(n)]
    print(insertion_sort(arr, n))
    print("OPERATIONS FOR INSERTION - ",ops_insert)
    print(merge_sort(arr, 0, n - 1))
    print("OPERATIONS FOR MERGEs - ",ops_merge)
    
    # print(time_complexity_and_operations(insertion_sort, arr))
    # print(time_complexity_and_operations(merge_sort, arr))