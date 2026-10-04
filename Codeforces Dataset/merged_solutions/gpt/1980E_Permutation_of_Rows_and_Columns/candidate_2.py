# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        total = n * m
        pos_r = [0] * (total + 1)
        pos_c = [0] * (total + 1)
        for i in range(n):
            for j in range(m):
                x = data[idx]
                idx += 1
                pos_r[x] = i
                pos_c[x] = j
        row_map = [-1] * n
        col_map = [-1] * m
        used_rows = [-1] * n
        used_cols = [-1] * m
        ok = True
        for i in range(n):
            for j in range(m):
                x = data[idx]
                idx += 1
                if not ok:
                    continue
                ar = pos_r[x]
                ac = pos_c[x]
                if row_map[ar] == -1:
                    if used_rows[i] != -1:
                        ok = False
                    else:
                        row_map[ar] = i
                        used_rows[i] = ar
                elif row_map[ar] != i:
                    ok = False
                if col_map[ac] == -1:
                    if used_cols[j] != -1:
                        ok = False
                    else:
                        col_map[ac] = j
                        used_cols[j] = ac
                elif col_map[ac] != j:
                    ok = False
        ans.append('YES' if ok else 'NO')
    sys.stdout.write('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
