# Clause setup_environment [Confidence: 0.60]
import sys

MOD = 998244353


# Clause solve_logic [Confidence: 0.60]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    total = n * m
    values = data[2:2 + total]
    r = data[2 + total] - 1
    c = data[3 + total] - 1
    target = r * m + c

    cells = []
    for idx, value in enumerate(values):
        cells.append((value, idx))
    cells.sort(key=lambda item: item[0])

    seen = 0
    sum_x = 0
    sum_y = 0
    sum_norm = 0
    sum_expect = 0
    answer = 0
    left = 0

    while left < total:
        value = cells[left][0]
        right = left
        while right < total and cells[right][0] == value:
            right += 1

        add_x = 0
        add_y = 0
        add_norm = 0
        add_expect = 0
        inv_seen = pow(seen, MOD - 2, MOD) if seen else 0

        for k in range(left, right):
            idx = cells[k][1]
            x = idx // m + 1
            y = idx % m + 1
            norm = x * x + y * y

            if seen:
                expect = sum_expect
                expect = (expect + seen * norm) % MOD
                expect = (expect - 2 * x * sum_x) % MOD
                expect = (expect - 2 * y * sum_y) % MOD
                expect = (expect + sum_norm) % MOD
                expect = expect * inv_seen % MOD
            else:
                expect = 0

            if idx == target:
                answer = expect

            add_x = (add_x + x) % MOD
            add_y = (add_y + y) % MOD
            add_norm = (add_norm + norm) % MOD
            add_expect = (add_expect + expect) % MOD

        seen += right - left
        sum_x = (sum_x + add_x) % MOD
        sum_y = (sum_y + add_y) % MOD
        sum_norm = (sum_norm + add_norm) % MOD
        sum_expect = (sum_expect + add_expect) % MOD
        left = right

    print(answer)


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


