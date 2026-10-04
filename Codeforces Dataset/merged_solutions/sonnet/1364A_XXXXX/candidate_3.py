import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        x = fields[offset + 1]
        offset += 2
        cases.append((x, fields[offset:offset + n]))
        offset += n
    return cases


# --- clause: longest_piece :: (x: int, a: list[int]) -> int ---
def longest_piece(x, a):
    n = len(a)
    if sum(a) % x:
        return n
    lead = -1
    last = -1
    for i in range(n):
        if a[i] % x:
            if lead < 0:
                lead = i
            last = i
    if lead < 0:
        return -1
    tail = n - lead - 1
    return tail if tail > last else last


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, a in read_input():
        out.append(longest_piece(x, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
