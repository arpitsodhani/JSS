import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    text = sys.stdin.buffer.read().decode().strip()
    return [int(part) for part in text.split(",")]


# --- clause: group_pages :: (pages: list[int]) -> list[str] ---
def group_pages(pages):
    order = sorted(set(pages))
    out = []
    start = order[0]
    last = order[0]
    for value in order[1:]:
        if value == last + 1:
            last = value
            continue
        out.append(str(start) if start == last else "%d-%d" % (start, last))
        start = value
        last = value
    out.append(str(start) if start == last else "%d-%d" % (start, last))
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(",".join(group_pages(read_input())) + "\n")


if __name__ == "__main__":
    main()
