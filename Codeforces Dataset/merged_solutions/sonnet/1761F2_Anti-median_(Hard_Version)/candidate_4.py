# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def valid_after_set(p, changed):
    n = len(p)
    left = changed
    right = changed
    for center in range(n):
        if p[center] == -1:
            continue
        limit = min(center, n - 1 - center)
        for radius in range(1, limit + 1):
            if not (center - radius <= changed <= center + radius):
                continue
            low = center - radius
            high = center + radius
            cnt = 0
            unknown = False
            for i in range(low, high + 1):
                if p[i] == -1:
                    unknown = True
                    break
                if p[i] < p[center]:
                    cnt += 1
            if not unknown and cnt == radius:
                return False
    return True

def initial_ok(p):
    n = len(p)
    for center in range(n):
        if p[center] == -1:
            continue
        for radius in range(1, min(center + 1, n - center)):
            segment = p[center - radius:center + radius + 1]
            if -1 in segment:
                continue
            smaller = sum(1 for x in segment if x < p[center])
            if smaller == radius:
                return False
    return True

def answer_one(n, p):
    seen = set()
    for x in p:
        if x != -1:
            seen.add(x)
    missing = set(range(1, n + 1)) - seen
    spots = [i for i, x in enumerate(p) if x == -1]
    if len(missing) != len(spots):
        return 0
    if not initial_ok(p):
        return 0
    result = 0

    def go(idx):
        nonlocal result
        if idx == len(spots):
            result = (result + 1) % MOD
            return
        pos = spots[idx]
        for val in tuple(missing):
            p[pos] = val
            missing.remove(val)
            if valid_after_set(p, pos):
                go(idx + 1)
            missing.add(val)
            p[pos] = -1

    go(0)
    return result

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0]) if data else 0
    ptr = 1
    res = []
    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        p = list(map(int, data[ptr:ptr + n]))
        ptr += n
        res.append(str(answer_one(n, p)))
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
