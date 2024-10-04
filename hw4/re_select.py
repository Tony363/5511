def selection_sort(arr,n):
    end = len(arr)
    if n >= end - 1:
        return
    selection_sort_recursive(arr,n - end, end)
    
def selection_sort_recursive(arr, start, n):
    if start >= n - 1:
        return
    min_index = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i
    arr[start], arr[min_index] = arr[min_index], arr[start]
    selection_sort_recursive(arr, start + 1,n)

# Unit Test
def test_selection_sort():
    arr = [64, 25, 12, 22, 11]
    selection_sort_recursive(arr)
    assert arr == [11, 12, 22, 25, 64]
    print("Selection Sort Test Passed.")

if __name__ == "__main__":
    test_selection_sort()
    arr = list(map(int, input("Enter integers separated by space: ").split()))
    selection_sort_recursive(arr)
    print("Sorted array:", arr)
