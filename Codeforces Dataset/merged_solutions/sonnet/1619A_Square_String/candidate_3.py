import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i] for i in range(t)]


# --- clause: is_square :: (s: bytes) -> str ---
def is_square(s):
    size = len(s)
    if size % 2:
        return "NO"
    half = size // 2
    for i in range(half):
        if s[i] != s[i + half]:
            return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(is_square(s))
    print("\n".join(out))


if __name__ == "__main__":
    main()
