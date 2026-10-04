# CLAUSE: setup_environment
import sys

def read_cases(nums):
    cursor = 1
    for _ in range(nums[0]):
        low, high = nums[cursor], nums[cursor + 1]
        cursor += 2
        count = high - low + 1
        block = nums[cursor:cursor + count]
        cursor += count
        yield low, high, block

def transformed_set(values, key):
    return {value ^ key for value in values}

# CLAUSE: solve_logic
def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    lines = []
    for low, high, block in read_cases(nums):
        required = set(range(low, high + 1))
        top = max(max(block), high, low)
        found = 0
        for key in range(1 << top.bit_length()):
            if transformed_set(block, key) == required:
                found = key
                break
        lines.append(str(found))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
