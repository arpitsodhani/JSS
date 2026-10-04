# CLAUSE: setup_environment
import sys

MOD = 10 ** 9 + 7

# CLAUSE: solve_logic
def solve_case(n, k, arr):
    indices = {}
    dp = [(0, 0)] * (n + 1)
    dp[0] = (0, 1)

    for i in range(1, n + 1):
        color = arr[i - 1]
        if color not in indices:
            indices[color] = []
        indices[color].append(i)

        length, count = dp[i - 1]
        group = indices[color]

        if len(group) >= k:
            left = group[len(group) - k]
            previous_length, previous_count = dp[left - 1]
            candidate_length = previous_length + 1
            if candidate_length > length:
                length = candidate_length
                count = previous_count
            elif candidate_length == length:
                count += previous_count
                if count >= MOD:
                    count %= MOD

        dp[i] = (length, count % MOD)

    return dp[n][1] % MOD

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 1
    result = []
    for _ in range(data[0]):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        arr = data[pos:pos + n]
        pos += n
        result.append(str(solve_case(n, k, arr)))

# CLAUSE: finish_program
    print("\n".join(result))

if __name__ == "__main__":
    main()
