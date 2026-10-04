# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def decide(n, arr, fact):
    mx = max(arr)
    mx_count = 0
    near_count = 0

    for value in arr:
        if value == mx:
            mx_count += 1

    if mx_count >= 2:
        return fact[n]

    for value in arr:
        if value == mx - 1:
            near_count += 1

    if near_count == 0:
        return 0

    all_orders = fact[n]
    blocked = all_orders * pow(near_count + 1, MOD - 2, MOD) % MOD
    return (all_orders - blocked) % MOD

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    index = 1
    parsed = []
    limit = 0

    for _ in range(t):
        n = data[index]
        index += 1
        values = data[index:index + n]
        index += n
        parsed.append((n, values))
        if n > limit:
            limit = n

    fact = [1] * (limit + 1)
    number = 1
    while number <= limit:
        fact[number] = fact[number - 1] * number % MOD
        number += 1

    result = []
    for n, values in parsed:
        result.append(str(decide(n, values, fact)))

    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
main()
