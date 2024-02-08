def generate_number_variations(arr):
    variations = []

for num in arr:
    num_str = str(num)
    num_length = len(num_str)
    visited = [False] * num_length

    def generate_permutations(current_index, current_num):
        nonlocal variations
        if current_index == num_length:
            variations.append(current_num)
            return

        for i in range(num_length):
            if not visited[i]:
                visited[i] = True
                generate_permutations(current_index + 1, current_num * 10 + int(num_str[i]))
                visited[i] = False

    generate_permutations(0, 0)

return variations
Example usage:
arr = [123, 456]
print(generate_number_variations(arr))