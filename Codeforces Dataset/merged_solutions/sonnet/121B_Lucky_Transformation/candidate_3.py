import sys


# --- clause: read_input :: () -> tuple[int, int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    digits = list(data[2].decode())
    return n, k, digits

# --- clause: transform :: (n: int, k: int, digits: list[str]) -> str ---
def transform(n, k, digits):
    pos = 0
    while pos + 1 < n and k > 0:
        if digits[pos] == "4" and digits[pos + 1] == "7":
            if pos % 2:
                if digits[pos - 1] == "4":
                    if k % 2:
                        digits[pos] = "7"
                        digits[pos + 1] = "7"
                    break
                digits[pos] = "7"
                digits[pos + 1] = "7"
            else:
                if pos + 2 < n and digits[pos + 2] == "7":
                    if k % 2:
                        digits[pos + 1] = "4"
                    break
                digits[pos + 1] = "4"
            k -= 1
        pos += 1
    return "".join(digits)

# --- clause: main :: () -> None ---
def main():
    n, k, digits = read_input()
    sys.stdout.write(transform(n, k, digits) + "\n")


if __name__ == "__main__":
    main()
