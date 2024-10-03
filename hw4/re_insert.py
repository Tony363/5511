def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

# Unit Test
def test_insertion_sort():
    arr = [12, 11, 13, 5, 6]
    insertion_sort_recursive(arr)
    assert arr == [5, 6, 11, 12, 13]
    print("Insertion Sort Test Passed.")

if __name__ == "__main__":
    test_insertion_sort()
    arr = list(map(int, input("Enter integers separated by space: ").split()))
    insertion_sort_recursive(arr)
    print("Sorted array:", arr)
