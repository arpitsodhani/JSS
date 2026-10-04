import sys


# --- clause: read_input :: () -> list[tuple[list[int], int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        centers = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        xs, ys = int(data[idx]), int(data[idx + 1])
        xt, yt = int(data[idx + 2]), int(data[idx + 3])
        idx += 4
        cases.append((centers, xs, ys, xt, yt))
    return cases


# --- clause: reachable :: (centers: list[int], xs: int, ys: int, xt: int, yt: int) -> str ---
def reachable(centers, xs, ys, xt, yt):
    dx = xs - xt
    dy = ys - yt
    travel = dx * dx + dy * dy
    for i in range(0, len(centers), 2):
        cx = centers[i] - xt
        cy = centers[i + 1] - yt
        if travel >= cx * cx + cy * cy:
            return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for centers, xs, ys, xt, yt in read_input():
        out.append(reachable(centers, xs, ys, xt, yt))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
