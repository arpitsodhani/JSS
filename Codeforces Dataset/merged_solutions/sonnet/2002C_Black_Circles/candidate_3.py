import sys


# --- clause: read_input :: () -> list[tuple[list[int], int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        pos += 1
        centers = [int(token) for token in data[pos:pos + 2 * n]]
        pos += 2 * n
        xs = int(data[pos])
        ys = int(data[pos + 1])
        xt = int(data[pos + 2])
        yt = int(data[pos + 3])
        pos += 4
        cases.append((centers, xs, ys, xt, yt))
    return cases


# --- clause: reachable :: (centers: list[int], xs: int, ys: int, xt: int, yt: int) -> str ---
def reachable(centers, xs, ys, xt, yt):
    dx = xs - xt
    dy = ys - yt
    travel = dx * dx + dy * dy
    i = 0
    total = len(centers)
    while i < total:
        cx = centers[i] - xt
        cy = centers[i + 1] - yt
        if cx * cx + cy * cy <= travel:
            return "NO"
        i += 2
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for centers, xs, ys, xt, yt in read_input():
        out.append(reachable(centers, xs, ys, xt, yt))
    print("\n".join(out))


if __name__ == "__main__":
    main()
