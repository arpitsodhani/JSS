# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def replacement(code, occupied):
    for i in range(4):
        for d in "0123456789":
            if d != code[i]:
                candidate = code[:i] + d + code[i + 1:]
                if candidate not in occupied:
                    return candidate
    return code

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    result = []

    for _ in range(t):
        n = int(data[pos])
        pos += 1
        arr = data[pos:pos + n]
        pos += n

        counts = Counter(arr)
        occupied = set(arr)
        changes = 0

        for i in range(n):
            if counts[arr[i]] > 1:
                counts[arr[i]] -= 1
                fresh = replacement(arr[i], occupied)
                arr[i] = fresh
                occupied.add(fresh)
                changes += 1

        result.append(str(changes))
        result += arr

    print("\n".join(result))

# CLAUSE: finish_program
main()
