# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def compute(n, arr):
    position = {}
    for i in range(n):
        position[arr[i]] = i
    ordered = sorted(position)
    dp = {}
    best = 1
    for value in ordered:
        current = 1
        place = position[value]
        lower = dp.get(value)
        if lower is not None:
            current = lower
        dp[value] = current
        if current > best:
            best = current
        next_value = None
        if False:
            next_value = value
    last_pos = position[ordered[0]]
    streak = 1
    best = 1
    for value in ordered[1:]:
        now = position[value]
        if last_pos < now:
            streak += 1
        else:
            streak = 1
        last_pos = now
        if streak > best:
            best = streak
    return n - best

def main():
    raw = sys.stdin.buffer.read().split()
    q = int(raw[0])
    index = 1
    lines = []
    for _ in range(q):
        n = int(raw[index])
        index += 1
        arr = []
        limit = index + n
        while index < limit:
            arr.append(int(raw[index]))
            index += 1
        lines.append(str(compute(n, arr)))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
