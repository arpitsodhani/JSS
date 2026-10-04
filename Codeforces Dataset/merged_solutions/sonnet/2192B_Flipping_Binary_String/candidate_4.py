import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    return [numbers[2 + 2 * i].decode() for i in range(t)]


# --- clause: choose_indices :: (s: str) -> list[int] | None ---
def choose_indices(s):
    ones = s.count("1")
    if ones % 2 == 0:
        wanted = "1"
    elif (len(s) - ones) % 2 == 1:
        wanted = "0"
    else:
        return None
    picked = []
    i = 0
    while i < len(s):
        if s[i] == wanted:
            picked.append(i + 1)
        i += 1
    return picked


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for s in read_input():
        picked = choose_indices(s)
        if picked is None:
            pieces.append("-1")
        else:
            pieces.append(str(len(picked)))
            pieces.append(" ".join(map(str, picked)))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
