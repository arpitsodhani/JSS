import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: is_magic :: (digits: str) -> bool ---
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


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if is_magic(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
