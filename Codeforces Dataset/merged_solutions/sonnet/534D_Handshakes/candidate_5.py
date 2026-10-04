# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def possible_order(n, arr):
    groups = [[], [], []]
    for i, x in enumerate(arr):
        groups[x % 3].append((x, i + 1))

    groups = [sorted(group, reverse=True) for group in groups]
    answer = []
    current = 0

    for place in range(n):
        residue = place % 3
        if not groups[residue]:
            return None

        value, number = groups[residue][-1]
        if value > current:
            return None

        groups[residue].pop()
        answer.append(number)
        current = value + 1

    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    arr = data[1:]
    if len(arr) != n:
        return

    answer = possible_order(n, arr)
    if answer is None:
        print("Impossible")
    else:
        print("Possible")
        print(" ".join(map(str, answer)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
