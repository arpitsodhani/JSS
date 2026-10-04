# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    largest = 1
    pointer = 1

    while len(cases) < t:
        n = int(data[pointer])
        m = int(data[pointer + 1])
        k = int(data[pointer + 2])
        pointer += 3
        cases.append([n, m, k])
        if n + m > largest:
            largest = n + m

    inv = [0 for _ in range(largest + 1)]
    inv[1] = 1
    current = 2
    while current <= largest:
        inv[current] = (MOD - MOD // current) * inv[MOD % current] % MOD
        current += 1

    results = []
    for n, m, k in cases:
        border = k - 1
        if n * m <= border:
            results.append("0")
            continue

        result = 1
        width = border // n + 1
        if width < 1:
            width = 1
        while width < m:
            result = (result + inv[width + border // width]) % MOD
            width += 1

        height = border // m + 1
        if height < 1:
            height = 1
        while height < n:
            result = (result + inv[height + border // height]) % MOD
            height += 1

        results.append(str(result))

    print("\n".join(results))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
