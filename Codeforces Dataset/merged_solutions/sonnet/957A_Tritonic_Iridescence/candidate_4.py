import sys


# --- clause: read_input :: () -> str ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[1].decode()


# --- clause: has_free_choice :: (s: str) -> bool ---
def has_free_choice(s):
    n = len(s)
    for i in range(n - 1):
        if s[i] != "?" and s[i] == s[i + 1]:
            return False
    located = False
    for i in range(n):
        if s[i] != "?":
            continue
        if i == 0 or i == n - 1:
            located = True
        elif s[i - 1] == "?" or s[i + 1] == "?":
            located = True
        elif s[i - 1] == s[i + 1]:
            located = True
    return located


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("Yes\n" if has_free_choice(read_input()) else "No\n")


if __name__ == "__main__":
    main()
