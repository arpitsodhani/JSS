import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        cases.append(raw[offset:offset + n])
        offset += n
    return cases


# --- clause: can_arrange :: (a: list[int]) -> bool ---
def can_arrange(a):
    tally = {}
    for number in a:
        tally[number] = tally.get(number, 0) + 1
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
