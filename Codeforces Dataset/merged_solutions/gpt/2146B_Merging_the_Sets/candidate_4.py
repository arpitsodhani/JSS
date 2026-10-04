# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2

        sets = []
        freq = [0] * (m + 1)

        for _ in range(n):
            l = data[idx]
            idx += 1
            s = data[idx:idx + l]
            idx += l
            sets.append(s)
            for x in s:
                freq[x] += 1

        if any(freq[x] == 0 for x in range(1, m + 1)):
            ans.append("NO")
            continue

        removable = 0
        for s in sets:
            ok = True
            for x in s:
                if freq[x] == 1:
                    ok = False
                    break
            if ok:
                removable += 1

        ans.append("YES" if removable >= 2 else "NO")

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
