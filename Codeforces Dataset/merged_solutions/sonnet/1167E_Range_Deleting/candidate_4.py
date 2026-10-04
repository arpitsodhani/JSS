# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return

    n, x = raw[0], raw[1]
    inf = n + 1
    first = [inf for _ in range(x + 5)]
    last = [0 for _ in range(x + 5)]

    pos = 1
    for value in raw[2:]:
        if first[value] > n:
            first[value] = pos
        last[value] = pos
        pos += 1

    left_clear = [False] * (x + 5)
    right_clear = [False] * (x + 6)
    left_max = [0] * (x + 5)
    right_min = [inf] * (x + 6)

    left_clear[0] = True
    highest = 0
    for value in range(1, x + 1):
        left_clear[value] = left_clear[value - 1] and highest <= first[value]
        highest = highest if highest >= last[value] else last[value]
        left_max[value] = highest

    right_clear[x + 1] = True
    lowest = inf
    for value in range(x, 0, -1):
        right_clear[value] = right_clear[value + 1] and last[value] <= lowest
        lowest = lowest if lowest <= first[value] else first[value]
        right_min[value] = lowest

    answer = 0
    right = 1

    for left in range(1, x + 1):
        keep_low = left - 1
        if not left_clear[keep_low]:
            break

        if right < left:
            right = left

        while right <= x:
            keep_high = right + 1
            if right_clear[keep_high] and left_max[keep_low] <= right_min[keep_high]:
                answer += x - right + 1
                break
            right += 1

    sys.stdout.write(f"{answer}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
