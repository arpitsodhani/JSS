import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[i] for i in range(1, t + 1)]


# --- clause: is_square :: (s: bytes) -> str ---
def is_square(s):
    size = len(s)
    if size % 2:
        return "NO"
    half = size // 2
    i = 0
    while i < half:
        if s[i] != s[i + half]:
            return "NO"
        i += 1
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(is_square(s))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
