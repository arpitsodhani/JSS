# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import deque

    def main():
        input = sys.stdin.readline
        n, m = map(int, input().split())
        g = [input().strip() for _ in range(n)]

        empty_rows = 0
        for i in range(n):
            seen = False
            segments = 0
            j = 0
            while j < m:
                if g[i][j] == '#':
                    seen = True
                    segments += 1
                    while j < m and g[i][j] == '#':
                        j += 1
                else:
                    j += 1
            if segments > 1:
                print(-1)
                return
            if not seen:
                empty_rows += 1

        empty_cols = 0
        for j in range(m):
            seen = False
            segments = 0
            i = 0
            while i < n:
                if g[i][j] == '#':
                    seen = True
                    segments += 1
                    while i < n and g[i][j] == '#':
                        i += 1
                else:
                    i += 1
            if segments > 1:
                print(-1)
                return
            if not seen:
                empty_cols += 1

        if (empty_rows == 0) != (empty_cols == 0):
            print(-1)
            return

        vis = [[False] * m for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m):
                if g[i][j] == '#' and not vis[i][j]:
                    ans += 1
                    q = deque([(i, j)])
                    vis[i][j] = True
                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == '#' and not vis[nx][ny]:
                                vis[nx][ny] = True
                                q.append((nx, ny))

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
