import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return list(data[1:1 + t])


# --- clause: is_square :: (s: bytes) -> str ---
def is_square(s):
    size = len(s)
    if size & 1:
        return "NO"
    half = size // 2
    if s[:half] == s[half:]:
        return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(is_square(s))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
