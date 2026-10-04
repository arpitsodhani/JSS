# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    it = iter(raw)
    n = int(next(it))
    q = int(next(it))
    v = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    b = [int(next(it)) for _ in range(n)]
    answers = []
    for _ in range(q):
        typ = int(next(it))
        if typ == 1:
            i = int(next(it)) - 1
            x = int(next(it))
            b[i] = x
            continue
        l = int(next(it)) - 1
        r = int(next(it)) - 1
        possible = []
        for i in range(l, r + 1):
            combined = 0
            largest = a[i]
            for j in range(i, r + 1):
                combined |= b[j]
                if a[j] > largest:
                    largest = a[j]
                if combined >= v:
                    possible.append(largest)
                    break
        if possible:
            answers.append(str(min(possible)))
        else:
            answers.append("-1")
    print("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
