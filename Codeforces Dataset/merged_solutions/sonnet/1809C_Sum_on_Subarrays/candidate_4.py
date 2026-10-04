import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[i]), int(data[i + 1])) for i in range(1, 2 * t + 1, 2)]


# --- clause: build_array :: (n: int, k: int) -> list[int] ---
def build_array(n, k):
    head = 0
    while (head + 1) * (head + 2) // 2 <= k:
        head += 1
    values = [2] * head
    left = k - head * (head + 1) // 2
    if head < n:
        values.append(-2 * (head - left) - 1)
    padding = n - len(values)
    values.extend([-1000] * padding)
    return values


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(" ".join(map(str, build_array(case[0], case[1]))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
