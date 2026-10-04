# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    n = int(raw[0])
    m = int(raw[1])
    k = int(raw[2])

    banned = bytearray(n)
    cursor = 3
    for cursor in range(3, 3 + m):
        banned[int(raw[cursor])] = 1

    cost_start = 3 + m

    previous = [-1] * n
    available = -1
    i = 0
    while i < n:
        if banned[i] == 0:
            available = i
        previous[i] = available
        i += 1

    if banned[0]:
        sys.stdout.write("-1\n")
        return

    result = 10 ** 30
    found = False

    power = 1
    while power <= k:
        covered = 0
        count = 0

        while covered < n:
            spot = previous[covered]
            reach = spot + power
            if spot < 0 or reach <= covered:
                count = -1
                break
            count += 1
            covered = reach

        if count >= 0:
            total = count * int(raw[cost_start + power - 1])
            if total < result:
                result = total
            found = True

        power += 1

    sys.stdout.write(str(result if found else -1) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
