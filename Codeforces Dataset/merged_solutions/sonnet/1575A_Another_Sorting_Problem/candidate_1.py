import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[2 + i].decode() for i in range(n)]


# --- clause: sort_keys :: (titles: list[str]) -> list[str] ---
def sort_keys(titles):
    keys = []
    for title in titles:
        letters = []
        for i in range(len(title)):
            if i % 2:
                letters.append(chr(155 - ord(title[i])))
            else:
                letters.append(title[i])
        keys.append("".join(letters))
    return keys


# --- clause: main :: () -> None ---
def main():
    titles = read_input()
    keys = sort_keys(titles)
    order = sorted(range(len(titles)), key=lambda i: keys[i])
    sys.stdout.write(" ".join(str(i + 1) for i in order) + "\n")


if __name__ == "__main__":
    main()
