import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    return [raw[1 + i].decode() for i in range(t)]


# --- clause: shortest_length :: (s: str) -> int ---
def shortest_length(s):
    stack = 0
    first_side = 0
    for ch in s:
        if ch == "A":
            stack += 1
            first_side += 1
        elif stack or first_side:
            if stack:
                stack -= 1
                first_side -= 1
            else:
                first_side -= 1
        else:
            first_side += 1
    return first_side


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s in read_input():
        lines.append(shortest_length(s))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
