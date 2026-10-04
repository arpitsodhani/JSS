import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause reachable [Confidence: 0.80]
def reachable(a):
    running = 0
    done = False
    for entry in a:
        running += entry
        if running < 0:
            return False
        if done and entry != 0:
            return False
        if running == 0:
            done = True
    return running == 0

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append("Yes" if reachable(a) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

