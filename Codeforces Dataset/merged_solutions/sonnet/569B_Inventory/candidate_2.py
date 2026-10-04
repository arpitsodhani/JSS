# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    arr = data[1:1 + n]
    used = set()
    replace = []
    for idx, value in enumerate(arr):
        if 1 <= value <= n and value not in used:
            used.add(value)
        else:
            replace.append(idx)
    missing = [value for value in range(1, n + 1) if value not in used]
    for idx, value in zip(replace, missing):
        arr[idx] = value
    sys.stdout.write(" ".join(map(str, arr)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
