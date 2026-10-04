# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []

    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n
        b = data[p:p + n]
        p += n

        mp = {}
        for i in range(n):
            mp[(a[i], b[i])] = i

        used = [False] * n
        left = []
        right = []
        center = -1
        ok = True
        self_count = 0

        for i in range(n):
            if used[i]:
                continue
            x, y = a[i], b[i]
            if x == y:
                self_count += 1
                center = i
                used[i] = True
            else:
                j = mp.get((y, x), -1)
                if j == -1 or j == i:
                    ok = False
                    break
                used[i] = used[j] = True
                left.append(i)
                right.append(j)

        if not ok or self_count != (n % 2):
            out.append("-1")
            continue

        target = left[:]
        if n % 2:
            target.append(center)
        target.extend(reversed(right))

        cur = list(range(n))
        pos = list(range(n))
        ops = []

        for i in range(n):
            if cur[i] != target[i]:
                j = pos[target[i]]
                ops.append((i + 1, j + 1))
                cur[i], cur[j] = cur[j], cur[i]
                pos[cur[i]] = i
                pos[cur[j]] = j

        out.append(str(len(ops)))
        for i, j in ops:
            out.append(f"{i} {j}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
