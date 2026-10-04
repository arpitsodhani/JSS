# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    lines = sys.stdin.read().splitlines()
    heading = lines[0] if lines else ""
    text = lines[1] if len(lines) > 1 else ""

    available = Counter(ch for ch in heading if ch != " ")

    for ch in text:
        if ch != " ":
            if available[ch] <= 0:
                print("NO")
                return
            available[ch] -= 1

    print("YES")


# Clause finish_program [Confidence: 0.80]
main()


