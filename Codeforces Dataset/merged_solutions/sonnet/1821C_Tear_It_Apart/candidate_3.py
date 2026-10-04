import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [piece.decode() for piece in data[1:1 + t]]

# --- clause: fewest_operations :: (s: str) -> int ---
def fewest_operations(s):
    n = len(s)
    answer = n
    for code in range(26):
        letter = chr(97 + code)
        if letter not in s:
            continue
        gap = 0
        worst = 0
        for ch in s:
            if ch == letter:
                gap = 0
            else:
                gap += 1
                if gap > worst:
                    worst = gap
        steps = 0
        while worst:
            worst //= 2
            steps += 1
        if steps < answer:
            answer = steps
    return answer

# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(str(fewest_operations(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
