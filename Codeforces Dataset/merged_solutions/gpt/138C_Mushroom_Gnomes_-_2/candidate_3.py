# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import math

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    it = iter(data)
    n = next(it)
    m = next(it)

    events = {}

    def add_event(x, kind, p):
        if p == 0:
            return
        if x not in events:
            events[x] = [[], [], [], [], []]
        events[x][kind].append(p)

    for _ in range(n):
        a = next(it)
        h = next(it)
        l = next(it)
        r = next(it)

        if l:
            add_event(a - h, 0, l)
            add_event(a, 1, l)
        if r:
            add_event(a, 3, r)
            add_event(a + h, 2, r)

    for _ in range(m):
        b = next(it)
        z = next(it)
        if b not in events:
            events[b] = [[], [], [], [], []]
        events[b][4].append(z)

    cnt = [0] * 101
    logs = [0.0] * 101
    for p in range(1, 100):
        logs[p] = math.log((100 - p) / 100.0)

    sum_log = 0.0
    zero = 0
    ans = 0.0

    for x in sorted(events):
        e = events[x]

        for p in e[0]:
            if p == 100:
                zero += 1
            else:
                cnt[p] += 1
                sum_log += logs[p]

        for p in e[1]:
            if p == 100:
                zero -= 1
            else:
                cnt[p] -= 1
                sum_log -= logs[p]

        if e[4]:
            if zero:
                prob = 0.0
            elif sum_log < -745:
                prob = 0.0
            else:
                prob = math.exp(sum_log)
            ans += prob * sum(e[4])

        for p in e[3]:
            if p == 100:
                zero += 1
            else:
                cnt[p] += 1
                sum_log += logs[p]

        for p in e[2]:
            if p == 100:
                zero -= 1
            else:
                cnt[p] -= 1
                sum_log -= logs[p]

    print("{:.10f}".format(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
