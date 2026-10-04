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
        a = data[idx:idx + n]
        idx += n
        c = data[idx:idx + n]
        idx += n
        mp = {}
        for x, q in zip(a, c):
            mp[x] = mp.get(x, 0) + q
        items = sorted(mp.items())
        best = 0
        for i, (x, cx) in enumerate(items):
            take = min(cx, m // x)
            best = max(best, take * x)
            if i + 1 < len(items) and items[i + 1][0] == x + 1:
                y, cy = items[i + 1]
                take_x = min(cx, m // x)
                spent = take_x * x
                rem = m - spent
                take_y = min(cy, rem // y)
                spent += take_y * y
                rem -= take_y * y
                upgrade = min(take_x, cy - take_y, rem)
                spent += upgrade
                best = max(best, spent)
        ans.append(str(best))
    print('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
