import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        k = raw[offset]
        n = raw[offset + 1]
        m = raw[offset + 2]
        offset += 3
        a = raw[offset:offset + n]
        offset += n
        b = raw[offset:offset + m]
        offset += m
        cases.append((k, a, b))
    return cases


# --- clause: weave :: (k: int, a: list[int], b: list[int]) -> list[int] | None ---
def weave(k, a, b):
    lines = k
    i = 0
    j = 0
    collected = []
    while i < len(a) or j < len(b):
        if i < len(a) and a[i] <= lines:
            if a[i] == 0:
                lines += 1
            collected.append(a[i])
            i += 1
        elif j < len(b) and b[j] <= lines:
            if b[j] == 0:
                lines += 1
            collected.append(b[j])
            j += 1
        else:
            return None
    return collected


# --- clause: main :: () -> None ---
def main():
    collected = []
    for k, a, b in read_input():
        woven = weave(k, a, b)
        collected.append("-1" if woven is None else " ".join(map(str, woven)))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
