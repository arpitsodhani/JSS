# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import deque

    s = sys.stdin.read()
    i = 0
    nums = []
    while i < len(s) and len(nums) < 3:
        while i < len(s) and not s[i].isdigit():
            i += 1
        x = 0
        while i < len(s) and s[i].isdigit():
            x = x * 10 + ord(s[i]) - 48
            i += 1
        nums.append(x)

    n, m, k = nums
    cells = [c for c in s[i:] if c in ".*X"]

    grid = []
    start = None
    p = 0
    for r in range(n):
        row = cells[p:p + m]
        p += m
        for c, ch in enumerate(row):
            if ch == "X":
                start = (r, c)
        grid.append(row)

    if k % 2:
        print("IMPOSSIBLE")
        sys.exit()

    dist = [[-1] * m for _ in range(n)]
    sr, sc = start
    dist[sr][sc] = 0
    q = deque([(sr, sc)])

    dirs = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]

    while q:
        r, c = q.popleft()
        for dr, dc, _ in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "*" and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    ans = []
    r, c = sr, sc

    for step in range(k):
        rem = k - step - 1
        ok = False
        for dr, dc, ch in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "*" and dist[nr][nc] != -1 and dist[nr][nc] <= rem:
                ans.append(ch)
                r, c = nr, nc
                ok = True
                break
        if not ok:
            print("IMPOSSIBLE")
            sys.exit()

    print("".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
