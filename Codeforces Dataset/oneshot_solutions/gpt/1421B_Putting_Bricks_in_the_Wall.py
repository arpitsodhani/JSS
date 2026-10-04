import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        g = data[idx:idx + n]
        idx += n

        a = [(0, 1), (1, 0)]
        b = [(n - 2, n - 1), (n - 1, n - 2)]

        ans0 = []
        for r, c in a:
            if g[r][c] != '0':
                ans0.append((r + 1, c + 1))
        for r, c in b:
            if g[r][c] != '1':
                ans0.append((r + 1, c + 1))

        ans1 = []
        for r, c in a:
            if g[r][c] != '1':
                ans1.append((r + 1, c + 1))
        for r, c in b:
            if g[r][c] != '0':
                ans1.append((r + 1, c + 1))

        ans = ans0 if len(ans0) <= len(ans1) else ans1
        out.append(str(len(ans)))
        for r, c in ans:
            out.append(f"{r} {c}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
