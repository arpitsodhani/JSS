# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def operations_needed(n, start):
    total = 0
    equal = start
    while equal < n:
        copied = min(equal, n - equal)
        total += copied + 1
        equal += copied
    return total

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    i = 1
    ans = []
    for _ in range(q):
        n = data[i]
        i += 1
        counts = {}
        most = 0
        end = i + n
        while i < end:
            value = data[i]
            new_count = counts.get(value, 0) + 1
            counts[value] = new_count
            if new_count > most:
                most = new_count
            i += 1
        ans.append(str(operations_needed(n, most)))
    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
