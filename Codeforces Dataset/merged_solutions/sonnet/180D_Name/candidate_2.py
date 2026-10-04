import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    s = tokens[0].decode()
    t = tokens[1].decode()
    return s, t


# --- clause: build_tail :: (counts: list[int]) -> str ---
def build_tail(counts):
    chunks = []
    for code in range(26):
        if counts[code] > 0:
            chunks.append(chr(ord("a") + code) * counts[code])
    return "".join(chunks)


# --- clause: find_answer :: (s: str, t: str) -> str ---
def find_answer(s, t):
    n = len(s)
    m = len(t)
    limit = n if n < m else m
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - ord("a")] += 1
    matched = 0
    while matched < limit and counts[ord(t[matched]) - ord("a")] > 0:
        counts[ord(t[matched]) - ord("a")] -= 1
        matched += 1
    if matched == limit and n > m:
        return t[:limit] + build_tail(counts)
    for i in range(matched, -1, -1):
        if i < matched:
            counts[ord(t[i]) - ord("a")] += 1
        if i < limit:
            here = ord(t[i]) - ord("a")
            for c in range(here + 1, 26):
                if counts[c] > 0:
                    counts[c] -= 1
                    return t[:i] + chr(ord("a") + c) + build_tail(counts)
    return "-1"


# --- clause: main :: () -> None ---
def main():
    s, t = read_input()
    sys.stdout.write(find_answer(s, t) + "\n")


if __name__ == "__main__":
    main()
