# Clause setup_environment [Confidence: 0.40]
import sys

def receive_after_output(prefix, values):
    line = prefix + " " + " ".join(map(str, values))
    print(line, flush=True)
    result = int(sys.stdin.readline())
    if result < 0:
        raise SystemExit
    return result


# Clause solve_logic [Confidence: 0.20]
def main():
    lower = (1 << 7) - 1
    upper = lower << 7
    first = query(range(1, 101))
    second = query((i << 7 for i in range(1, 101)))
    answer = (first & upper) | (second & lower)


# Clause finish_program [Confidence: 0.20]
print("! {}".format(solve()), flush=True)


