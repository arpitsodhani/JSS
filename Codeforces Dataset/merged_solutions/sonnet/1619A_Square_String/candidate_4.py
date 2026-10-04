import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [bytes(w) for w in data[1:t + 1]]


# --- clause: is_square :: (s: bytes) -> str ---
def is_square(s):
    size = len(s)
    if size % 2:
        return "NO"
    half = size // 2
    if s[:half] == s[half:]:
        return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(is_square(word))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
