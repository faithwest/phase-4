def solution(A):
    # Initialize an empty set to store paired elements
    paired = set()
    
    # Iterate through the array
    for num in A:
        # If the number is already in the set, remove it
        if num in paired:
            paired.remove(num)
        # If the number is not in the set, add it
        else:
            paired.add(num)
    
    # The remaining element in the set is the unpaired element
    unpaired_element = paired.pop()
    
    return unpaired_element

    
    return unpaired_element
A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))  # Output: 7
