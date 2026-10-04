import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    words = []
    pos = 1
    while len(words) < t:
        words.append(data[pos])
        pos += 1
    return words


# --- clause: dictionary_index :: (word: bytes) -> int ---
def dictionary_index(word):
    order = {}
    place = 0
    for a in range(26):
        for b in range(26):
            if a != b:
                place += 1
                order[(a, b)] = place
    return order[(word[0] - 97, word[1] - 97)]


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(str(dictionary_index(word)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
