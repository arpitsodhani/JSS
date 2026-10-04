# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def count_remaining(a, x):
    banned_until = -1
    removed = 0
    i = 0
    while i < len(a):
        bad_pair = i - 1 > banned_until and i >= 1 and a[i - 1] + a[i] < 2 * x
        bad_triple = i - 2 > banned_until and i >= 2 and a[i - 2] + a[i - 1] + a[i] < 3 * x
        if bad_pair or bad_triple:
            removed += 1
            banned_until = i
        i += 1
    return len(a) - removed

def main():
    data = sys.stdin.read().strip().split()
    index = 0
    t = int(data[index])
    index += 1
    result = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        numbers = []
        for _ in range(n):
            numbers.append(int(data[index]))
            index += 1
        x = int(data[index])
        index += 1
        result.append(str(count_remaining(numbers, x)))
    print("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
