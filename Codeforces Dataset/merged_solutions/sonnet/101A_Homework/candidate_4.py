import sys


# --- clause: read_input :: () -> tuple[str, int] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[0].decode(), int(numbers[1])


# --- clause: pick_dropped :: (word: str, k: int) -> set[str] ---
def pick_dropped(word, k):
    tally = [0] * 26
    for ch in word:
        tally[ord(ch) - 97] += 1
    order = sorted(range(26), key=lambda i: tally[i])
    dropped = set()
    for letter in order:
        times = tally[letter]
        if times and times <= k:
            k -= times
            dropped.add(chr(letter + 97))
    return dropped


# --- clause: main :: () -> None ---
def main():
    word, k = read_input()
    dropped = pick_dropped(word, k)
    kept = "".join(ch for ch in word if ch not in dropped)
    left = set(kept)
    sys.stdout.write("%d\n%s\n" % (len(left), kept))


if __name__ == "__main__":
    main()
