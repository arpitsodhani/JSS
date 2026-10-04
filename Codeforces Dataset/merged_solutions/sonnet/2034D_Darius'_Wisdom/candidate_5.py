# CLAUSE: setup_environment
import sys

def main():
    raw = sys.stdin.buffer.read().split()
    tests = int(raw[0])
    cur = 1
    lines = []

# CLAUSE: solve_logic
    for _ in range(tests):
        n = int(raw[cur])
        cur += 1
        a = [int(x) for x in raw[cur:cur + n]]
        cur += n

        c0 = sum(x == 0 for x in a)
        c1 = sum(x == 1 for x in a)
        c01 = c0 + c1
        ops = []

        zero_bad = set()
        one_any = set()
        for i in range(n):
            if a[i] == 1:
                one_any.add(i)
            elif a[i] == 0 and i >= c0:
                zero_bad.add(i)

        def apply(i, j):
            old_i = a[i]
            old_j = a[j]

            if old_i == 1:
                one_any.discard(i)
            if old_j == 1:
                one_any.discard(j)
            if i >= c0 and old_i == 0:
                zero_bad.discard(i)
            if j >= c0 and old_j == 0:
                zero_bad.discard(j)

            if old_i > old_j:
                ops.append((i + 1, j + 1))
            else:
                ops.append((j + 1, i + 1))

            a[i] = old_j
            a[j] = old_i

            if a[i] == 1:
                one_any.add(i)
            if a[j] == 1:
                one_any.add(j)
            if i >= c0 and a[i] == 0:
                zero_bad.add(i)
            if j >= c0 and a[j] == 0:
                zero_bad.add(j)

        i = 0
        while i < c0:
            if a[i] == 1:
                apply(i, next(iter(zero_bad)))
            elif a[i] == 2:
                apply(i, next(iter(one_any)))
                apply(i, next(iter(zero_bad)))
            i += 1

        misplaced_ones = set()
        for i in range(c01, n):
            if a[i] == 1:
                misplaced_ones.add(i)

        i = c0
        while i < c01:
            if a[i] == 2:
                apply(i, misplaced_ones.pop())
            i += 1

        lines.append(str(len(ops)))
        for op in ops:
            lines.append(str(op[0]) + " " + str(op[1]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
