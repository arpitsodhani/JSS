import sys


# --- clause: read_input :: () -> list[tuple[list[int], int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        centers = [int(data[pos + i]) for i in range(2 * n)]
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
    dx = xt - xs
    dy = yt - ys
    travel = dx * dx + dy * dy
    for i in range(0, len(centers), 2):
        cx = centers[i] - xt
        cy = centers[i + 1] - yt
        if cx * cx + cy * cy <= travel:
            return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(reachable(case[0], case[1], case[2], case[3], case[4]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
