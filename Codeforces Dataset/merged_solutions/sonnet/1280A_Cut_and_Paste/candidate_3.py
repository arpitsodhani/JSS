import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    cases = []
    for i in range(t):
        cases.append((int(fields[1 + 2 * i]), fields[2 + 2 * i].decode()))
    return cases


# --- clause: final_length :: (x: int, s: str) -> int ---
def final_length(x, s):
    mod = 1000000007
    entry_row = [int(ch) for ch in s]
    size = len(entry_row)
    length = size % mod
    for jump in range(1, x + 1):
        digit = entry_row[jump - 1]
        if size < x and digit > 1:
            tail = entry_row[jump:size]
            for _ in range(digit - 1):
                for value in tail:
                    entry_row.append(value)
                    size += 1
                    if size >= x:
                        break
                if size >= x:
                    break
        length = (length + (digit - 1) * ((length - jump) % mod)) % mod
    return length % mod


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, s in read_input():
        out.append(final_length(x, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
