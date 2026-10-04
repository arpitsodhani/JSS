import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        a = int(data[pos + 1])
        pos += 2
        marbles = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((a, marbles))
    return cases


# --- clause: pick_number :: (a: int, marbles: list[int]) -> int ---
def pick_number(a, marbles):
    above = sum(1 for value in marbles if value > a)
    below = sum(1 for value in marbles if value < a)
    if above >= below:
        return a + 1
    return a - 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, marbles in read_input():
        out.append(str(pick_number(a, marbles)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
