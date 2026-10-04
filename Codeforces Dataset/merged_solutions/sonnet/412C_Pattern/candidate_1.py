import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i] for i in range(n)]


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
        if seen == 0:
            out.append("a")
        elif seen < 0:
            out.append("?")
        else:
            out.append(chr(seen))
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(merge_patterns(read_input()) + "\n")


if __name__ == "__main__":
    main()
