import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[i]), int(data[i + 1])) for i in range(1, 2 * t + 1, 2)]


# --- clause: kth_free :: (n: int, k: int) -> int ---
def kth_free(n, k):
    return k + (k - 1) // (n - 1)


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(kth_free(case[0], case[1])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
