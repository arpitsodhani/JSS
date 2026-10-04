import sys


# --- clause: read_input :: () -> list[tuple[str, list[int], str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    offset = 1
    cases = []
    for _ in range(t):
        m = int(fields[offset + 1])
        s = fields[offset + 2].decode()
        offset += 3
        ind = [int(fields[offset + i]) for i in range(m)]
        offset += m
        c = fields[offset].decode()
        offset += 1
        cases.append((s, ind, c))
    return cases


# --- clause: smallest_string :: (s: str, ind: list[int], c: str) -> str ---
def smallest_string(s, ind, c):
    spots = sorted(set(ind))
    letters = sorted(c)
    pieces = list(s)
    for i in range(len(spots)):
        pieces[spots[i] - 1] = letters[i]
    return "".join(pieces)


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for s, ind, c in read_input():
        pieces.append(smallest_string(s, ind, c))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
