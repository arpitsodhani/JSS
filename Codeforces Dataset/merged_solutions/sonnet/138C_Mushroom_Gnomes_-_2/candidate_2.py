# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    n = data[p]
    m = data[p + 1]
    p += 2

    events = []
    for _ in range(n):
        a = data[p]
        h = data[p + 1]
        left = data[p + 2]
        right = data[p + 3]
        p += 4

        if left < 100:
            q = (100 - left) / 100.0
            events.append((a - h, q))
            events.append((a, 1.0 / q))

        if right < 100:
            q = (100 - right) / 100.0
            events.append((a + 1, q))
            events.append((a + h + 1, 1.0 / q))

    mushrooms = []
    for _ in range(m):
        b = data[p]
        z = data[p + 1]
        p += 2
        mushrooms.append((b, z))

    events.sort()
    mushrooms.sort()

    cur = 1.0
    ans = 0.0
    e = 0
    total_events = len(events)

    for x, z in mushrooms:
        while e < total_events and events[e][0] <= x:
            cur *= events[e][1]
            e += 1
        ans += z * cur

    sys.stdout.write("{:.10f}".format(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
