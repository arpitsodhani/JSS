import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return list(data[1:1 + n])


# --- clause: merge_patterns :: (rows: list[bytes]) -> str ---
def merge_patterns(rows):
    width = len(rows[0])
    fixed = [0] * width
    for row in rows:
        for j in range(width):
            ch = row[j]
            if ch == 63 or fixed[j] < 0:
                continue
            if fixed[j] == 0:
                fixed[j] = ch
            elif fixed[j] != ch:
                fixed[j] = -1
    out = []
    for value in fixed:
        if value == 0:
            out.append("a")
        elif value < 0:
            out.append("?")
        else:
            out.append(chr(value))
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%s\n" % merge_patterns(read_input()))


if __name__ == "__main__":
    main()
