import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [word.decode() for word in data[1:1 + t]]


# --- clause: rearrange :: (word: str) -> str ---
def rearrange(word):
    counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    if len(counts) == 1:
        return "-1"
    pieces = []
    for ch in sorted(counts):
        pieces.append(ch * counts[ch])
    return "".join(pieces)


# --- clause: main :: () -> None ---
def main():
    answers = []
    for word in read_input():
        answers.append(rearrange(word))
    sys.stdout.write("%s\n" % "\n".join(answers))


if __name__ == "__main__":
    main()
