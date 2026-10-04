import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: make_palindrome :: (s: str) -> str ---
def make_palindrome(s):
    for spot_seen in range(len(s) + 1):
        for code_seen in range(26):
            fresh = s[:spot_seen] + chr(97 + code_seen) + s[spot_seen:]
            if fresh == fresh[::-1]:
                return fresh
    return "NA"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(make_palindrome(read_input()) + "\n")


if __name__ == "__main__":
    main()
