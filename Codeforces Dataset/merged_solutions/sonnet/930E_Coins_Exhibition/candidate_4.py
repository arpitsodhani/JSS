import sys

# CLAUSE: setup_environment
MOD = 1000000007
INV2 = 500000004

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    k, n, m = values[:3]
    events = {}
    marks = {k, k - 1}
    i = 3

    for _ in range(n):
        l = values[i]
        r = values[i + 1]
        i += 2
        old0, old1 = events.get(r, (0, 0))
        events[r] = (max(old0, l), old1)
        marks.add(r)
        marks.add(l - 1)

    for _ in range(m):
        l = values[i]
        r = values[i + 1]
        i += 2
        old0, old1 = events.get(r, (0, 0))
        events[r] = (old0, max(old1, l))
        marks.add(r)
        marks.add(l - 1)

    positions = sorted(x for x in marks if 0 < x <= k)
    pref = {0: (1, 1)}
    z = 1
    o = 1
    last = 0
    forbid_z = 0
    forbid_o = 0

    for x in positions:
        ez, eo = events.get(x, (0, 0))

        if ez or eo:
            gap = x - 1 - last
            if gap > 0:
                cz = pref[forbid_z - 1][1] if forbid_z else 0
                co = pref[forbid_o - 1][0] if forbid_o else 0
                p2 = pow(2, gap, MOD)
                s = (p2 * (z + o) - (p2 - 1) * (cz + co)) % MOD
                z = (s + co - cz) * INV2 % MOD
                o = (s - co + cz) * INV2 % MOD
                last = x - 1

            if ez > forbid_z:
                forbid_z = ez
            if eo > forbid_o:
                forbid_o = eo

            cz = pref[forbid_z - 1][1] if forbid_z else 0
            co = pref[forbid_o - 1][0] if forbid_o else 0
            s = (2 * (z + o) - (cz + co)) % MOD
            z = (s + co - cz) * INV2 % MOD
            o = (s - co + cz) * INV2 % MOD
            last = x
        else:
            gap = x - last
            if gap > 0:
                cz = pref[forbid_z - 1][1] if forbid_z else 0
                co = pref[forbid_o - 1][0] if forbid_o else 0
                p2 = pow(2, gap, MOD)
                s = (p2 * (z + o) - (p2 - 1) * (cz + co)) % MOD
                z = (s + co - cz) * INV2 % MOD
                o = (s - co + cz) * INV2 % MOD
                last = x

        pref[x] = (z, o)

    before = pref[k - 1]
    print((z + o - before[0] - before[1]) % MOD)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
