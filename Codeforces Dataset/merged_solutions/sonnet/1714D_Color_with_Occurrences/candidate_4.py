import sys


# --- clause: read_input :: () -> list[tuple[str, list[str]]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    q = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(q):
        text = numbers[cursor].decode()
        n = int(numbers[cursor + 1])
        cursor += 2
        pieces = [numbers[cursor + i].decode() for i in range(n)]
        cursor += n
        cases.append((text, pieces))
    return cases


# --- clause: best_reach :: (text: str, pieces: list[str]) -> list[tuple[int, int]] ---
def best_reach(text, pieces):
    n = len(text)
    reach = [(-1, -1)] * n
    index = 0
    while index < len(pieces):
        piece = pieces[index]
        spot = text.find(piece)
        while spot >= 0:
            stop = spot + len(piece)
            if stop > reach[spot][0]:
                reach[spot] = (stop, index + 1)
            spot = text.find(piece, spot + 1)
        index += 1
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
            for index, spot in steps:
                out.append("%d %d" % (index, spot))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
