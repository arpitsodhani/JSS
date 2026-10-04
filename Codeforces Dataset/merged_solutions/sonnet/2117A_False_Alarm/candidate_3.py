import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        x = fields[offset + 1]
        offset += 2
        cases.append((x, fields[offset:offset + n]))
        offset += n
    return cases


# --- clause: can_pass :: (x: int, doors: list[int]) -> bool ---
def can_pass(x, doors):
    shut = []
    for i in range(len(doors)):
        if doors[i] == 1:
            shut.append(i)
    if not shut:
        return True
    return shut[-1] - shut[0] + 1 <= x


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for x, doors in read_input():
        pieces.append("YES" if can_pass(x, doors) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
