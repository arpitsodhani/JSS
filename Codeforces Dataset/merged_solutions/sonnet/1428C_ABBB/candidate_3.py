import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    return [fields[1 + i].decode() for i in range(t)]


# --- clause: shortest_length :: (s: str) -> int ---
def shortest_length(s):
    stack = 0
    begin = 0
    for ch in s:
        if ch == "A":
            stack += 1
            begin += 1
        elif stack or begin:
            if stack:
                stack -= 1
                begin -= 1
            else:
                begin -= 1
        else:
            begin += 1
    return begin


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for s in read_input():
        pieces.append(shortest_length(s))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
