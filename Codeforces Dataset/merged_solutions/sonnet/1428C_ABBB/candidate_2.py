import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    return [tokens[1 + i].decode() for i in range(t)]


# --- clause: shortest_length :: (s: str) -> int ---
def shortest_length(s):
    stack = 0
    low = 0
    for ch in s:
        if ch == "A":
            stack += 1
            low += 1
        elif stack or low:
            if stack:
                stack -= 1
                low -= 1
            else:
                low -= 1
        else:
            low += 1
    return low


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(shortest_length(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
