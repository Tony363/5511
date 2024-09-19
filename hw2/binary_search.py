import random
import math
import matplotlib.pyplot as plt

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return iterations  # Successful search
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return iterations  # Unsuccessful search

def estimate_average_iterations(array_size, num_trials):
    arr = list(range(array_size))  # Sorted array of integers from 0 to array_size - 1
    total_iterations = 0
    successful_iterations = 0
    unsuccessful_iterations = 0
    successful_searches = 0
    unsuccessful_searches = 0

    for _ in range(num_trials):
        # Decide whether the search will be successful or unsuccessful (50% chance each)
        if random.random() < 0.5:
            # Successful search
            target = random.choice(arr)
            iterations = binary_search(arr, target)
            successful_iterations += iterations
            successful_searches += 1
        else:
            # Unsuccessful search
            # Choose a target not in arr
            target = random.randint(-array_size, 2 * array_size)
            while target in arr:
                target = random.randint(-array_size, 2 * array_size)
            iterations = binary_search(arr, target)
            unsuccessful_iterations += iterations
            unsuccessful_searches += 1
        total_iterations += iterations

    average_iterations = total_iterations / num_trials
    average_successful = successful_iterations / successful_searches if successful_searches > 0 else 0
    average_unsuccessful = unsuccessful_iterations / unsuccessful_searches if unsuccessful_searches > 0 else 0

    return average_iterations, average_successful, average_unsuccessful

def main():
    array_sizes = [10, 100, 1000, 10000, 100000]
    num_trials = 10000
    results = []

    for size in array_sizes:
        avg_iter, avg_succ, avg_unsucc = estimate_average_iterations(size, num_trials)
        theoretical = math.log2(size) + 0.5
        results.append({
            'Array Size': size,
            'Average Iterations': avg_iter,
            'Average Successful': avg_succ,
            'Average Unsuccessful': avg_unsucc,
            'Theoretical': theoretical
        })
        print(f"Array Size: {size}")
        print(f"  Average Total Iterations: {avg_iter:.4f}")
        print(f"  Average Successful Iterations: {avg_succ:.4f}")
        print(f"  Average Unsuccessful Iterations: {avg_unsucc:.4f}")
        print(f"  Theoretical Average Iterations: {theoretical:.4f}\n")

    # Plotting the results
    array_sizes = [res['Array Size'] for res in results]
    avg_iterations = [res['Average Iterations'] for res in results]
    avg_successful = [res['Average Successful'] for res in results]
    avg_unsuccessful = [res['Average Unsuccessful'] for res in results]
    theoretical_values = [res['Theoretical'] for res in results]

    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, avg_iterations, marker='o', label='Empirical Average Iterations')
    plt.plot(array_sizes, theoretical_values, marker='x', linestyle='--', label='Theoretical Average Iterations')
    plt.xscale('log')
    plt.plot(array_sizes, avg_successful, marker='v', label='Average Successful Iterations')
    plt.plot(array_sizes, avg_unsuccessful, marker='^', label='Average Unsuccessful Iterations')
    plt.xlabel('Array Size (log scale)')
    plt.ylabel('Average Number of Iterations')
    plt.title('Binary Search Average Iterations vs. Array Size')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

