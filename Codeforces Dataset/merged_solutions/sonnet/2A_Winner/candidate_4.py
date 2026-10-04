# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    parts = sys.stdin.read().strip().split()
    n = int(parts[0])
    names = parts[1::2]
    scores = list(map(int, parts[2::2]))

    final_scores = {}
    for i in range(n):
        player = names[i]
        final_scores[player] = final_scores.setdefault(player, 0) + scores[i]

    winning_score = max(final_scores.values())
    tied = set()
    for player in final_scores:
        if final_scores[player] == winning_score:
            tied.add(player)

    prefix_scores = {}
    answer = ""
    for player, score in zip(names, scores):
        prefix_scores[player] = prefix_scores.get(player, 0) + score
        if player in tied and prefix_scores[player] >= winning_score:
            answer = player
            break

    print(answer)

# CLAUSE: finish_program
main()
