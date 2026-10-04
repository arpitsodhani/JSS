import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return int(numbers[1]), numbers[2].decode()


# --- clause: can_share :: (k: int, s: str) -> bool ---
def can_share(k, s):
    for ch in set(s):
        if s.count(ch) > k:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    k, s = read_input()
    sys.stdout.write("YES\n" if can_share(k, s) else "NO\n")


if __name__ == "__main__":
    main()
