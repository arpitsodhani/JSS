import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        b = data[idx:idx + n]
        idx += n

        pref = [0] * n
        pref[0] = b[0] + 1
        for i in range(1, n):
            pref[i] = max(pref[i - 1], b[i] + i + 1)

        suff = [0] * n
        suff[-1] = b[-1] - n
        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i + 1], b[i] - (i + 1))

        best = -10**30
        for j in range(1, n - 1):
            best = max(best, pref[j - 1] + b[j] + suff[j + 1])

        ans.append(str(best))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
