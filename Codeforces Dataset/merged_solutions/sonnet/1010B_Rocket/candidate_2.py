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
        result = ask(1)
        if result == 0:
            return None
        honest.append(1 if result == 1 else 0)
    return honest


# --- clause: hunt :: (m: int, honest: list[int]) -> None ---
def hunt(m, honest):
    n = len(honest)
    stride = n
    low = 2
    high = m
    while low <= high:
        mid = (low + high) // 2
        result = ask(mid)
        if result == 0:
            return
        truth = result if honest[stride % n] else -result
        stride += 1
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
