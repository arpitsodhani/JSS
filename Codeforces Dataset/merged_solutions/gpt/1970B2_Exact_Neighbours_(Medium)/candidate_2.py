# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = [0] + data[1:1 + n]
    pos = [i for i in range(2, n + 1) if a[i] > 0]
    pos.sort(key=lambda i: -a[i])
    zeros = [i for i in range(2, n + 1) if a[i] == 0]
    order = [1] + pos + zeros
    coords = [None] * (n + 1)
    ans = [0] * (n + 1)
    y = 1
    coords[1] = (1, y)
    ans[1] = 1
    prev = 1
    col = 2
    for idx in pos:
        s = a[idx] - 1
        if y + s <= n:
            y += s
        else:
            y -= s
        coords[idx] = (col, y)
        ans[idx] = prev
        prev = idx
        col += 1
    for idx in zeros:
        coords[idx] = (col, y)
        ans[idx] = idx
        col += 1
    out = ['YES']
    for i in range(1, n + 1):
        out.append(f'{coords[i][0]} {coords[i][1]}')
    out.append(' '.join(map(str, ans[1:])))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
