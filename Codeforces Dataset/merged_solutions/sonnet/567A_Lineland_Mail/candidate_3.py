import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = [int(token) for token in data[1:n + 1]]
    return n, spots


# --- clause: postage :: (n: int, spots: list[int]) -> list[str] ---
def postage(n, spots):
    huge = 1 << 62
    padded = [-huge] + spots + [huge]
    out = []
    for i in range(1, n + 1):
        left = padded[i] - padded[i - 1]
        right = padded[i + 1] - padded[i]
        near = left if left < right else right
        far = spots[n - 1] - padded[i]
        other = padded[i] - spots[0]
        if other > far:
            far = other
        out.append("%d %d" % (near, far))
    return out


# --- clause: main :: () -> None ---
def main():
    n, spots = read_input()
    print("\n".join(postage(n, spots)))


if __name__ == "__main__":
    main()
