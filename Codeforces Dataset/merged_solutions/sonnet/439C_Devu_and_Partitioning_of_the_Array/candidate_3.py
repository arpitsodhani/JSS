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
    odds = [v for v in a if v % 2 == 1]
    evens = [v for v in a if v % 2 == 0]
    odd_parts = k - p
    if len(odds) < odd_parts:
        return None
    leftover_odds = len(odds) - odd_parts
    if leftover_odds % 2 == 1:
        return None
    from_pairs = p - len(evens)
    if from_pairs > leftover_odds // 2:
        return None
    if from_pairs < 0:
        from_pairs = 0
    parts = []
    for i in range(odd_parts):
        parts.append([odds[i]])
    cut = odd_parts
    for i in range(from_pairs):
        parts.append([odds[cut + 2 * i], odds[cut + 2 * i + 1]])
    cut += 2 * from_pairs
    used_evens = p - from_pairs
    for i in range(used_evens):
        parts.append([evens[i]])
    rest = evens[used_evens:] + odds[cut:]
    if rest:
        parts[-1].extend(rest)
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
