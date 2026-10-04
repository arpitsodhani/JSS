import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: make_palindrome :: (s: str) -> str ---
def make_palindrome(s):
    for spot in range(len(s) + 1):
        for code in range(26):
            fresh = s[:spot] + chr(97 + code) + s[spot:]
            if fresh == fresh[::-1]:
                return fresh
    return "NA"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(make_palindrome(read_input()) + "\n")


if __name__ == "__main__":
    main()
