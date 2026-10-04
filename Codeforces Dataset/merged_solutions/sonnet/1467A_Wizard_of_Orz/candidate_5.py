# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    tests = nums[0]
    cycle = tuple("9012345678")
    answers = []
    for n in nums[1:tests + 1]:
        if n == 1:
            answers.append("9")
            continue
        pieces = ["98"]
        remaining = n - 2
        full, extra = divmod(remaining, 10)
        pieces.extend(["".join(cycle)] * full)
        pieces.append("".join(cycle[:extra]))
        answers.append("".join(pieces))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
