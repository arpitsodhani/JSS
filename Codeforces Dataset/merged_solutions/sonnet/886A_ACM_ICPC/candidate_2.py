import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    return list(map(int, sys.stdin.buffer.read().split()))[:6]


# --- clause: can_split :: (scores: list[int]) -> bool ---
def can_split(scores):
    amount = sum(scores)
    if amount % 2:
        return False
    half = amount // 2
    for i in range(6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                if scores[i] + scores[j] + scores[k] == half:
                    return True
    return False


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if can_split(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
