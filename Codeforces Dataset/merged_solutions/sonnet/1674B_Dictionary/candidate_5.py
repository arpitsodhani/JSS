import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    words = []
    pos = 1
    for _ in range(t):
        words.append(data[pos])
        pos += 1
    return words


# --- clause: dictionary_index :: (word: bytes) -> int ---
def dictionary_index(word):
    first = word[0] - 97
    second = word[1] - 97
    if second > first:
        second -= 1
    return first * 25 + second + 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(str(dictionary_index(word)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
