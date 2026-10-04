# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from bisect import bisect_right

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n = data[0]
    ops = []
    times_by_x = {}

    idx = 1
    for _ in range(n):
        typ = data[idx]
        t = data[idx + 1]
        x = data[idx + 2]
        idx += 3
        ops.append((typ, t, x))
        if typ != 3:
            times_by_x.setdefault(x, []).append(t)

    struct = {}
    for x, times in times_by_x.items():
        coords = sorted(set(times))
        struct[x] = [coords, [0] * (len(coords) + 1)]

    ans = []

    for typ, t, x in ops:
        if typ == 3:
            if x not in struct:
                ans.append("0")
                continue
            coords, bit = struct[x]
            i = bisect_right(coords, t)
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            ans.append(str(s))
        else:
            coords, bit = struct[x]
            i = bisect_right(coords, t)
            delta = 1 if typ == 1 else -1
            while i < len(bit):
                bit[i] += delta
                i += i & -i

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
