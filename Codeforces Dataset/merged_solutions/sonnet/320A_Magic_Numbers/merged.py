import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause is_magic [Confidence: 0.40]
def is_magic(digits):
    i = 0
    n = len(digits)
    while i < n:
        if digits[i] != "1":
            return False
        i += 1
        fours = 0
        while i < n and digits[i] == "4" and fours < 2:
            i += 1
            fours += 1
    return True

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("YES\n" if is_magic(read_input()) else "NO\n")


if __name__ == "__main__":
    main()

