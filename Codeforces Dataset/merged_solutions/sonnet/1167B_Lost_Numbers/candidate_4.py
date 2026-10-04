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
    values = [4, 8, 15, 16, 23, 42]
    for first in values:
        chain = [first]
        ok = True
        for step in range(4):
            nxt = 0
            for value in values:
                if value in chain:
                    continue
                if chain[-1] * value == answers[step]:
                    nxt = value
                    break
            if nxt == 0:
                ok = False
                break
            chain.append(nxt)
        if not ok:
            continue
        for value in values:
            if value not in chain:
                chain.append(value)
        if len(chain) == 6:
            return chain
    return values


# --- clause: main :: () -> None ---
def main():
    answers = gather()
    order = solve_order(answers)
    sys.stdout.write("! %s\n" % " ".join(map(str, order)))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
