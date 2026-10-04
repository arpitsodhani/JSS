# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    ans = []

    for _ in range(t):
        n = data[p]
        m = data[p + 1]
        p += 2

        elves = []
        for i in range(1, n + 1):
            elves.append((data[p], i))
            p += 1
        elves.sort()

        if n == 1:
            ans.append("0" if m == 1 else "-1")
            continue

        if m:
            if m > n // 2:
                ans.append("-1")
                continue
            ops = []
            for i in range(n - m):
                ops.append((elves[i + m][1], elves[i][1]))
            ans.append(str(len(ops)))
            for x, y in ops:
                ans.append(f"{x} {y}")
            continue

        if sum(v for v, _ in elves[:-1]) < elves[-1][0]:
            ans.append("-1")
            continue

        need = elves[-1][0]
        s = 0
        j = n - 2
        while j >= 0:
            s += elves[j][0]
            if s >= need:
                break
            j -= 1

        ops = []
        for i in range(j):
            ops.append((elves[i + 1][1], elves[i][1]))
        top = elves[-1][1]
        ops.append((top, elves[j][1]))
        for i in range(j + 1, n - 1):
            ops.append((elves[i][1], top))

        ans.append(str(len(ops)))
        for x, y in ops:
            ans.append(f"{x} {y}")


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()


