import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    ans = []
    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        y = int(data[idx + 2])
        a = data[idx + 3]
        b = data[idx + 4]
        idx += 5

        diff = [i for i in range(n) if a[i] != b[i]]
        m = len(diff)

        if m % 2:
            ans.append("-1")
        elif m == 0:
            ans.append("0")
        elif m == 2 and diff[1] == diff[0] + 1:
            if n == 2:
                ans.append(str(x))
            else:
                ans.append(str(min(x, 2 * y)))
        else:
            ans.append(str((m // 2) * y))

    print("\n".join(ans))

if __name__ == "__main__":
    solve()
