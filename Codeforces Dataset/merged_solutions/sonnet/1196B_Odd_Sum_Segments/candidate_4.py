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
        values = [int(data[pos + i]) for i in range(n)]
        pos += n
        cases.append((n, k, values))
    return cases


# --- clause: split_points :: (n: int, k: int, values: list[int]) -> list[int] ---
def split_points(n, k, values):
    spots = [i + 1 for i in range(n) if values[i] % 2]
    if len(spots) < k or (len(spots) - k) % 2:
        return None
    cuts = spots[:k - 1]
    cuts.append(n)
    return cuts


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        cuts = split_points(case[0], case[1], case[2])
        if cuts is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(" ".join(map(str, cuts)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
