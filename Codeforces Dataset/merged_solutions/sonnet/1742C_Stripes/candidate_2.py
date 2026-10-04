# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.read().split()
    tests = int(tokens[0])
    pos = 1
    result = []
    for _ in range(tests):
        board = tokens[pos:pos + 8]
        pos += 8
        color = "B"
        for line in board:
            if line == "RRRRRRRR":
                color = "R"
                break
        result.append(color)

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
