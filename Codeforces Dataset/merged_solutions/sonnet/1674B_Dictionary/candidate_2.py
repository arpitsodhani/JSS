import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return list(data[1:1 + t])


# --- clause: dictionary_index :: (word: bytes) -> int ---
def dictionary_index(word):
    first = word[0] - 97
    second = word[1] - 97
    seen = 0
    for other in range(26):
        if other == first:
            continue
        seen += 1
        if other == second:
            break
    return first * 25 + seen


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(str(dictionary_index(word)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
