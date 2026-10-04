# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    n = nums[0]
    specs = []
    prices = []
    ids = []

    at = 1
    for i in range(n):
        specs.append(tuple(nums[at:at + 3]))
        prices.append(nums[at + 3])
        ids.append(i + 1)
        at += 4

    answer_id = -1
    answer_price = 10 ** 20

    for i in range(n):
        speed, ram, hdd = specs[i]
        if any(speed < s and ram < r and hdd < h for s, r, h in specs):
            continue
        if prices[i] < answer_price:
            answer_price = prices[i]
            answer_id = ids[i]

    print(answer_id)

# CLAUSE: finish_program
main()
