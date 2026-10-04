import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    b = int(data[0])
    k = int(data[1])
    digits = list(map(int, data[2:k + 2]))
    return b, k, digits


# --- clause: parity :: (b: int, k: int, digits: list[int]) -> str ---
def parity(b, k, digits):
    if b & 1:
        rest = sum(digits) % 2
    else:
        rest = digits[-1] % 2
    return "odd" if rest else "even"


# --- clause: main :: () -> None ---
def main():
    b, k, digits = read_input()
    sys.stdout.write("%s\n" % parity(b, k, digits))


if __name__ == "__main__":
    main()
