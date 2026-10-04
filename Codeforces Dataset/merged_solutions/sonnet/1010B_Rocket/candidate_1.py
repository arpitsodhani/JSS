import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    parts = sys.stdin.readline().split()
    return int(parts[0]), int(parts[1])


# --- clause: ask :: (y: int) -> int ---
def ask(y):
    sys.stdout.write("%d\n" % y)
    sys.stdout.flush()
    return int(sys.stdin.readline())


# --- clause: learn_pattern :: (n: int) -> list[int] | None ---
def learn_pattern(n):
    honest = []
    for _ in range(n):
        answer = ask(1)
        if answer == 0:
            return None
        honest.append(1 if answer == 1 else 0)
    return honest


# --- clause: hunt :: (m: int, honest: list[int]) -> None ---
def hunt(m, honest):
    n = len(honest)
    step = n
    low = 2
    high = m
    while low <= high:
        mid = (low + high) // 2
        answer = ask(mid)
        if answer == 0:
            return
        truth = answer if honest[step % n] else -answer
        step += 1
        if truth == 1:
            low = mid + 1
        else:
            high = mid - 1


# --- clause: main :: () -> None ---
def main():
    m, n = read_input()
    honest = learn_pattern(n)
    if honest is not None:
        hunt(m, honest)


if __name__ == "__main__":
    main()
