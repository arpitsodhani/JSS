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
    need = [0] * 26
    for ch in p:
        need[ch - 97] += 1
    have = [0] * 26
    excess = 0
    for i in range(width):
        ch = s[i]
        if ch != 63:
            k = ch - 97
            have[k] += 1
            if have[k] == need[k] + 1:
                excess += 1
    total = 1 if excess == 0 else 0
    for i in range(width, len(s)):
        ch = s[i]
        if ch != 63:
            k = ch - 97
            have[k] += 1
            if have[k] == need[k] + 1:
                excess += 1
        gone = s[i - width]
        if gone != 63:
            k = gone - 97
            if have[k] == need[k] + 1:
                excess -= 1
            have[k] -= 1
        if excess == 0:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    s, p = read_input()
    sys.stdout.write(str(count_good(s, p)) + "\n")


if __name__ == "__main__":
    main()
