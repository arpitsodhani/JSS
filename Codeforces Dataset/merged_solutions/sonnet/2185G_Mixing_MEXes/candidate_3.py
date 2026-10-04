# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def add_count(box, value):
    box[value] = box.get(value, 0) + 1

def array_info(arr):
    freq = {}
    for value in arr:
        freq[value] = freq.get(value, 0) + 1
    mex = 0
    while mex in freq:
        mex += 1
    nxt = mex + 1
    while nxt in freq:
        nxt += 1
    loss = 0
    for value in range(mex):
        if freq.get(value, 0) == 1:
            loss += value - mex
    return mex, nxt, loss

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    tests = nums[at]
    at += 1
    answers = []
    for _ in range(tests):
        n = nums[at]
        at += 1
        stored = []
        total = {}
        length_sum = 0
        for _ in range(n):
            m = nums[at]
            at += 1
            arr = nums[at:at + m]
            at += m
            stored.append(arr)
            length_sum += m
            for value in arr:
                add_count(total, value)

        base_sum = 0
        removal_sum = 0
        mex_pairs = []
        for arr in stored:
            mex, nxt, loss = array_info(arr)
            base_sum += mex
            removal_sum += loss
            mex_pairs.append((mex, nxt))

        gain_sum = 0
        for mex, nxt in mex_pairs:
            gain_sum += total.get(mex, 0) * (nxt - mex)

        answers.append(str(length_sum * (n - 1) * base_sum + (n - 1) * removal_sum + gain_sum))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
main()
