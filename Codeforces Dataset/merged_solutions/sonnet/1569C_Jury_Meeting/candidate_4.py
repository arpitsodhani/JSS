# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    ptr = 1
    tests = []
    sizes = []

    for _ in range(t):
        n = int(raw[ptr])
        ptr += 1
        arr = [int(x) for x in raw[ptr:ptr + n]]
        ptr += n
        tests.append(arr)
        sizes.append(n)

    upto = max(sizes) if sizes else 0
    factorials = [1]
    cur = 1
    for i in range(1, upto + 1):
        cur = cur * i % MOD
        factorials.append(cur)

    out = []
    for arr, n in zip(tests, sizes):
        first = -1
        second = -1
        count_first = 0
        count_second = 0

        for value in arr:
            if value > first:
                second = first
                count_second = count_first
                first = value
                count_first = 1
            elif value == first:
                count_first += 1
            elif value > second:
                second = value
                count_second = 1
            elif value == second:
                count_second += 1

        if count_first > 1:
            out.append(str(factorials[n]))
        elif first - second != 1:
            out.append("0")
        else:
            total = factorials[n]
            out.append(str((total - total * pow(count_second + 1, MOD - 2, MOD)) % MOD))

    print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
