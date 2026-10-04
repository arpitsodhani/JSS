import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    pos = 1
    cases = []
    for _ in range(q):
        text = data[pos].decode()
        n = int(data[pos + 1])
        pos += 2
        pieces = [data[pos + i].decode() for i in range(n)]
        pos += n
        cases.append((text, pieces))
    return cases

# Clause best_reach [Confidence: 1.00]
def best_reach(text, pieces):
    n = len(text)
    reach = [(-1, -1)] * n
    for spot in range(n):
        for index in range(len(pieces)):
            piece = pieces[index]
            if text.startswith(piece, spot):
                stop = spot + len(piece)
                if stop > reach[spot][0]:
                    reach[spot] = (stop, index + 1)
    return reach

# Clause cover_text [Confidence: 1.00]
def cover_text(text, reach):
    n = len(text)
    covered = 0
    steps = []
    while covered < n:
        best = covered
        pick = -1
        start = -1
        for spot in range(covered + 1):
            if spot >= n:
                break
            stop, index = reach[spot]
            if stop > best:
                best = stop
                pick = index
                start = spot
        if pick < 0:
            return None
        steps.append((pick, start + 1))
        covered = best
    return steps

# Clause main [Confidence: 1.00]
def main():
    out = []
    for text, pieces in read_input():
        reach = best_reach(text, pieces)
        steps = cover_text(text, reach)
        if steps is None:
            out.append("-1")
        else:
            out.append(str(len(steps)))
            for index, spot in steps:
                out.append("%d %d" % (index, spot))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

