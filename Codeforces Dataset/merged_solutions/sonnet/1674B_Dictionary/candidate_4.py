import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[i + 1] for i in range(t)]


# --- clause: dictionary_index :: (word: bytes) -> int ---
def dictionary_index(word):
    first = word[0] - 97
    second = word[1] - 97
    base = first * 26 + second + 1
    return base - first - (1 if second > first else 0)


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(str(dictionary_index(word)))
    answer = "\n".join(out)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
