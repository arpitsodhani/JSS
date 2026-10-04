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
        reply = ask(1)
        if reply == 0:
            return None
        honest.append(1 if reply == 1 else 0)
    return honest


# --- clause: hunt :: (m: int, honest: list[int]) -> None ---
def hunt(m, honest):
    n = len(honest)
    delta = n
    small = 2
    high = m
    while small <= high:
        mid = (small + high) // 2
        reply = ask(mid)
        if reply == 0:
            return
        truth = reply if honest[delta % n] else -reply
        delta += 1
        if truth == 1:
            small = mid + 1
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
