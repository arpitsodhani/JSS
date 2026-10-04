# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def answer_case(arr):
    by_value = {}
    for x in arr:
        by_value[x] = by_value.get(x, 0) + 1

    start = {}
    total = 0
    for x in sorted(by_value):
        start[x] = total
        total += by_value[x]

    used = {}
    pos = [0] * len(arr)
    for i, x in enumerate(arr):
        k = used.get(x, 0)
        used[x] = k + 1
        pos[start[x] + k] = i

    best = 0
    cur = 0
    last = -1
    for p in pos:
        if p > last:
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
        last = p
    return len(arr) - best

def run(data):
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        out.append(str(answer_case(arr)))
    return "\n".join(out)

# CLAUSE: finish_program
if __name__ == "__main__":
    tokens = sys.stdin.buffer.read().split()
    sys.stdout.write(run(tokens))
