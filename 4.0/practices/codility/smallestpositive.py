def smallest_No(A):
    # Filter out non-positive integers and duplicates
    posNo = set(filter(lambda m: m > 0, A))

    # Find the smallest positive integer not in the set
    smallest_No= 1
    while smallest_No in posNo:
        smallest_No += 1

    return smallest_No

# Example usage:
arr1 = [1, 3, 6, 4, 1, 2]
result1 = smallest_No(arr1)
print(result1)  # Output: 5

arr2 = [1, 2, 3]
result2 = smallest_No(arr2)
print(result2)  # Output: 4

arr3 = [-1, -3]
result3 = smallest_No(arr3)
print(result3)  # Output: 1
