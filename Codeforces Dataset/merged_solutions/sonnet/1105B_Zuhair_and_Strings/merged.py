# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    k = int(tokens[1])
    s = tokens[2]
    answer = 0
    left = 0
    while left < n:
        right = left + 1
        while right < n and s[right] == s[left]:
            right += 1
        count = (right - left) // k
        if count > answer:
            answer = count
        left = right


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write(str(answer))

if __name__ == "__main__":
    main()


