import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, k = map(int, data)

    colors = 0
    p = 1
    while p < n:
        p *= k
        colors += 1

    vals = []
    for x in range(n):
        a = [0] * colors
        y = x
        s = 0
        for i in range(colors):
            a[i] = y % k
            s += a[i]
            y //= k
        vals.append((s, a))

    vals.sort()
    digits = [a for _, a in vals]

    ans = []
    for i in range(n):
        ai = digits[i]
        for j in range(i + 1, n):
            aj = digits[j]
            for c in range(colors):
                if ai[c] < aj[c]:
                    ans.append(str(c + 1))
                    break

    sys.stdout.write(str(colors) + "\n")
    sys.stdout.write(" ".join(ans) + "\n")

if __name__ == "__main__":
    main()
