# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import deque

    def solve():
        input = sys.stdin.readline
        t = int(input())
        out = []
        for _ in range(t):
            n, m = map(int, input().split())
            g = [input().strip() for _ in range(n)]

            comp = [[-1] * m for _ in range(n)]
            sizes = []
            r1 = []
            r2 = []
            c1 = []
            c2 = []

            for i in range(n):
                for j in range(m):
                    if g[i][j] == '#' and comp[i][j] == -1:
                        cid = len(sizes)
                        q = deque([(i, j)])
                        comp[i][j] = cid
                        sz = 0
                        mn_r = mx_r = i
                        mn_c = mx_c = j
                        while q:
                            x, y = q.popleft()
                            sz += 1
                            if x < mn_r: mn_r = x
                            if x > mx_r: mx_r = x
                            if y < mn_c: mn_c = y
                            if y > mx_c: mx_c = y
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == '#' and comp[nx][ny] == -1:
                                    comp[nx][ny] = cid
                                    q.append((nx, ny))
                        sizes.append(sz)
                        r1.append(max(0, mn_r - 1))
                        r2.append(min(n - 1, mx_r + 1))
                        c1.append(max(0, mn_c - 1))
                        c2.append(min(m - 1, mx_c + 1))

            row_dots = [row.count('.') for row in g]
            col_dots = [0] * m
            for i in range(n):
                for j, ch in enumerate(g[i]):
                    if ch == '.':
                        col_dots[j] += 1

            k = len(sizes)
            add = [[] for _ in range(n)]
            rem = [[] for _ in range(n)]
            for cid in range(k):
                add[r1[cid]].append(cid)
                if r2[cid] + 1 < n:
                    rem[r2[cid] + 1].append(cid)

            col_events = [[] for _ in range(m + 1)]
            best = 0
            active = [False] * k
            cur_row_sum = 0

            for r in range(n):
                for cid in add[r]:
                    active[cid] = True
                    cur_row_sum += sizes[cid]
                    col_events[c1[cid]].append(sizes[cid])
                    col_events[c2[cid] + 1].append(-sizes[cid])

                cur_col_sum = 0
                for c in range(m):
                    for v in col_events[c]:
                        cur_col_sum += v
                    val = cur_row_sum + cur_col_sum + row_dots[r] + col_dots[c]
                    if g[r][c] == '.':
                        val -= 1
                    if val > best:
                        best = val

                for cid in rem[r + 1] if r + 1 < n else ():
                    active[cid] = False
                    cur_row_sum -= sizes[cid]
                    col_events[c1[cid]].append(-sizes[cid])
                    col_events[c2[cid] + 1].append(sizes[cid])

            out.append(str(best))

        print("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
