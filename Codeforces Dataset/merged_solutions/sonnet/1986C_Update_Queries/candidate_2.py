import sys


# --- clause: read_input :: () -> list[tuple[str, list[int], str]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    at = 1
    cases = []
    for _ in range(t):
        m = int(tokens[at + 1])
        s = tokens[at + 2].decode()
        at += 3
        ind = [int(tokens[at + i]) for i in range(m)]
        at += m
        c = tokens[at].decode()
        at += 1
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
