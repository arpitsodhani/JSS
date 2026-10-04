# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n, b = values[0], values[1]
    q = deque()
    result = []
    pos = 2
    for _ in range(n):
        t = values[pos]
        d = values[pos + 1]
        pos += 2
        while q and q[0] <= t:
            q.popleft()
        if len(q) > b:
            result.append("-1")
        else:
            start = t if not q else q[-1]
            finish = start + d
            q.append(finish)
            result.append(str(finish))
    sys.stdout.write(" ".join(result))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


