# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    cases = int(raw[0])
    index = 1
    answers = []
    for _ in range(cases):
        n = int(raw[index])
        index += 1
        freq = {}
        limit = n + 1
        for _ in range(n):
            num = int(raw[index])
            index += 1
            if num <= limit:
                freq[num] = freq.get(num, 0) + 1
        score = 0
        current = 0
        while freq.get(current, 0) > 0:
            freq[current] -= 1
            current += 1
        score += current
        current = 0
        while freq.get(current, 0) > 0:
            freq[current] -= 1
            current += 1
        score += current
        answers.append(str(score))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
