# Example: Binary search for 3 in a sorted list of 8 items
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 3
result = binary_search(arr, target)
print(f"Element {target} is at index: {result}")