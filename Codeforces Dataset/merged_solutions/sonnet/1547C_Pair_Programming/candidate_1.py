import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        k = data[pos]
        n = data[pos + 1]
        m = data[pos + 2]
        pos += 3
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + m]
        pos += m
        cases.append((k, a, b))
    return cases


# --- clause: weave :: (k: int, a: list[int], b: list[int]) -> list[int] | None ---
def weave(k, a, b):
    lines = k
    i = 0
    j = 0
    out = []
    while i < len(a) or j < len(b):
        if i < len(a) and a[i] <= lines:
            if a[i] == 0:
                lines += 1
            out.append(a[i])
            i += 1
        elif j < len(b) and b[j] <= lines:
            if b[j] == 0:
                lines += 1
            out.append(b[j])
            j += 1
        else:
            return None
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a, b in read_input():
        woven = weave(k, a, b)
        out.append("-1" if woven is None else " ".join(map(str, woven)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
