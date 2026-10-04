import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [piece.decode() for piece in data[1:1 + t]]

# --- clause: fewest_operations :: (s: str) -> int ---
def fewest_operations(s):
    n = len(s)
    spots = [[] for _ in range(26)]
    for i, ch in enumerate(s):
        spots[ord(ch) - 97].append(i)
    best = n
    for places in spots:
        if not places:
            continue
        longest = places[0]
        previous = places[0]
        for pos in places[1:]:
            if pos - previous - 1 > longest:
                longest = pos - previous - 1
            previous = pos
        if n - previous - 1 > longest:
            longest = n - previous - 1
        steps = 0
        while longest:
            longest >>= 1
            steps += 1
        if steps < best:
            best = steps
    return best

# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(str(fewest_operations(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
