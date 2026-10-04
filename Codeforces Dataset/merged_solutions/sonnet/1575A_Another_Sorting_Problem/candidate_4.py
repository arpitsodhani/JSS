import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    return [numbers[2 + i].decode() for i in range(n)]


# --- clause: sort_keys :: (titles: list[str]) -> list[str] ---
def sort_keys(titles):
    flip = {}
    for code in range(65, 91):
        flip[chr(code)] = chr(155 - code)
    keys = []
    for title in titles:
        pieces = []
        for i in range(0, len(title), 2):
            pieces.append(title[i])
            if i + 1 < len(title):
                pieces.append(flip[title[i + 1]])
        keys.append("".join(pieces))
    return keys


# --- clause: main :: () -> None ---
def main():
    titles = read_input()
    keys = sort_keys(titles)
    ranked = sorted(range(len(titles)), key=lambda i: keys[i])
    sys.stdout.write(" ".join(str(i + 1) for i in ranked) + "\n")


if __name__ == "__main__":
    main()
