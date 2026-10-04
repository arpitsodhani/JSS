# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_prefix(values, size):
    counts = [0] * (size + 1)
    for value in values:
        counts[value] += 1
    for i in range(1, size + 1):
        counts[i] += counts[i - 1]
    return counts

def query_count(prefix, size, x, bound):
    total = 0
    left = 0
    while left <= size:
        right = left + bound
        if right > size:
            right = size
        total += prefix[right] if left == 0 else prefix[right] - prefix[left - 1]
        left += x
    return total

def answer_one(prefix, size, need, x):
    low = 0
    high = x - 1
    while low <= high:
        mid = (low + high) // 2
        if query_count(prefix, size, x, mid) >= need:
            best = mid
            high = mid - 1
        else:
            low = mid + 1
    return best

def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    tests = numbers[at]
    at += 1
    lines = []

    for _ in range(tests):
        n = numbers[at]
        q = numbers[at + 1]
        at += 2
        values = numbers[at:at + n]
        at += n
        asked = numbers[at:at + q]
        at += q

        prefix = build_prefix(values, n)
        need = (n + 2) // 2
        solved = {}
        for x in asked:
            if x not in solved:
                solved[x] = answer_one(prefix, n, need, x)

        lines.append(" ".join(map(str, (solved[x] for x in asked))))

    print("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
