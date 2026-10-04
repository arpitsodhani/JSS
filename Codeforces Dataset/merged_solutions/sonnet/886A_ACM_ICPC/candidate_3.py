import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    return list(map(int, sys.stdin.buffer.read().split()))[:6]


# --- clause: can_split :: (scores: list[int]) -> bool ---
def can_split(scores):
    total = sum(scores)
    if total % 2:
        return False
    for mask in range(64):
        if bin(mask).count("1") != 3:
            continue
        here = 0
        for i in range(6):
            if (mask >> i) & 1:
                here += scores[i]
        if here * 2 == total:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if can_split(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
