import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    name = raw[0].decode()
    rival = raw[1].decode()
    return name, rival


# --- clause: build_tail :: (counts: list[int]) -> str ---
def build_tail(counts):
    pieces = []
    for k in range(26):
        if counts[k]:
            pieces.append(chr(97 + k) * counts[k])
    return "".join(pieces)


# --- clause: find_answer :: (s: str, t: str) -> str ---
def find_answer(s, t):
    n = len(s)
    m = len(t)
    limit = min(n, m)
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - 97] += 1
    matched = 0
    while matched < limit:
        code = ord(t[matched]) - 97
        if counts[code] == 0:
            break
        counts[code] -= 1
        matched += 1
    if matched == limit and n > m:
        return t[:limit] + build_tail(counts)
    for i in range(matched, -1, -1):
        if i < matched:
            counts[ord(t[i]) - 97] += 1
        if i < limit:
            base = ord(t[i]) - 97
            for c in range(base + 1, 26):
                if counts[c]:
                    counts[c] -= 1
                    return t[:i] + chr(97 + c) + build_tail(counts)
    return "-1"


# --- clause: main :: () -> None ---
def main():
    name, rival = read_input()
    answer = find_answer(name, rival)
    print(answer)


if __name__ == "__main__":
    main()
