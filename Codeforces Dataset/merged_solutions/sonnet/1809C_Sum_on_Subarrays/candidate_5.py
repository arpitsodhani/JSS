import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return cases


# --- clause: build_array :: (n: int, k: int) -> list[int] ---
def build_array(n, k):
    head = 0
    made = 0
    while head < n and k >= made + head + 1:
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
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
