import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        k = tokens[pos]
        n = tokens[pos + 1]
        m = tokens[pos + 2]
        pos += 3
        a = tokens[pos:pos + n]
        pos += n
        b = tokens[pos:pos + m]
        pos += m
        cases.append((k, a, b))
    return cases


# --- clause: weave :: (k: int, a: list[int], b: list[int]) -> list[int] | None ---
def weave(k, a, b):
    lines = k
    i = 0
    j = 0
    pieces = []
    while i < len(a) or j < len(b):
        if i < len(a) and a[i] <= lines:
            if a[i] == 0:
                lines += 1
            pieces.append(a[i])
            i += 1
        elif j < len(b) and b[j] <= lines:
            if b[j] == 0:
                lines += 1
            pieces.append(b[j])
            j += 1
        else:
            return None
    return pieces


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for k, a, b in read_input():
        woven = weave(k, a, b)
        pieces.append("-1" if woven is None else " ".join(map(str, woven)))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
