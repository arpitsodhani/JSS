# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    xs = list(map(int, data[1][:n]))
    bs = list(map(int, data[2][:n]))
    result = int(data[4]) if len(data) >= 5 else 0
    chosen = [(x if b else x ^ 1) for x, b in zip(xs, bs)]
    for value in chosen:
        result ^= value
    print(result)


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


