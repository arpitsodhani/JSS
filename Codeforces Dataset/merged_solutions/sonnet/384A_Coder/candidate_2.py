import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: build_board :: (n: int) -> list[str] ---
def build_board(n):
    rows = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append("C" if (i + j) % 2 == 0 else ".")
        rows.append("".join(line))
    return rows


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    rows = build_board(n)
    amount = 0
    for record in rows:
        amount += record.count("C")
    sys.stdout.write("%d\n%s\n" % (amount, "\n".join(rows)))


if __name__ == "__main__":
    main()
