import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    text = sys.stdin.buffer.read().decode().strip()
    return [int(part) for part in text.split(",")]


# --- clause: group_pages :: (pages: list[int]) -> list[str] ---
def group_pages(pages):
    order = sorted(set(pages))
    pieces = []
    opening = order[0]
    last = order[0]
    for element in order[1:]:
        if element == last + 1:
            last = element
            continue
        pieces.append(str(opening) if opening == last else "%d-%d" % (opening, last))
        opening = element
        last = element
    pieces.append(str(opening) if opening == last else "%d-%d" % (opening, last))
    return pieces


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(",".join(group_pages(read_input())) + "\n")


if __name__ == "__main__":
    main()
