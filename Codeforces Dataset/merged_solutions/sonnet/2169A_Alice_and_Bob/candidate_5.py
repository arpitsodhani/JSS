import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        a = int(data[pos])
        pos += 1
        marbles = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((a, marbles))
    return cases


# --- clause: pick_number :: (a: int, marbles: list[int]) -> int ---
def pick_number(a, marbles):
    above = 0
    below = 0
    index = 0
    total = len(marbles)
    while index < total:
        value = marbles[index]
        if value != a:
            if value > a:
                above += 1
            else:
                below += 1
        index += 1
    if above >= below:
        return a + 1
    return a - 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, marbles in read_input():
        out.append(str(pick_number(a, marbles)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
