import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = list(map(int, data[1:n + 1]))
    return n, spots


# --- clause: postage :: (n: int, spots: list[int]) -> list[str] ---
def postage(n, spots):
    out = []
    for i in range(n):
        if i == 0:
            near = spots[1] - spots[0]
        elif i == n - 1:
            near = spots[n - 1] - spots[n - 2]
        else:
            near = min(spots[i] - spots[i - 1], spots[i + 1] - spots[i])
        far = spots[n - 1] - spots[i]
        other = spots[i] - spots[0]
        if other > far:
            far = other
        out.append("%d %d" % (near, far))
    return out


# --- clause: main :: () -> None ---
def main():
    n, spots = read_input()
    sys.stdout.write("%s\n" % "\n".join(postage(n, spots)))


if __name__ == "__main__":
    main()
