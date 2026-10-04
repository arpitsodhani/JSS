import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    first = data[0].decode()
    second = data[1].decode()
    return first, second


# --- clause: build_tail :: (counts: list[int]) -> str ---
def build_tail(counts):
    out = []
    for idx in range(26):
        if counts[idx] > 0:
            out.append(chr(97 + idx) * counts[idx])
    return "".join(out)


# --- clause: find_answer :: (s: str, t: str) -> str ---
def find_answer(s, t):
    n = len(s)
    m = len(t)
    limit = min(n, m)
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - 97] = counts[ord(ch) - 97] + 1
    matched = 0
    while matched < limit and counts[ord(t[matched]) - 97]:
        counts[ord(t[matched]) - 97] -= 1
        matched = matched + 1
    if matched == limit and n > m:
        return t + build_tail(counts)
    for i in range(matched, -1, -1):
        if i < matched:
            counts[ord(t[i]) - 97] += 1
        if i < limit:
            found = -1
            for c in range(ord(t[i]) - 97 + 1, 26):
                if counts[c]:
                    found = c
                    break
            if found >= 0:
                counts[found] -= 1
                return t[:i] + chr(97 + found) + build_tail(counts)
    return "-1"


# --- clause: main :: () -> None ---
def main():
    pair = read_input()
    print(find_answer(pair[0], pair[1]))


if __name__ == "__main__":
    main()
