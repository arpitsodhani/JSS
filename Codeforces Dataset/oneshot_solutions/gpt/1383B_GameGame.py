import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        res = "DRAW"
        for b in range(30, -1, -1):
            cnt = sum((x >> b) & 1 for x in a)
            if cnt % 2 == 0:
                continue
            if cnt % 4 == 1:
                res = "WIN"
            else:
                res = "WIN" if (n - cnt) % 2 == 1 else "LOSE"
            break

        ans.append(res)

    print("\n".join(ans))

if __name__ == "__main__":
    solve()
