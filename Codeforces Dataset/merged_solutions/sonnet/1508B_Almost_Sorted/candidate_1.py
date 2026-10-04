import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(t)]


# --- clause: block_choices :: (n: int, k: int) -> list[int] ---
def block_choices(n, k):
    if n <= 62 and k > (1 << (n - 1)):
        return None
    out = []
    i = 1
    left = k
    while i <= n:
        length = 1
        while True:
            end = i + length - 1
            if end >= n:
                count = 1
            else:
                shift = n - end - 1
                count = (1 << shift) if shift < 62 else (1 << 62)
            if left > count:
                left -= count
                length += 1
            else:
                break
        for value in range(i + length - 1, i - 1, -1):
            out.append(value)
        i += length
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        picked = block_choices(n, k)
        if picked is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, picked)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
