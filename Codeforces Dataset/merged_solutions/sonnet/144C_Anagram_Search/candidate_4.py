import sys


# --- clause: read_input :: () -> tuple[bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return bytes(data[0]), bytes(data[1])


# --- clause: count_good :: (s: bytes, p: bytes) -> int ---
def count_good(s, p):
    width = len(p)
    length = len(s)
    if width > length:
        return 0
    budget = [0] * 26
    for ch in p:
        budget[ch - 97] += 1
    used = [0] * 26
    offenders = set()
    for i in range(width):
        ch = s[i]
        if ch != 63:
            k = ch - 97
            used[k] += 1
            if used[k] > budget[k]:
                offenders.add(k)
    total = 1 if not offenders else 0
    for i in range(width, length):
        ch = s[i]
        if ch != 63:
            k = ch - 97
            used[k] += 1
            if used[k] > budget[k]:
                offenders.add(k)
        gone = s[i - width]
        if gone != 63:
            k = gone - 97
            used[k] -= 1
            if used[k] <= budget[k]:
                offenders.discard(k)
        if not offenders:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    s, p = read_input()
    answer = count_good(s, p)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
