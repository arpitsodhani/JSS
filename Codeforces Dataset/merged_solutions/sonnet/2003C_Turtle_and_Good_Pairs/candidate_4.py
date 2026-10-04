import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [bytes(data[2 * i + 2]) for i in range(t)]


# --- clause: spread_letters :: (s: bytes) -> str ---
def spread_letters(s):
    counts = [0] * 26
    for ch in s:
        counts[ch - 97] += 1
    out = []
    left = len(s)
    while left:
        for k in range(26):
            if counts[k]:
                out.append(chr(97 + k))
                counts[k] -= 1
                left -= 1
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(spread_letters(word))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
