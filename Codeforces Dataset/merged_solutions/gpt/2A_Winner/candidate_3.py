# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import defaultdict

    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit()

    n = int(data[0])
    rounds = []
    total = defaultdict(int)

    idx = 1
    for _ in range(n):
        name = data[idx]
        score = int(data[idx + 1])
        idx += 2
        rounds.append((name, score))
        total[name] += score

    max_score = max(total.values())
    candidates = {name for name, score in total.items() if score == max_score}

    current = defaultdict(int)
    for name, score in rounds:
        current[name] += score
        if name in candidates and current[name] >= max_score:
            print(name)
            break

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
