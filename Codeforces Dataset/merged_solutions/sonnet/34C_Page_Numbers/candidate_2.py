import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    text = sys.stdin.buffer.read().decode().strip()
    return [int(part) for part in text.split(",")]


# --- clause: group_pages :: (pages: list[int]) -> list[str] ---
def group_pages(pages):
    order = sorted(set(pages))
    out = []
    begin = order[0]
    last = order[0]
    for item in order[1:]:
        if item == last + 1:
            last = item
            continue
        out.append(str(begin) if begin == last else "%d-%d" % (begin, last))
        begin = item
        last = item
    out.append(str(begin) if begin == last else "%d-%d" % (begin, last))
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(",".join(group_pages(read_input())) + "\n")


if __name__ == "__main__":
    main()
