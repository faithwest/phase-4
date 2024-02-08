
def game(skills):
    n = len(skills)
    leftout = list(range(n))
    final_lap = [-1] * n
    lap_count = 1
    while len(leftout) > 1:
        incoming_players = []
        i = 0
        while i < len(leftout):
            first_player = leftout[i]
            second_player = leftout[i + 1] if i + 1 < len(leftout) else None
            if second_player is None or skills[first_player] > skills[second_player]:
                winners_id = first_player
            else:
                winners_id = second_player
            incoming_players.append(winners_id)
            final_lap[first_player] = lap_count
            if second_player is not None:
                final_lap[second_player] = lap_count
            i += 2
        leftout = incoming_players
        lap_count += 1
    return final_lap

def solution(skills):
    return game(skills)