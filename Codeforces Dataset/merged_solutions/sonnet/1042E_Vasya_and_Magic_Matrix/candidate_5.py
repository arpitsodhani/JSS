# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def main():
    tokens = [int(x) for x in sys.stdin.buffer.read().split()]
    n, m = tokens[0], tokens[1]
    total = n * m
    groups = {}
    for idx in range(total):
        value = tokens[idx + 2]
        if value in groups:
            groups[value].append(idx)
        else:
            groups[value] = [idx]

    r = tokens[total + 2] - 1
    c = tokens[total + 3] - 1
    target = r * m + c

    processed = 0
    row_sum = 0
    col_sum = 0
    square_sum = 0
    dp_sum = 0
    answer = 0

    for value in sorted(groups):
        indices = groups[value]
        local_row = 0
        local_col = 0
        local_square = 0
        local_dp = 0

        if processed:
            inv_processed = pow(processed, MOD - 2, MOD)
            for idx in indices:
                row = idx // m + 1
                col = idx % m + 1
                square = row * row + col * col
                dp = dp_sum
                dp += processed * square
                dp -= 2 * row * row_sum
                dp -= 2 * col * col_sum
                dp += square_sum
                dp %= MOD
                dp = dp * inv_processed % MOD
                if idx == target:
                    answer = dp
                local_row = (local_row + row) % MOD
                local_col = (local_col + col) % MOD
                local_square = (local_square + square) % MOD
                local_dp = (local_dp + dp) % MOD
        else:
            for idx in indices:
                row = idx // m + 1
                col = idx % m + 1
                square = row * row + col * col
                if idx == target:
                    answer = 0
                local_row = (local_row + row) % MOD
                local_col = (local_col + col) % MOD
                local_square = (local_square + square) % MOD

        processed += len(indices)
        row_sum = (row_sum + local_row) % MOD
        col_sum = (col_sum + local_col) % MOD
        square_sum = (square_sum + local_square) % MOD
        dp_sum = (dp_sum + local_dp) % MOD

    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
