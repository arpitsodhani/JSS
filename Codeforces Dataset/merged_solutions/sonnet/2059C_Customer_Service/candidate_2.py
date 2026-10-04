# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def trailing_ones(row):
    total = 0
    for value in row[::-1]:
        if value != 1:
            break
        total += 1
    return total

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    tests = nums[pos]
    pos += 1
    out = []
    for _ in range(tests):
        n = nums[pos]
        pos += 1
        tails = []
        for _ in range(n):
            row = nums[pos:pos + n]
            pos += n
            tails.append(trailing_ones(row))
        tails.sort()
        wanted = 1
        for tail in tails:
            if tail >= wanted:
                wanted += 1
        out.append(str(n if wanted > n else wanted))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
