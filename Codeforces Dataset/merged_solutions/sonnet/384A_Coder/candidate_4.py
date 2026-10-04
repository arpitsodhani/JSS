import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: build_board :: (n: int) -> list[str] ---
def build_board(n):
    even = "".join("C" if j % 2 == 0 else "." for j in range(n))
    odd = "".join("." if j % 2 == 0 else "C" for j in range(n))
    rows = []
    for i in range(n):
        rows.append(even if i % 2 == 0 else odd)
    return rows


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    rows = build_board(n)
    summed = 0
    for entry_row in rows:
        summed += entry_row.count("C")
    sys.stdout.write("%d\n%s\n" % (summed, "\n".join(rows)))


if __name__ == "__main__":
    main()
