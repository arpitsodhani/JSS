import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), data[1].decode()


# --- clause: build_tail :: (counts: list[int]) -> str ---
def build_tail(counts):
    parts = []
    for i in range(26):
        if counts[i]:
            parts.append(chr(97 + i) * counts[i])
    return "".join(parts)


# --- clause: find_answer :: (s: str, t: str) -> str ---
def find_answer(s, t):
    n = len(s)
    limit = min(n, len(t))
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - 97] += 1
    matched = 0
    while matched < limit and counts[ord(t[matched]) - 97] > 0:
        counts[ord(t[matched]) - 97] -= 1
        matched += 1
    if matched == limit and n > len(t):
        return t[:limit] + build_tail(counts)
    for i in range(matched, -1, -1):
        if i < matched:
            counts[ord(t[i]) - 97] += 1
        if i < limit:
            for c in range(ord(t[i]) - 96, 26):
                if counts[c]:
                    counts[c] -= 1
                    return t[:i] + chr(97 + c) + build_tail(counts)
    return "-1"


# --- clause: main :: () -> None ---
def main():
    s, t = read_input()
    print(find_answer(s, t))


if __name__ == "__main__":
    main()
