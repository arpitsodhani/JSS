# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    p = 1
    out = []
    dirs = {
        76: (0, -1),
        82: (0, 1),
        85: (-1, 0),
        68: (1, 0),
    }

    for _ in range(t):
        n = int(data[p])
        m = int(data[p + 1])
        p += 2
        grid = data[p:p + n]
        p += n

        total = n * m
        nxt = [-1] * total

        for i in range(n):
            row = grid[i]
            for j, ch in enumerate(row):
                di, dj = dirs[ch]
                ni = i + di
                nj = j + dj
                idx = i * m + j
                if 0 <= ni < n and 0 <= nj < m:
                    nxt[idx] = ni * m + nj

        state = [0] * total
        dp = [0] * total
        pos = [-1] * total

        for s in range(total):
            if state[s]:
                continue

            stack = []
            v = s
            while v != -1 and state[v] == 0:
                state[v] = 1
                pos[v] = len(stack)
                stack.append(v)
                v = nxt[v]

            if v == -1:
                val = 0
                for u in reversed(stack):
                    val += 1
                    dp[u] = val
            elif state[v] == 2:
                val = dp[v]
                for u in reversed(stack):
                    val += 1
                    dp[u] = val
            else:
                start = pos[v]
                cycle_len = len(stack) - start
                for i in range(start, len(stack)):
                    dp[stack[i]] = cycle_len
                for i in range(start - 1, -1, -1):
                    u = stack[i]
                    dp[u] = dp[nxt[u]] + 1

            for u in stack:
                state[u] = 2
                pos[u] = -1

        best = 0
        best_i = 0
        best_j = 0
        for idx, val in enumerate(dp):
            if val > best:
                best = val
                best_i = idx // m
                best_j = idx % m

        out.append(f"{best_i + 1} {best_j + 1} {best}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
