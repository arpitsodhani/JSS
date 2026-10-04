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
    limit = max(max(correct), 2 * min(correct))
    if limit >= min(wrong):
        return -1
    return limit

# --- clause: main :: () -> None ---
def main():
    correct, wrong = read_input()
    sys.stdout.write(str(best_limit(correct, wrong)) + "\n")


if __name__ == "__main__":
    main()
