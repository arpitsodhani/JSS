# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def process(n, limit, pairs):
    finishes = []
    head = 0
    answers = []
    for t, d in pairs:
        while head < len(finishes) and finishes[head] <= t:
            head += 1
        active = len(finishes) - head
        if active > limit:
            answers.append(-1)
            continue
        if active == 0:
            done = t + d
        else:
            done = finishes[-1] + d
        finishes.append(done)
        answers.append(done)
    return answers

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    if not nums:
        return
    n = nums[0]
    b = nums[1]
    pairs = zip(nums[2::2], nums[3::2])
    ans = process(n, b, pairs)
    sys.stdout.write(" ".join(map(str, ans)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
