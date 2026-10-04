import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: is_magic :: (digits: str) -> bool ---
def is_magic(digits):
    rest = digits
    while rest:
        if rest.startswith("144"):
            rest = rest[3:]
        elif rest.startswith("14"):
            rest = rest[2:]
        elif rest.startswith("1"):
            rest = rest[1:]
        else:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if is_magic(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
