import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n, k, x = data[idx], data[idx + 1], data[idx + 2]
    idx += 3

    if x != 1:
        out.append("YES")
        out.append(str(n))
        out.append(" ".join(["1"] * n))
    else:
        if k == 1:
            out.append("NO")
        elif n % 2 == 0:
            out.append("YES")
            out.append(str(n // 2))
            out.append(" ".join(["2"] * (n // 2)))
        elif k >= 3 and n >= 3:
            parts = ["3"] + ["2"] * ((n - 3) // 2)
            out.append("YES")
            out.append(str(len(parts)))
            out.append(" ".join(parts))
        else:
            out.append("NO")

print("\n".join(out))
