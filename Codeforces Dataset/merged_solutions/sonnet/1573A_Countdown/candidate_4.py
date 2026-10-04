import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [bytes(data[2 * i + 2]) for i in range(t)]


# --- clause: countdown_cost :: (digits: bytes) -> int ---
def countdown_cost(digits):
    total = 0
    nonzero = 0
    for index in range(len(digits)):
        value = digits[index] - 48
        total += value
        if value != 0:
            nonzero += 1
    if nonzero and digits[len(digits) - 1] != 48:
        nonzero -= 1
    return total + nonzero


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(str(countdown_cost(word)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
