# CLAUSE: setup_environment
import sys

def primes_up_to(m):
    ok = [True] * (m + 1)
    if m >= 0:
        ok[0] = False
    if m >= 1:
        ok[1] = False
    i = 2
    while i <= m // i:
        if ok[i]:
            j = i * i
            while j <= m:
                ok[j] = False
                j += i
        i += 1
    return ok

# CLAUSE: solve_logic
def contribution(values, prime):
    total = 0
    items = []
    for index, value in enumerate(values):
        if value != 1:
            items.append((index, value))
    size = len(values)

    previous = -1
    for i, item in enumerate(items):
        position, value = item
        next_position = items[i + 1][0] if i + 1 < len(items) else size
        if prime[value]:
            total += (position - previous) * (next_position - position) - 1
        previous = position
    return total

def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    where = 1
    tests = []
    high = 0

    for _ in range(t):
        n = int(raw[where])
        e = int(raw[where + 1])
        where += 2
        arr = [int(x) for x in raw[where:where + n]]
        where += n
        tests.append((n, e, arr))
        local = max(arr)
        if local > high:
            high = local

    prime = primes_up_to(high)
    lines = []
    for n, e, arr in tests:
        answer = 0
        grouped = [[] for _ in range(e)]
        for idx, value in enumerate(arr):
            grouped[idx % e].append(value)
        for group in grouped:
            answer += contribution(group, prime)
        lines.append(str(answer))

    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
main()
