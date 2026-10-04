import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: is_magic :: (digits: str) -> bool ---
def is_magic(digits):
    if not digits.startswith("1"):
        return False
    for piece in digits.split("1"):
        if piece not in ("", "4", "44"):
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if is_magic(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
