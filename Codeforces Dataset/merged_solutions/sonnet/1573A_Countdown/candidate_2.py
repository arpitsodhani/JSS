import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[i] for i in range(2, 2 * t + 2, 2)]


# --- clause: countdown_cost :: (digits: bytes) -> int ---
def countdown_cost(digits):
    total = sum(ch - 48 for ch in digits)
    nonzero = sum(1 for ch in digits if ch != 48)
    if nonzero and digits[-1] != 48:
        nonzero -= 1
    return total + nonzero


# --- clause: main :: () -> None ---
def main():
    out = []
    for digits in read_input():
        out.append(str(countdown_cost(digits)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
