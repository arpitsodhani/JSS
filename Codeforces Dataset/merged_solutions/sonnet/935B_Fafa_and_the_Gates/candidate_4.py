# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    parts = sys.stdin.read().split()
    if len(parts) == 1:
        path = "".join(filter(lambda c: c in "UR", parts[0]))
    else:
        path = parts[1]

    changes = {"R": 1, "U": -1}
    diff = 0
    states = []

    for step in path:
        diff += changes[step]
        if diff > 0:
            states.append(1)
        elif diff < 0:
            states.append(-1)

    coins = 0
    for i in range(1, len(states)):
        if states[i] != states[i - 1]:
            coins += 1

    print(coins)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
