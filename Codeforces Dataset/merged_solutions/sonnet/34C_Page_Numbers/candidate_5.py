import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    text = sys.stdin.buffer.read().decode().strip()
    return [int(part) for part in text.split(",")]


# --- clause: group_pages :: (pages: list[int]) -> list[str] ---
def group_pages(pages):
    order = sorted(set(pages))
    lines = []
    head_pos = order[0]
    last = order[0]
    for number in order[1:]:
        if number == last + 1:
            last = number
            continue
        lines.append(str(head_pos) if head_pos == last else "%d-%d" % (head_pos, last))
        head_pos = number
        last = number
    lines.append(str(head_pos) if head_pos == last else "%d-%d" % (head_pos, last))
    return lines


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(",".join(group_pages(read_input())) + "\n")


if __name__ == "__main__":
    main()
