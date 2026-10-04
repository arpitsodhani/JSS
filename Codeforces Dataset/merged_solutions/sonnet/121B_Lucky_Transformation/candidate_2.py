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
        if digits[i] != "4" or digits[i + 1] != "7":
            i += 1
            continue
        if i % 2 == 0:
            digits[i + 1] = "4"
            nxt = i + 1
        else:
            digits[i] = "7"
            digits[i + 1] = "7"
            nxt = i - 1
        k -= 1
        if nxt + 1 < n and digits[nxt] == "4" and digits[nxt + 1] == "7":
            if k % 2 == 1:
                if nxt % 2 == 0:
                    digits[nxt + 1] = "4"
                else:
                    digits[nxt] = "7"
                    digits[nxt + 1] = "7"
            break
        if nxt > i:
            i = nxt
        else:
            i += 1
    return "".join(digits)

# --- clause: main :: () -> None ---
def main():
    n, k, digits = read_input()
    sys.stdout.write(transform(n, k, digits) + "\n")


if __name__ == "__main__":
    main()
