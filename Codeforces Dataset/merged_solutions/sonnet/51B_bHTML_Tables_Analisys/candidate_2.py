import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return "".join(sys.stdin.read().split())


# --- clause: table_sizes :: (text: str) -> list[int] ---
def table_sizes(text):
    sizes = []
    counts = []
    for chunk in text.split("<")[1:]:
        tag = chunk.split(">")[0]
        if tag == "table":
            counts.append(0)
        elif tag == "/table":
            sizes.append(counts.pop())
        elif tag == "td":
            counts[-1] += 1
    return sorted(sizes)


# --- clause: main :: () -> None ---
def main():
    sizes = table_sizes(read_input())
    sys.stdout.write(" ".join(map(str, sizes)) + "\n")


if __name__ == "__main__":
    main()
