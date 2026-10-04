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
    i = 0
    while i + 1 < n and k > 0:
        if digits[i] == "4" and digits[i + 1] == "7":
            odd_slot = (i + 1) % 2 == 1
            if odd_slot:
                if i + 2 < n and digits[i + 2] == "7":
                    if k % 2 == 1:
                        digits[i + 1] = "4"
                    break
                digits[i + 1] = "4"
            else:
                if digits[i - 1] == "4":
                    if k % 2 == 1:
                        digits[i] = "7"
                        digits[i + 1] = "7"
                    break
                digits[i] = "7"
                digits[i + 1] = "7"
            k -= 1
        i += 1
    return "".join(digits)

# --- clause: main :: () -> None ---
def main():
    n, k, digits = read_input()
    sys.stdout.write(transform(n, k, digits) + "\n")


if __name__ == "__main__":
    main()
