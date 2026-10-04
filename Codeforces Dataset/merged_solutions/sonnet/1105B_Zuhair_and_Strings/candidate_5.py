# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.readline().split()
    n = int(data[0])
    k = int(data[1])
    s = sys.stdin.readline().strip()
    runs = []
    length = 1
    for index in range(1, n):
        if s[index] == s[index - 1]:
            length += 1
        else:
            runs.append(length)
            length = 1
    runs.append(length)
    answer = max((value // k for value in runs), default=0)

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
