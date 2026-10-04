import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = [int(data[i + 1]) for i in range(n)]
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
            left = spots[i] - spots[i - 1]
            right = spots[i + 1] - spots[i]
            near = left if left < right else right
        far = max(spots[n - 1] - spots[i], spots[i] - spots[0])
        out.append("%d %d" % (near, far))
    return out


# --- clause: main :: () -> None ---
def main():
    n, spots = read_input()
    rows = postage(n, spots)
    sys.stdout.write("\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
