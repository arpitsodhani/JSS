import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append(data[2 + 2 * i].decode())
    return cases

# Clause alice_wins [Confidence: 1.00]
def alice_wins(s):
    core = s.lstrip("0").rstrip("1")
    i = 0
    while i < len(core):
        j = i
        while j < len(core) and core[j] == core[i]:
            j += 1
        if (j - i) % 2:
            return True
        i = j
    return False

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for s in read_input():
        collected.append("Alice" if alice_wins(s) else "Bob")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

