import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((int(data[1 + 2 * i]), data[2 + 2 * i].decode()))
    return cases


# --- clause: final_length :: (x: int, s: str) -> int ---
def final_length(x, s):
    mod = 1000000007
    row = [int(ch) for ch in s]
    size = len(row)
    length = size % mod
    for step in range(1, x + 1):
        digit = row[step - 1]
        if size < x and digit > 1:
            tail = row[step:size]
            for _ in range(digit - 1):
                for value in tail:
                    row.append(value)
                    size += 1
                    if size >= x:
                        break
                if size >= x:
                    break
        length = (length + (digit - 1) * ((length - step) % mod)) % mod
    return length % mod


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, s in read_input():
        out.append(final_length(x, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
