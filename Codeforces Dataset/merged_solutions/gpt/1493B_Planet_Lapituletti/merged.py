# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
mp = {'0': '0', '1': '1', '2': '5', '5': '2', '8': '8'}

def valid(h, m, hh, mm):
    s = f"{hh:02d}{mm:02d}"
    if any(c not in mp for c in s):
        return False
    rh = int(mp[s[3]] + mp[s[2]])
    rm = int(mp[s[1]] + mp[s[0]])
    return rh < h and rm < m

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        h = int(data[idx])
        m = int(data[idx + 1])
        time_s = data[idx + 2]
        idx += 3

        hh = int(time_s[:2])
        mm = int(time_s[3:])

        while not valid(h, m, hh, mm):
            mm += 1
            if mm == m:
                mm = 0
                hh += 1
                if hh == h:
                    hh = 0

        out.append(f"{hh:02d}:{mm:02d}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
