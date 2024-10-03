import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from typing import Callable, List

def quicksort(
    A: List[int],
    p: int,
    r: int,
    partition_fn: Callable[[List[int], int, int, dict], int],
    counters: dict
) -> None:
    if p < r:
        q = partition_fn(A, p, r, counters)
        if partition_fn.__name__ == 'lomuto_partition':
            quicksort(A, p, q - 1, partition_fn, counters)
        else:
            quicksort(A, p, q, partition_fn, counters)
        quicksort(A, q + 1, r, partition_fn, counters)

def lomuto_partition(
    A: List[int],
    p: int,
    r: int,
    counters: dict
) -> int:
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        counters['core_operations'] += 1  # Comparison
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            counters['core_operations'] += 1  # Swap
    A[i + 1], A[r] = A[r], A[i + 1]
    counters['core_operations'] += 1  # Swap
    return i + 1

def hoare_partition(
    A: List[int],
    p: int,
    r: int,
    counters: dict
) -> int:
    pivot = A[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j -= 1
            counters['core_operations'] += 1  # Comparison
            if A[j] <= pivot:
                break
        while True:
            i += 1
            counters['core_operations'] += 1  # Comparison
            if A[i] >= pivot:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
            counters['core_operations'] += 1  # Swap
        else:
            return j

def main()->None:
    array_sizes = [10**i for i in range(1, 7)]  # Sizes from 10^1 to 10^6
    # num_trials = 5  # Number of trials per size
    results = {
        'lomuto': {'sizes': [], 'core_operations': []},
        'hoare': {'sizes': [], 'core_operations': []}
    }

    for size in array_sizes:
        lomuto_core_ops = 0
        hoare_core_ops = 0
    
        # Generate random array
        A = random.sample(range(size * 10), size)
        B = A.copy()
        
        # Lomuto Partition
        counters_lomuto = {'core_operations': 0}
        quicksort(A, 0, len(A) - 1, lomuto_partition, counters_lomuto)
        lomuto_core_ops += counters_lomuto['core_operations']
        
        # Hoare Partition
        counters_hoare = {'core_operations': 0}
        quicksort(B, 0, len(B) - 1, hoare_partition, counters_hoare)
        hoare_core_ops += counters_hoare['core_operations']
        
        
        # Store results
        results['lomuto']['sizes'].append(size)
        results['lomuto']['core_operations'].append(lomuto_core_ops)
        
        results['hoare']['sizes'].append(size)
        results['hoare']['core_operations'].append(hoare_core_ops)
   
    plot(results)
   
def plot(results:dict)->None:     
    import matplotlib.ticker as mticker

    # Define positions for each array size
    x_positions = range(len(results['lomuto']['sizes']))  # Positions 0 to 5
    x_labels = [f'$10^{{{i}}}$' for i in range(1, 7)]     # ['$10^1$', '$10^2$', ..., '$10^6$']

    # Plotting Core Operations with Categorical X-Axis
    plt.figure(figsize=(12, 7))
    plt.plot(x_positions, results['lomuto']['core_operations'], marker='o', label='Lomuto Partition')
    plt.plot(x_positions, results['hoare']['core_operations'], marker='s', label='Hoare Partition')

    plt.xlabel('Array Size')
    plt.ylabel('Number of Core Operations')
    plt.title('Core Operations vs. Array Size')
    plt.legend()
    plt.grid(True, which="both", ls="--")

    # Adjust y-axis formatter to prevent scientific notation
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.ticklabel_format(style='plain', axis='y')

    # Set x-axis ticks and labels
    plt.xticks(ticks=x_positions, labels=x_labels)

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()