# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def best_perimeter(sticks):
    count = Counter(sticks)
    total = sum(sticks)
    odd = sorted(x for x, c in count.items() if c & 1)
    removed = 0
    values = sorted(count, reverse=True)

    while total > removed:
        perimeter = total - removed
        largest = 0
        odd_set = set(odd)
        for x in values:
            usable = count[x] - (1 if x in odd_set else 0)
            if usable > 0 or x in odd_set:
                largest = x
                break

        if largest * 2 < perimeter and perimeter - removed >= 3:
            return perimeter

        if odd:
            removed += odd.pop(0)
        else:
            for x in reversed(values):
                if count[x] >= 2:
                    count[x] -= 2
                    removed += x + x
                    break
            else:
                break

    return 0

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    pos = 1
    ans = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        ans.append(str(best_perimeter(data[pos:pos + n])))
        pos += n
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
