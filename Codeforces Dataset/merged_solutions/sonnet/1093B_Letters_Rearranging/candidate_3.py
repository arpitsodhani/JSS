import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    words = []
    pos = 1
    while len(words) < t:
        words.append(data[pos].decode())
        pos += 1
    return words


# --- clause: rearrange :: (word: str) -> str ---
def rearrange(word):
    tally = [0] * 26
    for ch in word:
        tally[ord(ch) - 97] += 1
    seen = 0
    for count in tally:
        if count:
            seen += 1
    if seen < 2:
        return "-1"
    built = []
    for k in range(26):
        if tally[k]:
            built.append(chr(97 + k) * tally[k])
    return "".join(built)


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(rearrange(word))
    print("\n".join(out))


if __name__ == "__main__":
    main()
