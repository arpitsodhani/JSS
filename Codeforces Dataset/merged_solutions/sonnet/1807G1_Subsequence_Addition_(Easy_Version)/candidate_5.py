import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: can_build :: (c: list[int]) -> bool ---
def can_build(c):
    sorted_items = sorted(c)
    if sorted_items[0] != 1:
        return False
    reached = 1
    for i in range(1, len(sorted_items)):
        if sorted_items[i] > reached:
            return False
        reached += sorted_items[i]
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for c in read_input():
        out.append("YES" if can_build(c) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
