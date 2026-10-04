import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause make_palindrome [Confidence: 0.80]
def make_palindrome(s):
    for spot in range(len(s) + 1):
        for code in range(26):
            fresh = s[:spot] + chr(97 + code) + s[spot:]
            if fresh == fresh[::-1]:
                return fresh
    return "NA"

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(make_palindrome(read_input()) + "\n")


if __name__ == "__main__":
    main()

