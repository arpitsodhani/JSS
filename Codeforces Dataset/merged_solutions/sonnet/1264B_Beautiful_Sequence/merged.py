import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return [int(token) for token in data[:4]]

# Clause try_start [Confidence: 1.00]
def try_start(counts, start):
    left = list(counts)
    if left[start] == 0:
        return None
    left[start] -= 1
    made = [start]
    cur = start
    while True:
        if cur > 0 and left[cur - 1] > 0:
            cur -= 1
        elif cur < 3 and left[cur + 1] > 0:
            cur += 1
        else:
            break
        left[cur] -= 1
        made.append(cur)
    if sum(left) == 0:
        return made
    return None

# Clause main [Confidence: 1.00]
def main():
    counts = read_input()
    for start in range(4):
        made = try_start(counts, start)
        if made is not None:
            sys.stdout.write("YES\n" + " ".join(map(str, made)) + "\n")
            return
    sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()

