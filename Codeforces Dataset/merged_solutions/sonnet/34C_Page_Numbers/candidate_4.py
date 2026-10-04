import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    text = sys.stdin.buffer.read().decode().strip()
    return [int(part) for part in text.split(",")]


# --- clause: group_pages :: (pages: list[int]) -> list[str] ---
def group_pages(pages):
    order = sorted(set(pages))
    out = []
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and order[j + 1] == order[j] + 1:
            j += 1
        if i == j:
            out.append(str(order[i]))
        else:
            out.append("%d-%d" % (order[i], order[j]))
        i = j + 1
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(",".join(group_pages(read_input())) + "\n")


if __name__ == "__main__":
    main()
