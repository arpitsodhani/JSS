import sys

def min_max_digit(x):
    mn = 9
    mx = 0
    while x:
        d = x % 10
        if d < mn:
            mn = d
        if d > mx:
            mx = d
        x //= 10
    return mn, mx

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    ans = []
    idx = 1

    for _ in range(t):
        a = int(data[idx])
        k = int(data[idx + 1])
        idx += 2

        for _ in range(k - 1):
            mn, mx = min_max_digit(a)
            if mn == 0:
                break
            a += mn * mx

        ans.append(str(a))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
