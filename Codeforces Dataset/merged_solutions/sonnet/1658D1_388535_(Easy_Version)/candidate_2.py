# CLAUSE: setup_environment
import sys

def possible(candidate, values, left, right):
    used = set()
    for item in values:
        restored = item ^ candidate
        if restored < left or restored > right or restored in used:
            return False
        used.add(restored)
    return True

# CLAUSE: solve_logic
def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    tests = numbers[pos]
    pos += 1
    answers = []
    for _ in range(tests):
        left = numbers[pos]
        right = numbers[pos + 1]
        pos += 2
        length = right - left + 1
        values = numbers[pos:pos + length]
        pos += length
        bound = 1
        highest = max(left, right, max(values))
        while bound <= highest:
            bound <<= 1
        result = 0
        for candidate in range(bound):
            if possible(candidate, values, left, right):
                result = candidate
                break
        answers.append(str(result))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
