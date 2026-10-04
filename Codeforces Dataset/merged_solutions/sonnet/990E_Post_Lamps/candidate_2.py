# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n, m, k = values[0], values[1], values[2]
    p = 3

    blocked = [False] * n
    for _ in range(m):
        blocked[values[p]] = True
        p += 1

    price = [0] + values[p:p + k]

    nearest = [-1] * n
    last = -1
    for i in range(n):
        if not blocked[i]:
            last = i
        nearest[i] = last

    if blocked[0]:
        sys.stdout.write("-1")
        return

    best = None
    for length in range(1, k + 1):
        used = 0
        right = 0
        ok = True

        while right < n:
            place = nearest[right]
            if place < 0 or place + length <= right:
                ok = False
                break
            used += 1
            right = place + length

        if ok:
            total = used * price[length]
            if best is None or total < best:
                best = total

    sys.stdout.write(str(best if best is not None else -1))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
