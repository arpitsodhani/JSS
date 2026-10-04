# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
powers = [1]
while powers[-1] <= 10 ** 18:
    powers.append(powers[-1] * 3)

def make_good_numbers(index, total, values):
    if index == len(powers):
        values.append(total)
        return
    make_good_numbers(index + 1, total, values)
    make_good_numbers(index + 1, total + powers[index], values)

good_values = []
make_good_numbers(0, 0, good_values)
good_values.sort()

def lower_bound(values, target):
    left = 0
    right = len(values)
    while left < right:
        mid = (left + right) // 2
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid
    return values[left]

def main():
    nums = list(map(int, sys.stdin.read().split()))
    q = nums[0]
    answers = [str(lower_bound(good_values, nums[i])) for i in range(1, q + 1)]
    print("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
