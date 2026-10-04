# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    data = sys.stdin.read().split()
    if len(data) == 1:
        moves = "".join(ch for ch in data[0] if ch in "UR")
    else:
        moves = data[1]

    balance = 0
    side = 0
    answer = 0

    for ch in moves:
        balance += 1 if ch == "R" else -1
        current = (balance > 0) - (balance < 0)
        if current == 0:
            continue
        if side and current != side:
            answer += 1
        side = current

    sys.stdout.write(str(answer))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


