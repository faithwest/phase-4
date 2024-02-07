# def solution(P, Q):
#     N = len(P)
#     distinct_letters = set()
#     must_have_letters = set()

#     for i in range(N):
#         if P[i] != Q[i]:
#             distinct_letters.add(P[i])
#             distinct_letters.add(Q[i])
#         else:
#             must_have_letters.add(P[i])

#     return max(len(must_have_letters), 1)  # Ensure at least one distinct letter

# p=["axxz"]
# q=[ "yzwy"]
# print(solution(p, q)) #


# def decimal_to_binary(decimal_num):
#     binary_digits = []

#     # Continue dividing the number by 2 until it becomes 0
#     while decimal_num > 0:
#         remainder = decimal_num % 2  # Get the remainder when dividing by 2
#         binary_digits.append(str(remainder))  # Append the remainder to the binary_digits list
#         decimal_num //= 2  # Integer division by 2

#     # Reverse the list to get the binary representation
#     binary_representation = ''.join(binary_digits[::-1])
#     return binary_representation

# # Test the function
# decimal_num = 8
# binary_representation = decimal_to_binary(decimal_num)
# print("Binary representation of", decimal_num, "is:", binary_representation)
