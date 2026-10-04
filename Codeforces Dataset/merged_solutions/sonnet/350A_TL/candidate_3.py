import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    correct = data[2:2 + n]
    wrong = data[2 + n:2 + n + m]
    return correct, wrong

# --- clause: best_limit :: (correct: list[int], wrong: list[int]) -> int ---
def best_limit(correct, wrong):
    slowest = max(correct)
    fastest = min(correct)
    limit = slowest if slowest > 2 * fastest else 2 * fastest
    return limit if min(wrong) > limit else -1

# --- clause: main :: () -> None ---
def main():
    correct, wrong = read_input()
    sys.stdout.write(str(best_limit(correct, wrong)) + "\n")


if __name__ == "__main__":
    main()
