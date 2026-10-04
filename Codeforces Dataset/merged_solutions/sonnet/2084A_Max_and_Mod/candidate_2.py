import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    tests = values[0]
    cases = []
    for i in range(1, tests + 1):
        cases.append(values[i])
    return cases


# --- clause: solve_case :: (n: int) -> str ---
def solve_case(n):
    if n % 2 == 0:
        return "-1"
    perm = [n]
    for v in range(1, n):
        perm.append(v)
    return " ".join(map(str, perm))


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    answers = []
    for n in cases:
        answers.append(solve_case(n))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
