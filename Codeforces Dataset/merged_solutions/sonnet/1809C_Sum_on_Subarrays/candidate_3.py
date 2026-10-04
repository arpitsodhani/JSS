import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(t)]


# --- clause: build_array :: (n: int, k: int) -> list[int] ---
def build_array(n, k):
    head = 0
    made = 0
    while head < n and made + head + 1 <= k:
        head += 1
        made += head
    values = [2] * head
    if head < n:
        values.append(2 * (k - made) - 2 * head - 1)
    while len(values) < n:
        values.append(-1000)
    return values


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(" ".join(map(str, build_array(n, k))))
    print("\n".join(out))


if __name__ == "__main__":
    main()
