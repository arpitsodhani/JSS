# CLAUSE: setup_environment
import sys

def upto(n):
    if n < 0:
        return 0
    table = (n, 1, n + 1, 0)
    return table[n % 4]

def banned(n, bit, residue):
    if n < residue:
        return 0
    block = 1 << bit
    last_index = (n - residue) // block
    amount = last_index + 1
    ans = upto(last_index) * block
    if amount % 2:
        ans ^= residue
    return ans

def range_answer(left, right, bit, residue):
    whole = upto(right) ^ upto(left - 1)
    removed = banned(right, bit, residue) ^ banned(left - 1, bit, residue)
    return whole ^ removed

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    tests = int(tokens[0])
    answers = []
    cursor = 1
    while tests:
        left = int(tokens[cursor])
        right = int(tokens[cursor + 1])
        bit = int(tokens[cursor + 2])
        residue = int(tokens[cursor + 3])
        cursor += 4
        answers.append(str(range_answer(left, right, bit, residue)))
        tests -= 1
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
