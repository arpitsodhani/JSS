import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0].decode())


# --- clause: best_product :: (n: int) -> int ---
def best_product(n):
    if n < 10:
        return 1 if n == 0 else n
    digits = str(n)
    best = 1
    for digit in digits:
        best *= int(digit)
    for cut in range(len(digits)):
        if digits[cut] == "0":
            continue
        lowered = digits[:cut] + str(int(digits[cut]) - 1) + "9" * (len(digits) - cut - 1)
        lowered = lowered.lstrip("0")
        if not lowered:
            continue
        product = 1
        for digit in lowered:
            product *= int(digit)
        if product > best:
            best = product
    return best


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    print(best_product(n))


if __name__ == "__main__":
    main()
