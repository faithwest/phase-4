# # from itertools import permutations

# # def is_valid_time(hour, minute):
# #     return 0 <= hour < 24 and 0 <= minute < 60


# # def Solution(A, B, C, D):
# #     digits = [A, B, C, D]
# #     valid_times = set()

# #     for perm in permutations(digits):
# #         hour = perm[0] * 10 + perm[1]
# #         minute = perm[2] * 10 + perm[3]
# #         if is_valid_time(hour, minute):
# #             valid_times.add((hour, minute))

# #     return len(valid_times)

# # # Example usage:
# from itertools import permutations

# def is_valid_time(hour, minute):
#     return 0 <= hour < 24 and 0 <= minute < 60

# def Solution(A, B, C, D):
#     digits = [A, B, C, D]
#     valid_times = set()

#     for perm in permutations(digits):
#         hour = perm[0] * 10 + perm[1]
#         minute = perm[2] * 10 + perm[3]
#         if is_valid_time(hour, minute):
#             valid_times.add((hour, minute))

#     return len(valid_times), valid_times

# # Example usage:
# A, B, C, D = 6, 2, 4, 7
# count, valid_times = Solution(A, B, C, D)
# print("Number of valid times:", count)
# print("Valid times:")
# for time in valid_times:
#     print("{:02d}:{:02d}".format(time[0], time[1]))

# # Output will vary based on input

# #given 4 didgits ,count how many times can be displayedon a digitalclock in a 24 hr format using those digits.the earliest time is 00:00 and the latest being 23:59.
# #write a function:def Solution(A,B,C,D) that given four integers A,B,C and D returns the number of valid times that can be displayed on a digital clock.


def generate_permutations(arr):
    if len(arr) == 1:
        return arr
    else:
        for i in range(len(arr)):
            element = arr[i]
            remaining_elements = arr[:i] + arr[i+1:]
            for permutation in generate_permutations(remaining_elements):
                return [element] + permutation

def is_valid_time(hour, minute):
    return 0 <= hour < 24 and 0 <= minute < 60

def solution(A, B, C, D):
    digits = [str(A), str(B), str(C), str(D)]
    possible_times = set()

    # Generate all possible permutations of the digits
    for perm in generate_permutations(digits):
        hour = int(perm[0] + perm[1])
        minute = int(perm[2] + perm[3])
        if is_valid_time(hour, minute):
            possible_times.add((hour, minute))

    return len(possible_times), possible_times
