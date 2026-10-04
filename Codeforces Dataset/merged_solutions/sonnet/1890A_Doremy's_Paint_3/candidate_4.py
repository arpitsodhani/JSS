import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: can_arrange :: (a: list[int]) -> bool ---
def can_arrange(a):
    kinds = sorted(set(a))
    if len(kinds) > 2:
        return False
    if len(kinds) == 1:
        return True
    first = 0
    for value in a:
        if value == kinds[0]:
            first += 1
    second = len(a) - first
    gap = first - second
    if gap < 0:
        gap = -gap
    return gap <= 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("Yes" if can_arrange(a) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
