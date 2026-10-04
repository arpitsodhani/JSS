import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rows = []
    for i in range(n):
        rows.append(data[1 + i])
    return rows


# --- clause: merge_patterns :: (rows: list[bytes]) -> str ---
def merge_patterns(rows):
    width = len(rows[0])
    out = []
    for j in range(width):
        seen = 0
        for row in rows:
            ch = row[j]
            if ch == 63:
                continue
            if seen == 0:
                seen = ch
            elif seen != ch:
                seen = -1
                break
        if seen < 0:
            out.append("?")
        elif seen:
            out.append(chr(seen))
        else:
            out.append("z")
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    print(merge_patterns(read_input()))


if __name__ == "__main__":
    main()
