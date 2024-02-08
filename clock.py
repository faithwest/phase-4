from itertools import permutations

def is_valid_time(hour, minute):
    return 0 <= hour < 24 and 0 <= minute < 60

def Solution(A, B, C, D):
    digits = [str(A), str(B), str(C), str(D)]
    posibble_times = set()

    # Generate all possible permutations of the digits
    for perm in permutations(digits):
        hour = int(perm[0] + perm[1])
        minute = int(perm[2] + perm[3])
        if is_valid_time(hour, minute):
            posibble_times.add((hour, minute))

    return len(posibble_times), posibble_times

# Example usage:
A, B, C, D = 2, 3, 3, 2
count, posibble_times = Solution(A, B, C, D)
print("Number of valid times:", count)
print("Valid times:")
for time in posibble_times:
    print("{:02d}:{:02d}".format(time[0], time[1]))
