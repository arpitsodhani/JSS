import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]


# --- clause: shortest_length :: (s: str) -> int ---
def shortest_length(s):
    stack = 0
    left = 0
    for ch in s:
        if ch == "A":
            stack += 1
            left += 1
        elif stack or left:
            if stack:
                stack -= 1
                left -= 1
            else:
                left -= 1
        else:
            left += 1
    return left


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(shortest_length(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
