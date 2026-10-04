# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = sys.stdin.buffer.read().split()
    at = 0
    n = int(data[at])
    m = int(data[at + 1])
    q = int(data[at + 2])
    at += 3

    masks = [[0] * 26 for _ in range(m)]

    for row in range(n):
        line = data[at]
        at += 1
        bit = 1 << row
        for col, value in enumerate(line):
            masks[col][value - 97] |= bit

    result = []
    for _ in range(q):
        query = data[at]
        at += 1

        active = masks[0][query[0] - 97]
        if active == 0:
            result.append("-1")
            continue

        answer = 0
        ok = True
        for col in range(1, m):
            choices = masks[col][query[col] - 97]
            if choices == 0:
                ok = False
                break
            overlap = active & choices
            if overlap:
                active = overlap
            else:
                answer += 1
                active = choices

        if ok:
            result.append(str(answer))
        else:
            result.append("-1")

    sys.stdout.write("\n".join(result))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


