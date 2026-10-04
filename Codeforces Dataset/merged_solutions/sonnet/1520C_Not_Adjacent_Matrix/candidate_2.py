import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: build_matrix :: (n: int) -> list[list[int]] | None ---
def build_matrix(n):
    if n == 2:
        return None
    rows = []
    value = 1
    total = n * n
    stream = []
    while value <= total:
        stream.append(value)
        value += 2
    value = 2
    while value <= total:
        stream.append(value)
        value += 2
    at = 0
    for _ in range(n):
        rows.append(stream[at:at + n])
        at += n
    return rows


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        rows = build_matrix(n)
        if rows is None:
            out.append("-1")
        else:
            for row in rows:
                out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
