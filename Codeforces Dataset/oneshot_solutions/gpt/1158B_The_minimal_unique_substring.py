import sys

data = sys.stdin.read().split()
n, k = map(int, data[:2])

if k == 1:
    ans = "0" * (n - 1) + "1"
else:
    d = (n - k + 2) // 2
    if d == 1:
        ans = "1" * n
    else:
        c = "0" * (d - 1) + "1"
        need = k - 2
        pref = (c * ((need + d - 1) // d))[:need]
        ans = c + c + pref

sys.stdout.write(ans)
