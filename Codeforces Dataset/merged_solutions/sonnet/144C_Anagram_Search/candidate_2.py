import sys


# --- clause: read_input :: () -> tuple[bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0], data[1]


# --- clause: count_good :: (s: bytes, p: bytes) -> int ---
def count_good(s, p):
    width = len(p)
    if width > len(s):
        return 0
    room = [0] * 26
    for ch in p:
        room[ch - 97] += 1
    spare = list(room)
    total = 0
    broken = 0
    for i in range(len(s)):
        ch = s[i]
        if ch != 63:
            k = ch - 97
            spare[k] -= 1
            if spare[k] == -1:
                broken += 1
        if i >= width:
            gone = s[i - width]
            if gone != 63:
                k = gone - 97
                if spare[k] == -1:
                    broken -= 1
                spare[k] += 1
        if i >= width - 1 and broken == 0:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    s, p = read_input()
    sys.stdout.write("%d\n" % count_good(s, p))


if __name__ == "__main__":
    main()
