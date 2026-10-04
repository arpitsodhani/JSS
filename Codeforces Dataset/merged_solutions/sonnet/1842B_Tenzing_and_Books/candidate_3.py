import sys


# --- clause: read_input :: () -> list[tuple[int, list[list[int]]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        x = fields[cursor + 1]
        cursor += 2
        stacks = []
        for _ in range(3):
            stacks.append(fields[cursor:cursor + n])
            cursor += n
        cases.append((x, stacks))
    return cases


# --- clause: usable_prefix :: (x: int, books: list[int]) -> int ---
def usable_prefix(x, books):
    gained = 0
    for element in books:
        if element | x != x:
            break
        gained |= element
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
