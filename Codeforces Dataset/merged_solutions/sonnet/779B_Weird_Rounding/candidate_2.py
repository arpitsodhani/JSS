import sys


# --- clause: read_input :: () -> tuple[str, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    digits, k = data[0].decode(), int(data[1])
    return digits, k


# --- clause: fewest_deletions :: (digits: str, k: int) -> int ---
def fewest_deletions(digits, k):
    size = len(digits)
    target = 10 ** k
    best = size - 1
    for mask in range(1, 1 << size):
        kept = []
        for i in range(size):
            if mask >> i & 1:
                kept.append(digits[i])
        if len(kept) > 1 and kept[0] == "0":
            continue
        value = int("".join(kept))
        if value % target == 0:
            removed = size - len(kept)
            if removed < best:
                best = removed
    return best


# --- clause: main :: () -> None ---
def main():
    digits, k = read_input()
    sys.stdout.write("%d\n" % fewest_deletions(digits, k))


if __name__ == "__main__":
    main()
