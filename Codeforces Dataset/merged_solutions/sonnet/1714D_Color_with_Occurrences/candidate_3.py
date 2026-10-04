import sys


# --- clause: read_input :: () -> list[tuple[str, list[str]]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    q = int(fields[0])
    offset = 1
    cases = []
    for _ in range(q):
        text = fields[offset].decode()
        n = int(fields[offset + 1])
        offset += 2
        pieces = [fields[offset + i].decode() for i in range(n)]
        offset += n
        cases.append((text, pieces))
    return cases


# --- clause: best_reach :: (text: str, pieces: list[str]) -> list[tuple[int, int]] ---
def best_reach(text, pieces):
    n = len(text)
    reach = [(-1, -1)] * n
    for spot in range(n):
        for place in range(len(pieces)):
            piece = pieces[place]
            if text.startswith(piece, spot):
                stop = spot + len(piece)
                if stop > reach[spot][0]:
                    reach[spot] = (stop, place + 1)
    return reach


# --- clause: cover_text :: (text: str, reach: list[tuple[int, int]]) -> list[tuple[int, int]] | None ---
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
            stop, place = reach[spot]
            if stop > best:
                best = stop
                pick = place
                start = spot
        if pick < 0:
            return None
        steps.append((pick, start + 1))
        covered = best
    return steps


# --- clause: main :: () -> None ---
def main():
    out = []
    for text, pieces in read_input():
        reach = best_reach(text, pieces)
        steps = cover_text(text, reach)
        if steps is None:
            out.append("-1")
        else:
            out.append(str(len(steps)))
            for place, spot in steps:
                out.append("%d %d" % (place, spot))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
