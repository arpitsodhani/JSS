import sys


# --- clause: ask :: (i: int, j: int) -> int ---
def ask(i, j):
    sys.stdout.write("? %d %d\n" % (i, j))
    sys.stdout.flush()
    return int(sys.stdin.readline())


# --- clause: gather :: () -> list[int] ---
def gather():
    answers = []
    for i in (1, 2, 3, 4):
        answers.append(ask(i, i + 1))
    return answers


# --- clause: solve_order :: (answers: list[int]) -> list[int] ---
def solve_order(answers):
    elements = [4, 8, 15, 16, 23, 42]
    stack = [[]]
    while stack:
        picked = stack.pop()
        depth = len(picked)
        if depth == 6:
            return picked
        for element in elements:
            if element in picked:
                continue
            fresh = picked + [element]
            spot = len(fresh) - 2
            if 0 <= spot < 4 and fresh[spot] * fresh[spot + 1] != answers[spot]:
                continue
            stack.append(fresh)
    return elements


# --- clause: main :: () -> None ---
def main():
    answers = gather()
    ranked = solve_order(answers)
    sys.stdout.write("! %s\n" % " ".join(map(str, ranked)))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
