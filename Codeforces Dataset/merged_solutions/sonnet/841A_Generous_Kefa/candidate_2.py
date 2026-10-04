import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return int(tokens[1]), tokens[2].decode()


# --- clause: can_share :: (k: int, s: str) -> bool ---
def can_share(k, s):
    tally = {}
    for ch in s:
        tally[ch] = tally.get(ch, 0) + 1
    for ch in tally:
        if tally[ch] > k:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    k, s = read_input()
    sys.stdout.write("YES\n" if can_share(k, s) else "NO\n")


if __name__ == "__main__":
    main()
