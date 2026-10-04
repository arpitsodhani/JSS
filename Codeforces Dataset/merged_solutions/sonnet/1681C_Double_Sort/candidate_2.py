import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        first = list(map(int, data[pos:pos + n]))
        pos += n
        second = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, first, second))
    return cases


# --- clause: sort_pairs :: (n: int, first: list[int], second: list[int]) -> list[str] ---
def sort_pairs(n, first, second):
    a = list(first)
    b = list(second)
    moves = []
    for i in range(n):
        pick = i
        for j in range(i + 1, n):
            if a[j] < a[pick] or (a[j] == a[pick] and b[j] < b[pick]):
                pick = j
        if pick != i:
            a[i], a[pick] = a[pick], a[i]
            b[i], b[pick] = b[pick], b[i]
            moves.append("%d %d" % (i + 1, pick + 1))
    for i in range(n - 1):
        if b[i] > b[i + 1]:
            return None
    return moves


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, first, second in read_input():
        moves = sort_pairs(n, first, second)
        if moves is None:
            out.append("-1")
        else:
            out.append(str(len(moves)))
            out.extend(moves)
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
