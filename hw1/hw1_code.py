import random
import matplotlib.pyplot as plt

def insertion_sort(
    a:list,
    n:int,
)->list:
    global ops_insert, counter
    for i in range(1,n):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            counter += 1; 
            j = j - 1
        a[j + 1] = k
        ops_insert += (counter,)
    return a

def merge(
    a:list, 
    p:int, 
    q:int, 
    r:int,
)->None:
    global counter
    nl = q - p + 1  # Number of elements in left subarray
    nr = r - q      # Number of elements in right subarray
    left = [0] * nl
    right = [0] * nr

    for i in range(nl):
        left[i] = a[p + i]
        counter += 1
    for j in range(nr):
        right[j] = a[q + j + 1]
        counter += 1

    i = j = 0
    k = p
    while i < nl and j < nr:
        counter += 1
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
    global ops_merge,counter
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(a, p, q)
    ops_merge += (counter,)
    merge_sort(a, q + 1, r)
    ops_merge += (counter,)
    merge(a, p, q, r)
    return a

def plot_operations(
    ops_insert:tuple,
    ops_merge:tuple,
)->None:
    print(len(ops_insert),len(ops_merge))
    plt.plot(list(range(len(ops_insert))),ops_insert, label='Insertion Sort')
    plt.plot(list(range(len(ops_merge))),ops_merge, label='Merge Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Operations')
    plt.title('Insertion Sort vs Merge Sort')
    plt.legend()
    plt.show()   
    plt.savefig('complexity.jpg') 



if __name__ == "__main__":
    ops_insert,ops_merge = (),()
    n = 100
    counter = 0
    arr = [random.randint(0, n) for i in range(n)]
    print(insertion_sort(arr, n))
    print("OPERATIONS FOR INSERTION - ",counter)
    print("INSERTION SORT LOOPS", n - 1)
    
    counter = 0
    print(merge_sort(arr, 0, n - 1))
    print("OPERATIONS FOR MERGE - ",max(ops_merge))
    print("MERGE RECURSIVE CALLS - ",counter)
    plot_operations(ops_insert, ops_merge[::2])
    
