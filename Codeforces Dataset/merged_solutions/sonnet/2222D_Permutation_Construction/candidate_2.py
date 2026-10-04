# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    answers = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        prefix = 0
        keyed = []
        for i in range(n):
            keyed.append((prefix, i))
            prefix += int(data[pos + i])
        pos += n
        keyed.sort()
        p = [0] * n
        cur = n
        for _, idx in keyed:
            p[idx] = cur
            cur -= 1
        answers.append(" ".join(map(str, p)))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
