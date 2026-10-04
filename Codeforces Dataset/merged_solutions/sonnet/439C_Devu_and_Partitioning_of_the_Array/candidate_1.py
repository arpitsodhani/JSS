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
    spare_pairs = (len(odds) - odd_parts) // 2
    if len(evens) + spare_pairs < p:
        return None
    parts = []
    taken_odd = 0
    for _ in range(odd_parts):
        parts.append([odds[taken_odd]])
        taken_odd += 1
    taken_even = 0
    for _ in range(p):
        if taken_even < len(evens):
            parts.append([evens[taken_even]])
            taken_even += 1
        else:
            parts.append([odds[taken_odd], odds[taken_odd + 1]])
            taken_odd += 2
    leftover = evens[taken_even:] + odds[taken_odd:]
    if leftover:
        parts[-1].extend(leftover)
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
