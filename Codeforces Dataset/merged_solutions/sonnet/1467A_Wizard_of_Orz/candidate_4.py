# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def wizard(n):
    answer = []
    for pos in range(n):
        if pos == 0:
            answer.append("9")
        elif pos == 1:
            answer.append("8")
        else:
            answer.append(str((pos + 7) % 10))
    return "".join(answer)

def main():
    tokens = sys.stdin.read().strip().split()
    count = int(tokens[0])
    result = []
    index = 1
    while index <= count:
        result.append(wizard(int(tokens[index])))
        index += 1

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
