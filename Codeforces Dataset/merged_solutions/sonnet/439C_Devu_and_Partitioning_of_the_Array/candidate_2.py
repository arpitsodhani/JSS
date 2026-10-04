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
    odds = []
    evens = []
    for value in a:
        if value & 1:
            odds.append(value)
        else:
            evens.append(value)
    odd_parts = k - p
    spare = len(odds) - odd_parts
    if spare < 0 or spare % 2:
        return None
    if len(evens) + spare // 2 < p:
        return None
    odds.reverse()
    evens.reverse()
    parts = [[odds.pop()] for _ in range(odd_parts)]
    for _ in range(p):
        if evens:
            parts.append([evens.pop()])
        else:
            parts.append([odds.pop(), odds.pop()])
    rest = evens + odds
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
