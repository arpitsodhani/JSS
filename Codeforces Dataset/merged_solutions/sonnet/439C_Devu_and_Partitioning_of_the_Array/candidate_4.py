import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    p = data[2]
    return n, k, p, data[3:3 + n]

# --- clause: partition :: (n: int, k: int, p: int, a: list[int]) -> list[list[int]] | None ---
def partition(n, k, p, a):
    odds = [v for v in a if v % 2]
    evens = [v for v in a if v % 2 == 0]
    odd_parts = k - p
    if len(odds) < odd_parts or (len(odds) - odd_parts) % 2:
        return None
    pairs = (len(odds) - odd_parts) // 2
    if len(evens) + pairs < p:
        return None
    parts = []
    next_odd = 0
    while len(parts) < odd_parts:
        parts.append([odds[next_odd]])
        next_odd += 1
    next_even = 0
    while len(parts) < k:
        if next_even < len(evens):
            parts.append([evens[next_even]])
            next_even += 1
        else:
            parts.append([odds[next_odd], odds[next_odd + 1]])
            next_odd += 2
    tail = evens[next_even:] + odds[next_odd:]
    if tail:
        parts[-1].extend(tail)
    return parts

# --- clause: main :: () -> None ---
def main():
    n, k, p, a = read_input()
    parts = partition(n, k, p, a)
    if parts is None:
        sys.stdout.write("NO\n")
        return
    out = ["YES"]
    for part in parts:
        out.append(str(len(part)) + " " + " ".join(map(str, part)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
