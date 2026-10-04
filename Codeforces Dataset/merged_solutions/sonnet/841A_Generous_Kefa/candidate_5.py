import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return int(raw[1]), raw[2].decode()


# --- clause: can_share :: (k: int, s: str) -> bool ---
def can_share(k, s):
    frequency = {}
    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1
    for ch in frequency:
        if frequency[ch] > k:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    k, s = read_input()
    sys.stdout.write("YES\n" if can_share(k, s) else "NO\n")


if __name__ == "__main__":
    main()
