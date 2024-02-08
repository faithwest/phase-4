# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].
# def solution(N):
#     binary=bin[2:]
    
#     for i in strings:
#         if i in strings
#         return binary_gap 2

####################################################
# def solution(x):
#     x_new = bin(x)[2:]
#     print(x_new)
#     sp = x_new.split("1")
#     max_length = max(len(substring) for substring in sp)
################################################################
def solution(N):

# Step 1: Convert N to binary representation
    binary = bin(N)[2:]
    print(f"Binary representation of {N}: {binary}")

    # Step 2: Find the positions of all the 1s in the binary representation
    ones = [i for i, x in enumerate(binary) if x == '1']
    print(ones)

    # Step 3: Calculate the length of the longest binary gap
    max_length = 0
    for i in range(1, len(ones)):
        max_length = max(max_length, ones[i] - ones[i-1] - 1)
        print(f"{max_length}")

    return max_length

print(solution(529))