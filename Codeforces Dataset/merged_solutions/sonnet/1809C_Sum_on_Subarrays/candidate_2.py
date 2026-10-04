import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    nums = list(map(int, data[1:1 + 2 * t]))
    return list(zip(nums[0::2], nums[1::2]))


# --- clause: build_array :: (n: int, k: int) -> list[int] ---
def build_array(n, k):
    head = 0
    while (head + 1) * (head + 2) <= 2 * k:
        head = head + 1
    values = [2] * head
    left = k - head * (head + 1) // 2
    if head < n:
        values.append(-2 * (head - left) - 1)
    while len(values) < n:
        values.append(-1000)
    return values


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(" ".join(map(str, build_array(n, k))))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
