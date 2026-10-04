import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    q = int(data[pos])
    pos += 1
    cases = []
    for _ in range(q):
        n = int(data[pos])
        k = int(data[pos + 1])
        pos += 2
        values = list(map(int, data[pos:pos + n]))
        pos += n
        cases.append((n, k, values))
    return cases


# --- clause: split_points :: (n: int, k: int, values: list[int]) -> list[int] ---
def split_points(n, k, values):
    spots = []
    for i in range(n):
        if values[i] % 2:
            spots.append(i + 1)
    if len(spots) < k:
        return None
    if (len(spots) - k) & 1:
        return None
    cuts = spots[:k - 1]
    cuts.append(n)
    return cuts


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k, values in read_input():
        cuts = split_points(n, k, values)
        if cuts is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(" ".join(map(str, cuts)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
