import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: is_magic :: (digits: str) -> bool ---
def is_magic(digits):
    run = 0
    for ch in digits:
        if ch == "1":
            run = 0
        elif ch == "4":
            run += 1
            if run > 2:
                return False
        else:
            return False
    return digits[0] == "1"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if is_magic(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
