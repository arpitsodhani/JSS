import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    return [numbers[1 + i].decode() for i in range(t)]


# --- clause: shortest_length :: (s: str) -> int ---
def shortest_length(s):
    stack = []
    for ch in s:
        if ch == "B" and stack:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(shortest_length(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
