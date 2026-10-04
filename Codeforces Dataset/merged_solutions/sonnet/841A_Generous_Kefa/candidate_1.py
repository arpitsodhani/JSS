import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[1]), data[2].decode()


# --- clause: can_share :: (k: int, s: str) -> bool ---
def can_share(k, s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in counts:
        if counts[ch] > k:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    k, s = read_input()
    sys.stdout.write("YES\n" if can_share(k, s) else "NO\n")


if __name__ == "__main__":
    main()
