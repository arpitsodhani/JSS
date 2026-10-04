import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    return [numbers[1 + i].decode() for i in range(t)]


# --- clause: pick_positions :: (s: str) -> list[int] ---
def pick_positions(s):
    picked = []
    letters = list(s)
    for i in range(len(letters) - 2):
        window = "".join(letters[i:i + 3])
        if window != "one" and window != "two":
            continue
        if window == "two" and "".join(letters[i:i + 5]) == "twone":
            picked.append(i + 3)
            letters[i + 2] = "."
        elif window == "one":
            picked.append(i + 2)
            letters[i + 1] = "."
        else:
            picked.append(i + 2)
            letters[i + 1] = "."
    return picked


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for s in read_input():
        picked = pick_positions(s)
        pieces.append(str(len(picked)))
        pieces.append(" ".join(str(p) for p in picked))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
