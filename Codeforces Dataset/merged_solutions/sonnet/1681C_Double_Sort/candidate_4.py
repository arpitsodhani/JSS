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
        first = [int(token) for token in data[pos:pos + n]]
        pos += n
        second = [int(data[pos + i]) for i in range(n)]
        pos += n
        cases.append((n, first, second))
    return cases


# --- clause: sort_pairs :: (n: int, first: list[int], second: list[int]) -> list[str] ---
def sort_pairs(n, first, second):
    moves = []
    a = first[:]
    b = second[:]
    for i in range(n):
        pick = i
        for j in range(i + 1, n):
            if (a[j], b[j]) < (a[pick], b[pick]):
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
    for case in read_input():
        moves = sort_pairs(case[0], case[1], case[2])
        if moves is None:
            out.append("-1")
        else:
            out.append(str(len(moves)))
            out.extend(moves)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
