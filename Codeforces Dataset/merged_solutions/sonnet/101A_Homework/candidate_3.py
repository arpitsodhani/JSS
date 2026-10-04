import sys


# --- clause: read_input :: () -> tuple[str, int] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return fields[0].decode(), int(fields[1])


# --- clause: pick_dropped :: (word: str, k: int) -> set[str] ---
def pick_dropped(word, k):
    occurrences = {}
    for ch in word:
        occurrences[ch] = occurrences.get(ch, 0) + 1
    dropped = set()
    for ch, times in sorted(occurrences.items(), key=lambda row: row[1]):
        if times <= k:
            k -= times
            dropped.add(ch)
    return dropped


# --- clause: main :: () -> None ---
def main():
    word, k = read_input()
    dropped = pick_dropped(word, k)
    kept = "".join(ch for ch in word if ch not in dropped)
    start = set(kept)
    sys.stdout.write("%d\n%s\n" % (len(start), kept))


if __name__ == "__main__":
    main()
