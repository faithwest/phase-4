def solution(S):
    n = len(S)
    prev_moved_player = -1  # track the last player who moved
    successful_moves = 0

for i in range(n):
    if S[i] == '>':
git         if i == n - 1:
            successful_moves += 1
            prev_moved_player = i
    elif S[i] == '<':
        # Check if the previous player has moved from his position
        if prev_moved_player == i - 1:
            successful_moves += 1
            prev_moved_player = i
    elif S[i] == '^':
        # Up move is always successful
        successful_moves += 1
        prev_moved_player = i
    else:
        # Down move is always successful
        successful_moves += 1
        prev_moved_player = i

return successful_moves