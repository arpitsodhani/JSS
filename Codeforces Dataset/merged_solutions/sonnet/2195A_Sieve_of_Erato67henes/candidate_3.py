# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def contains_target(values, start, count):
    end = start + count
    while start < end:
        if values[start] == 67:
            return True
        start += 1
    return False

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    index = 1
    answers = []
    for _ in range(nums[0]):
        n = nums[index]
        index += 1
        answers.append("YES" if contains_target(nums, index, n) else "NO")
        index += n

# CLAUSE: finish_program
    print("\n".join(answers))

if __name__ == "__main__":
    main()
