def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1)

# Unit Test
def test_bubble_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_recursive(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]
    print("Bubble Sort Test Passed.")

if __name__ == "__main__":
    test_bubble_sort()
    arr = list(map(int, input("Enter integers separated by space: ").split()))
    bubble_sort_recursive(arr)
    print("Sorted array:", arr)
