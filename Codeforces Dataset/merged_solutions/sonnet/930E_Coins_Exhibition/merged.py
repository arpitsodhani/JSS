# Clause setup_environment [Confidence: 0.60]
import sys

MOD = 1000000007
INV2 = 500000004


# Clause solve_logic [Confidence: 1.00]
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    nums = [int(x) for x in raw]
    k, n, m = nums[0], nums[1], nums[2]
    lim0 = {}
    lim1 = {}
    useful = [k, k - 1]
    q = 3

    for _ in range(n):
        l = nums[q]
        r = nums[q + 1]
        q += 2
        if r not in lim0 or lim0[r] < l:
            lim0[r] = l
        useful.append(r)
        useful.append(l - 1)

    for _ in range(m):
        l = nums[q]
        r = nums[q + 1]
        q += 2
        if r not in lim1 or lim1[r] < l:
            lim1[r] = l
        useful.append(r)
        useful.append(l - 1)

    useful = sorted(set(x for x in useful if 0 < x <= k))
    pref0 = {0: 1}
    pref1 = {0: 1}
    state0 = 1
    state1 = 1
    pos = 0
    bound0 = 0
    bound1 = 0

    for x in useful:
        event = x in lim0 or x in lim1
        pieces = (x - 1 - pos, 1) if event else (x - pos,)

        for step, length in enumerate(pieces):
            if event and step == 1:
                v0 = lim0.get(x, 0)
                v1 = lim1.get(x, 0)
                if v0 > bound0:
                    bound0 = v0
                if v1 > bound1:
                    bound1 = v1

            if length > 0:
                a = pref1[bound0 - 1] if bound0 else 0
                b = pref0[bound1 - 1] if bound1 else 0
                p2 = pow(2, length, MOD)
                total = (p2 * (state0 + state1) - (p2 - 1) * (a + b)) % MOD
                state0 = (total + b - a) * INV2 % MOD
                state1 = (total - b + a) * INV2 % MOD
                pos += length

        pref0[x] = state0
        pref1[x] = state1

    ans = (state0 + state1 - pref0.get(k - 1, 1) - pref1.get(k - 1, 1)) % MOD
    sys.stdout.write(str(ans) + "\n")


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


