# CLAUSE: setup_environment
import sys

MOD = 1000000007

def factorial_tables(n):
    factorial = [1]
    for x in range(1, n + 1):
        factorial.append(factorial[-1] * x % MOD)

    inverse_factorial = [1] * (n + 1)
    inverse_factorial[-1] = pow(factorial[-1], MOD - 2, MOD)

    x = n
    while x:
        inverse_factorial[x - 1] = inverse_factorial[x] * x % MOD
        x -= 1

    return factorial, inverse_factorial

def combination(factorial, inverse_factorial, n, k):
    if k < 0 or n < k:
        return 0
    return factorial[n] * inverse_factorial[k] % MOD * inverse_factorial[n - k] % MOD

# CLAUSE: solve_logic
def excellent_arrays(n, l, r, factorial, inverse_factorial):
    half_down = n // 2
    half_up = n - half_down
    left_capacity = 1 - l
    right_capacity = r - n
    shared = min(left_capacity, right_capacity)

    balanced = combination(factorial, inverse_factorial, n, half_down)
    if half_down != half_up:
        balanced = 2 * balanced % MOD

    ans = shared % MOD * balanced % MOD
    end = shared + half_up

    for d in range(shared + 1, end + 1):
        fixed_from_left = d - left_capacity if d > left_capacity else 0
        fixed_from_right = d - right_capacity if d > right_capacity else 0
        open_slots = n - fixed_from_left - fixed_from_right

        if open_slots >= 0:
            add = combination(factorial, inverse_factorial, open_slots, half_down - fixed_from_left)
            if half_down != half_up:
                add += combination(factorial, inverse_factorial, open_slots, half_up - fixed_from_left)
            ans = (ans + add) % MOD

    return ans

# CLAUSE: finish_program
def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    max_size = 0

    for i in range(t):
        base = 1 + 3 * i
        case = (numbers[base], numbers[base + 1], numbers[base + 2])
        cases.append(case)
        max_size = max(max_size, case[0])

    factorial, inverse_factorial = factorial_tables(max_size)
    result = []
    for case in cases:
        result.append(str(excellent_arrays(*case, factorial, inverse_factorial)))

    sys.stdout.write("\n".join(result))

main()
