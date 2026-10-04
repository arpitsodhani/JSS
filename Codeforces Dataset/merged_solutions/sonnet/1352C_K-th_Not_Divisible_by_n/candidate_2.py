import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    nums = list(map(int, data[1:1 + 2 * t]))
    return list(zip(nums[0::2], nums[1::2]))


# --- clause: kth_free :: (n: int, k: int) -> int ---
def kth_free(n, k):
    full = (k - 1) // (n - 1)
    return k + full


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(str(kth_free(n, k)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
