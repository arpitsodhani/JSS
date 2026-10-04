# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 998244353

def ints():
    data = sys.stdin.buffer.read()
    num = 0
    in_num = False
    for b in data:
        if 48 <= b <= 57:
            num = num * 10 + (b - 48)
            in_num = True
        elif in_num:
            yield num
            num = 0
            in_num = False
    if in_num:
        yield num

def main():
    it = ints()
    n = next(it)
    m = next(it)
    total = n * m
    base = total

    cells = []
    for i in range(n):
        for j in range(m):
            value = next(it)
            cells.append(value * base + i * m + j)

    r = next(it) - 1
    c = next(it) - 1
    target = r * m + c

    cells.sort()

    inv = [0] * (total + 1)
    inv[1] = 1
    for i in range(2, total + 1):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD

    count = 0
    sum_i = 0
    sum_j = 0
    sum_sq = 0
    sum_dp = 0

    answer = 0
    pos = 0

    while pos < total:
        value = cells[pos] // base
        end = pos
        while end < total and cells[end] // base == value:
            end += 1

        group_i = 0
        group_j = 0
        group_sq = 0
        group_dp = 0

        if count == 0:
            for k in range(pos, end):
                idx = cells[k] % base
                x = idx // m + 1
                y = idx % m + 1

                if idx == target:
                    answer = 0

                group_i = (group_i + x) % MOD
                group_j = (group_j + y) % MOD
                group_sq = (group_sq + x * x + y * y) % MOD
        else:
            inv_count = inv[count]

            for k in range(pos, end):
                idx = cells[k] % base
                x = idx // m + 1
                y = idx % m + 1

                cur = sum_dp
                cur += count * (x * x + y * y)
                cur -= 2 * x * sum_i
                cur -= 2 * y * sum_j
                cur += sum_sq
                cur %= MOD
                cur = cur * inv_count % MOD

                if idx == target:
                    answer = cur

                group_i = (group_i + x) % MOD
                group_j = (group_j + y) % MOD
                group_sq = (group_sq + x * x + y * y) % MOD
                group_dp = (group_dp + cur) % MOD

        count += end - pos
        sum_i = (sum_i + group_i) % MOD
        sum_j = (sum_j + group_j) % MOD
        sum_sq = (sum_sq + group_sq) % MOD
        sum_dp = (sum_dp + group_dp) % MOD

        pos = end

    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
