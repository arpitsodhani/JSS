# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    input_line = sys.stdin.buffer.readline

    n_line = input_line()
    while n_line.strip() == b"":
        n_line = input_line()
    n = int(n_line)

    volumes = list(map(int, input_line().split()))
    best_time = 0
    total = 0

    for index, current in enumerate(accumulate(volumes), 1):
        total = current
        needed = (current + index - 1) // index
        if needed > best_time:
            best_time = needed

    q = int(input_line())
    result = []

    for _ in range(q):
        t = int(input_line())
        if t >= best_time:
            result.append(str((total + t - 1) // t))
        else:
            result.append("-1")

    sys.stdout.write("\n".join(result))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


