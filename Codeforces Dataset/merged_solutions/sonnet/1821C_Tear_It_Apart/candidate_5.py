import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [piece.decode() for piece in data[1:1 + t]]

# --- clause: fewest_operations :: (s: str) -> int ---
def fewest_operations(s):
    n = len(s)
    best = n
    for code in range(26):
        letter = chr(97 + code)
        worst = 0
        run = 0
        found = False
        for ch in s:
            if ch == letter:
                found = True
                if run > worst:
                    worst = run
                run = 0
            else:
                run += 1
        if not found:
            continue
        if run > worst:
            worst = run
        steps = 0
        while worst:
            worst //= 2
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
