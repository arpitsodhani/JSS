import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]

# Clause kicks_taken [Confidence: 1.00]
def kicks_taken(s, choice):
    goals = [0, 0]
    begin = [5, 5]
    bit = 0
    for i in range(10):
        side = i % 2
        if s[i] == "?":
            scored = (choice >> bit) & 1
            bit += 1
        else:
            scored = 1 if s[i] == "1" else 0
        goals[side] += scored
        begin[side] -= 1
        if goals[0] > goals[1] + begin[1] or goals[1] > goals[0] + begin[0]:
            return i + 1
    return 10

# Clause fewest_kicks [Confidence: 1.00]
def fewest_kicks(s):
    unknown = 0
    for ch in s:
        if ch == "?":
            unknown += 1
    best = 10
    for choice in range(1 << unknown):
        here = kicks_taken(s, choice)
        if here < best:
            best = here
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        out.append(fewest_kicks(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

