def binary_search(arr, target):
    # Initialize left and right pointers
    left, right = 0, len(arr) - 1

    # Loop until the left pointer crosses the right pointer
    while left <= right:
        # Find the middle index
        mid = left + (right - left) // 2

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid  # Target found, return the index

        # If the target is greater than the middle element,
        # ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller than the middle element,
        # ignore the right half
        else:
            right = mid - 1

    # Target not found, return -1
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
