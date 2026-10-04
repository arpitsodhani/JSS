import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [piece.decode() for piece in data[1:1 + t]]

# Clause fewest_operations [Confidence: 0.80]
def fewest_operations(s):
    n = len(s)
    best = n
    for code in range(26):
        letter = chr(97 + code)
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

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        out.append(str(fewest_operations(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

