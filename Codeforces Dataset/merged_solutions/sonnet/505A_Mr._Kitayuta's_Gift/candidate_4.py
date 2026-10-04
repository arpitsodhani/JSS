import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: make_palindrome :: (s: str) -> str ---
def make_palindrome(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    spot = 0
    while spot <= len(s):
        for ch in letters:
            fresh = s[:spot] + ch + s[spot:]
            if fresh == fresh[::-1]:
                return fresh
        spot += 1
    return "NA"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(make_palindrome(read_input()) + "\n")


if __name__ == "__main__":
    main()
