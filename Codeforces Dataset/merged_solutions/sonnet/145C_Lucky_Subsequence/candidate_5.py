# CLAUSE: setup_environment
import sys

MOD = 1000000007

LUCKY = set()
frontier = [4, 7]
while frontier:
    value = frontier.pop()
    if value > 10000000000:
        continue
    LUCKY.add(value)
    frontier.append(value * 10 + 4)
    frontier.append(value * 10 + 7)

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n, k = nums[0], nums[1]

    by_value = {}
    not_lucky = 0
    for number in nums[2:]:
        if number in LUCKY:
            if number in by_value:
                by_value[number] += 1
            else:
                by_value[number] = 1
        else:
            not_lucky += 1

    inv = [0] * (n + 2)
    if n + 1 > 1:
        inv[1] = 1
    for i in range(2, n + 2):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

    choose_unlucky = [0] * (min(k, not_lucky) + 1)
    choose_unlucky[0] = 1
    for r in range(1, len(choose_unlucky)):
        choose_unlucky[r] = choose_unlucky[r - 1] * (not_lucky - r + 1) % MOD * inv[r] % MOD

    selected = [0] * (len(by_value) + 1)
    selected[0] = 1
    size = 0
    for frequency in by_value.values():
        for used in range(size, -1, -1):
            selected[used + 1] = (selected[used + 1] + selected[used] * frequency) % MOD
        size += 1

    result = 0
    max_lucky = min(k, len(by_value))
    for lucky_used in range(max_lucky + 1):
        unlucky_used = k - lucky_used
        if 0 <= unlucky_used < len(choose_unlucky):
            result = (result + selected[lucky_used] * choose_unlucky[unlucky_used]) % MOD

    print(result)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
