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
    for limit in range(1, 201):
        if any(a > limit for a in correct):
            continue
        if not any(2 * a <= limit for a in correct):
            continue
        if any(b <= limit for b in wrong):
            continue
        return limit
    return -1

# --- clause: main :: () -> None ---
def main():
    correct, wrong = read_input()
    sys.stdout.write(str(best_limit(correct, wrong)) + "\n")


if __name__ == "__main__":
    main()
