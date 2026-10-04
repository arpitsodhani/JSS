import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2

        a = data[idx:idx + n]
        idx += n
        a.sort()

        pref = [0] * (n + 1)
        for i, x in enumerate(a):
            pref[i + 1] = pref[i] + x

        total = pref[n]
        best = 0

        for pairs_removed in range(k + 1):
            left_removed = 2 * pairs_removed
            right_removed = k - pairs_removed
            current = total - pref[left_removed] - (pref[n] - pref[n - right_removed])
            if current > best:
                best = current

        ans.append(str(best))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
