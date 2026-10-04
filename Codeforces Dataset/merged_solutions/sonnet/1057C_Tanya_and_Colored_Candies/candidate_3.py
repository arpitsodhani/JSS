# CLAUSE: setup_environment
import sys

def main():
    parts = sys.stdin.read().split()
    if not parts:
        return
    n, start, need = map(int, parts[:3])
    start -= 1
    amounts = list(map(int, parts[3:3 + n]))
    colors = parts[3 + n]
    inf = 10 ** 18
    color_id = {"R": 0, "G": 1, "B": 2}

# CLAUSE: solve_logic
    by_amount = {}
    for i, value in enumerate(amounts):
        by_amount.setdefault(value, []).append(i)

    minus_pos = [[inf] * (need + 1) for _ in range(3)]
    plus_pos = [[inf] * (need + 1) for _ in range(3)]
    answer = inf

    for value in sorted(by_amount):
        current = []
        capped = min(need, value)

        for i in by_amount[value]:
            row = [inf] * (need + 1)
            row[capped] = abs(i - start)
            own = color_id[colors[i]]

            for c in range(3):
                if c == own:
                    continue
                left = minus_pos[c]
                right = plus_pos[c]
                for eaten in range(need + 1):
                    base = left[eaten] + i
                    alt = right[eaten] - i
                    if alt < base:
                        base = alt
                    if base >= inf:
                        continue
                    total = eaten + value
                    if total > need:
                        total = need
                    if base < row[total]:
                        row[total] = base

            if row[need] < answer:
                answer = row[need]
            current.append((i, own, row))

        for i, own, row in current:
            left = minus_pos[own]
            right = plus_pos[own]
            for eaten, cost in enumerate(row):
                if cost == inf:
                    continue
                a = cost - i
                b = cost + i
                if a < left[eaten]:
                    left[eaten] = a
                if b < right[eaten]:
                    right[eaten] = b

# CLAUSE: finish_program
    print(-1 if answer == inf else answer)

if __name__ == "__main__":
    main()
