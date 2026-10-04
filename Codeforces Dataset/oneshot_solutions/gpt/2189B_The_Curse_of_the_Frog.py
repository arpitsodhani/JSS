import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    p = 1
    ans = []

    for _ in range(t):
        x = data[p]
        n = data[p + 1]
        p += 2

        free = 0
        best = -10**30

        for _ in range(n):
            a = data[p]
            b = data[p + 1]
            c = data[p + 2]
            p += 3

            free += a * (b - 1)
            best = max(best, a * b - c)

        if free >= x:
            ans.append("0")
        elif best <= 0:
            ans.append("-1")
        else:
            need = x - free
            ans.append(str((need + best - 1) // best))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
