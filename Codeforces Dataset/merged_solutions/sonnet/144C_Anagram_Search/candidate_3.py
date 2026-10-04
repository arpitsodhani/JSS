import sys


# --- clause: read_input :: () -> tuple[bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    s = data[0]
    p = data[1]
    return s, p


# --- clause: count_good :: (s: bytes, p: bytes) -> int ---
def count_good(s, p):
    width = len(p)
    length = len(s)
    if width > length:
        return 0
    allowed = [0] * 26
    for ch in p:
        allowed[ch - 97] += 1
    total = 0
    seen = [0] * 26
    for i in range(length):
        ch = s[i]
        if ch != 63:
            seen[ch - 97] += 1
        if i >= width:
            gone = s[i - width]
            if gone != 63:
                seen[gone - 97] -= 1
        if i < width - 1:
            continue
        good = True
        for k in range(26):
            if seen[k] > allowed[k]:
                good = False
                break
        if good:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    s, p = read_input()
    print(count_good(s, p))


if __name__ == "__main__":
    main()
