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
    for code in range(97, 123):
        letter = chr(code)
        longest = 0
        run = 0
        for ch in s:
            if ch == letter:
                if run > longest:
                    longest = run
                run = 0
            else:
                run += 1
        if run > longest:
            longest = run
        if longest == n:
            continue
        steps = 0
        while longest:
            longest //= 2
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
