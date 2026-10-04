import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        k = fields[cursor]
        n = fields[cursor + 1]
        m = fields[cursor + 2]
        cursor += 3
        a = fields[cursor:cursor + n]
        cursor += n
        b = fields[cursor:cursor + m]
        cursor += m
        cases.append((k, a, b))
    return cases


# --- clause: weave :: (k: int, a: list[int], b: list[int]) -> list[int] | None ---
def weave(k, a, b):
    lines = k
    i = 0
    j = 0
    written = []
    while i < len(a) or j < len(b):
        if i < len(a) and a[i] <= lines:
            if a[i] == 0:
                lines += 1
            written.append(a[i])
            i += 1
        elif j < len(b) and b[j] <= lines:
            if b[j] == 0:
                lines += 1
            written.append(b[j])
            j += 1
        else:
            return None
    return written


# --- clause: main :: () -> None ---
def main():
    written = []
    for k, a, b in read_input():
        woven = weave(k, a, b)
        written.append("-1" if woven is None else " ".join(map(str, woven)))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
