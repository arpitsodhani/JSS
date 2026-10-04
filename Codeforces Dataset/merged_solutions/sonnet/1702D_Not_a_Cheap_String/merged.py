import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i].decode(), int(data[2 + 2 * i])))
    return cases

# Clause trim_word [Confidence: 0.80]
def trim_word(word, budget):
    price = 0
    for ch in word:
        price += ord(ch) - 96
    if price <= budget:
        return word
    arranged = sorted(range(len(word)), key=lambda i: -(ord(word[i]) - 96))
    dropped = [False] * len(word)
    for spot in arranged:
        if price <= budget:
            break
        price -= ord(word[spot]) - 96
        dropped[spot] = True
    kept = []
    for i in range(len(word)):
        if not dropped[i]:
            kept.append(word[i])
    return "".join(kept)

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for word, budget in read_input():
        lines.append(trim_word(word, budget))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

