import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return "".join(sys.stdin.read().split())


# --- clause: table_sizes :: (text: str) -> list[int] ---
def table_sizes(text):
    sizes = []
    stack = []
    position = 0
    total = len(text)
    while position < total:
        close = text.find(">", position)
        name = text[position + 1:close]
        position = close + 1
        if name == "td":
            stack[-1] += 1
        elif name == "table":
            stack.append(0)
        elif name == "/table":
            sizes.append(stack.pop())
    sizes.sort()
    return sizes


# --- clause: main :: () -> None ---
def main():
    sizes = table_sizes(read_input())
    sys.stdout.write(" ".join(map(str, sizes)) + "\n")


if __name__ == "__main__":
    main()
