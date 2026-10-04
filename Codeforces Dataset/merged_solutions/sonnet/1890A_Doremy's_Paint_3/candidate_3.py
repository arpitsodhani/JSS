import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: can_arrange :: (a: list[int]) -> bool ---
def can_arrange(a):
    tally = {}
    for element in a:
        tally[element] = tally.get(element, 0) + 1
    if len(tally) > 2:
        return False
    counts = sorted(tally.values())
    if len(counts) == 1:
        return True
    return counts[1] - counts[0] <= 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("Yes" if can_arrange(a) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
