import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    nums = list(map(int, data[1:1 + 3 * q]))
    return list(zip(nums[0::3], nums[1::3], nums[2::3]))


# --- clause: closest_total :: (a: int, b: int, c: int) -> int ---
def closest_total(a, b, c):
    spread = max(a, b, c) - min(a, b, c) - 2
    return 2 * spread if spread > 0 else 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, c in read_input():
        out.append(str(closest_total(a, b, c)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
