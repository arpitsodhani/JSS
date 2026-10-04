import sys


# --- clause: read_input :: () -> list[tuple[str, list[int], str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(t):
        m = int(numbers[cursor + 1])
        s = numbers[cursor + 2].decode()
        cursor += 3
        ind = [int(numbers[cursor + i]) for i in range(m)]
        cursor += m
        c = numbers[cursor].decode()
        cursor += 1
        cases.append((s, ind, c))
    return cases


# --- clause: smallest_string :: (s: str, ind: list[int], c: str) -> str ---
def smallest_string(s, ind, c):
    seen = {}
    for spot in ind:
        seen[spot] = 1
    spots = list(seen)
    spots.sort()
    letters = list(c)
    letters.sort()
    out = list(s)
    at = 0
    while at < len(spots):
        out[spots[at] - 1] = letters[at]
        at += 1
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, ind, c in read_input():
        out.append(smallest_string(s, ind, c))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
