import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cases = []
    for i in range(t):
        cases.append((int(numbers[1 + 2 * i]), numbers[2 + 2 * i].decode()))
    return cases


# --- clause: final_length :: (x: int, s: str) -> int ---
def final_length(x, s):
    mod = 1000000007
    row = []
    for ch in s:
        row.append(int(ch))
    length = len(row) % mod
    for step in range(1, x + 1):
        digit = row[step - 1]
        if len(row) < x and digit > 1:
            copies = row[step:]
            spare = x - len(row)
            block = copies * (digit - 1)
            row.extend(block[:spare])
        length = (length + (digit - 1) * (length - step)) % mod
    return length % mod


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, s in read_input():
        out.append(final_length(x, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
