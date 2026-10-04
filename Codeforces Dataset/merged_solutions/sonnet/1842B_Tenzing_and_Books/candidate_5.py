import sys


# --- clause: read_input :: () -> list[tuple[int, list[list[int]]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        x = raw[offset + 1]
        offset += 2
        stacks = []
        for _ in range(3):
            stacks.append(raw[offset:offset + n])
            offset += n
        cases.append((x, stacks))
    return cases


# --- clause: usable_prefix :: (x: int, books: list[int]) -> int ---
def usable_prefix(x, books):
    gained = 0
    for number in books:
        if number | x != x:
            break
        gained |= number
    return gained


# --- clause: can_reach :: (x: int, stacks: list[list[int]]) -> bool ---
def can_reach(x, stacks):
    gained = 0
    for books in stacks:
        gained |= usable_prefix(x, books)
    return gained == x


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, stacks in read_input():
        out.append("Yes" if can_reach(x, stacks) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
