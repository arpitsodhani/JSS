import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    rows = []
    for i in range(t):
        rows.append(data[2 * i + 2])
    return rows


# --- clause: countdown_cost :: (digits: bytes) -> int ---
def countdown_cost(digits):
    total = 0
    nonzero = 0
    for ch in digits:
        value = ch - 48
        total += value
        if value:
            nonzero += 1
    swaps = nonzero
    if swaps > 0 and digits[len(digits) - 1] > 48:
        swaps -= 1
    return total + swaps


# --- clause: main :: () -> None ---
def main():
    out = []
    for digits in read_input():
        out.append(str(countdown_cost(digits)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
