import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        ok = False
        for i in range(n - 1):
            if abs(a[i] - a[i + 1]) <= 1:
                ok = True
                break

        if ok:
            ans.append("0")
        elif n == 2:
            ans.append("-1")
        else:
            ans.append("1")

    print("\n".join(ans))

if __name__ == "__main__":
    solve()
