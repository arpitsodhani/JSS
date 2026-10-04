import sys
from collections import Counter

def best_perimeter(sticks):
    count = Counter(sticks)
    total = sum(sticks)
    odd = sorted([x for x, c in count.items() if c % 2 == 1])

    removed = 0
    while len(odd) > 2:
        removed += odd.pop(0)

    values = sorted(count.keys(), reverse=True)

    while total - removed > 0:
        perimeter = total - removed

        largest = 0
        for x in values:
            used = count[x]
            if x in odd:
                used -= 1
            if used > 0 or x in odd:
                largest = x
                break

        if largest * 2 < perimeter and perimeter - removed >= 3:
            return perimeter

        if odd:
            removed += odd.pop(0)
        else:
            for x in sorted(values):
                if count[x] >= 2:
                    count[x] -= 2
                    removed += 2 * x
                    break
            else:
                break

    return 0

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        sticks = data[idx:idx + n]
        idx += n
        out.append(str(best_perimeter(sticks)))

    print('\n'.join(out))

if __name__ == "__main__":
    main()
