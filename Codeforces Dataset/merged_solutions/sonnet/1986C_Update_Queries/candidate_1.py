import sys


# --- clause: read_input :: () -> list[tuple[str, list[int], str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        m = int(data[pos + 1])
        s = data[pos + 2].decode()
        pos += 3
        ind = [int(data[pos + i]) for i in range(m)]
        pos += m
        c = data[pos].decode()
        pos += 1
        cases.append((s, ind, c))
    return cases


# --- clause: smallest_string :: (s: str, ind: list[int], c: str) -> str ---
def smallest_string(s, ind, c):
    spots = sorted(set(ind))
    letters = sorted(c)
    out = list(s)
    for i in range(len(spots)):
        out[spots[i] - 1] = letters[i]
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, ind, c in read_input():
        out.append(smallest_string(s, ind, c))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
