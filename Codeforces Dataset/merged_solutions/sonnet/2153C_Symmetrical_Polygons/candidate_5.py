# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def answer(sticks):
    freq = defaultdict(int)
    total = 0
    for stick in sticks:
        freq[stick] += 1
        total += stick

    keys = sorted(freq)
    odd = []
    for key in keys:
        if freq[key] % 2 == 1:
            odd.append(key)

    removed = sum(odd[:-2]) if len(odd) > 2 else 0
    odd = odd[-2:] if len(odd) > 2 else odd[:]

    while True:
        perimeter = total - removed
        if perimeter <= 0:
            return 0

        largest = 0
        for key in keys[::-1]:
            if freq[key] > 0:
                if key in odd or freq[key] - 1 >= 0:
                    largest = key
                    break

        if largest * 2 < perimeter and perimeter - removed >= 3:
            return perimeter

        if odd:
            removed += odd[0]
            odd = odd[1:]
            continue

        deleted = False
        for key in keys:
            if freq[key] >= 2:
                freq[key] -= 2
                removed += key * 2
                deleted = True
                break
        if not deleted:
            return 0

# CLAUSE: finish_program
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return
    tests = raw[0]
    at = 1
    lines = []
    for _ in range(tests):
        n = raw[at]
        at += 1
        lines.append(str(answer(raw[at:at + n])))
        at += n
    print("\n".join(lines))

if __name__ == "__main__":
    main()
