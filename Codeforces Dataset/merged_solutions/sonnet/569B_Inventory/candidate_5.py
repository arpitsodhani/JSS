# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    items = sys.stdin.read().strip().split()
    if not items:
        return
    n = int(items[0])
    arr = list(map(int, items[1:1 + n]))
    present = [0] * (n + 1)
    for value in arr:
        if 1 <= value <= n:
            present[value] += 1
    missing = [value for value in range(1, n + 1) if present[value] == 0]
    cursor = 0
    already_kept = [0] * (n + 1)
    for index, value in enumerate(arr):
        if 1 <= value <= n and already_kept[value] == 0:
            already_kept[value] = 1
        else:
            arr[index] = missing[cursor]
            cursor += 1
    output = []
    for value in arr:
        output.append(str(value))
    sys.stdout.write(" ".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
