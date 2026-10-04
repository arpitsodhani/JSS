# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    ans = []
    limit = 70

    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n

        pref = [0] * (n + 1)
        pos = []
        for i, x in enumerate(a):
            pref[i + 1] = pref[i] + x
            if x > 1:
                pos.append(i)

        if not pos:
            ans.append("1 1")
        elif len(pos) > limit:
            ans.append(str(pos[0] + 1) + " " + str(pos[-1] + 1))
        else:
            best = 0
            left = 0
            right = 0
            for i in range(len(pos)):
                prod = 1
                for j in range(i, len(pos)):
                    prod *= a[pos[j]]
                    l = pos[i]
                    r = pos[j]
                    gain = prod - (pref[r + 1] - pref[l])
                    if gain > best:
                        best = gain
                        left = l
                        right = r
            ans.append(str(left + 1) + " " + str(right + 1))

    sys.stdout.write("\n".join(ans))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


