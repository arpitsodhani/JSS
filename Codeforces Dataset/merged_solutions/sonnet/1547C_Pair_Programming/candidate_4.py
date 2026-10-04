import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        k = numbers[reader]
        n = numbers[reader + 1]
        m = numbers[reader + 2]
        reader += 3
        a = numbers[reader:reader + n]
        reader += n
        b = numbers[reader:reader + m]
        reader += m
        cases.append((k, a, b))
    return cases


# --- clause: weave :: (k: int, a: list[int], b: list[int]) -> list[int] | None ---
def weave(k, a, b):
    lines = k
    left = list(reversed(a))
    right = list(reversed(b))
    out = []
    while left or right:
        moved = False
        for pile in (left, right):
            if pile and pile[-1] <= lines:
                value = pile.pop()
                if value == 0:
                    lines += 1
                out.append(value)
                moved = True
                break
        if not moved:
            return None
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a, b in read_input():
        woven = weave(k, a, b)
        out.append("-1" if woven is None else " ".join(map(str, woven)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
