import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    total = int(data[0])
    cases = []
    for case in range(total):
        cases.append((int(data[2 * case + 1]), int(data[2 * case + 2])))
    return cases


# --- clause: solve_case :: (h: int, p: int) -> int ---
def solve_case(h, p):
    level = 0
    while level < h and (1 << level) <= p:
        level += 1
    total = 1 << h
    left = total - (1 << level)
    return level + (left + p - 1) // p


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, p in read_input():
        out.append(str(solve_case(h, p)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
