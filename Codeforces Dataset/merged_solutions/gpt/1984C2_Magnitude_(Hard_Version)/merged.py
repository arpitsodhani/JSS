# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 998244353

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        pref = 0
        mn = 0
        mx = 0
        counts = {0: 1}

        for x in a:
            states = [(mn, counts[mn])]
            if mx != mn:
                states.append((mx, counts[mx]))

            nxt = {}
            for v, cnt in states:
                y = v + x
                nxt[y] = (nxt.get(y, 0) + cnt) % MOD
                ay = abs(y)
                nxt[ay] = (nxt.get(ay, 0) + cnt) % MOD

            pref += x
            mn = pref
            mx = max(nxt)

            if mn == mx:
                counts = {mn: nxt[mn] % MOD}
            else:
                counts = {
                    mn: nxt[mn] % MOD,
                    mx: nxt[mx] % MOD,
                }

        out.append(str(counts[mx] % MOD))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
