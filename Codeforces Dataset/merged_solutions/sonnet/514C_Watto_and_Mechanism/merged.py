import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    stored = [data[2 + i].decode() for i in range(n)]
    asked = [data[2 + n + i].decode() for i in range(m)]
    return stored, asked

# Clause memory_hashes [Confidence: 1.00]
def memory_hashes(stored, base, mod):
    memory = {}
    for word in stored:
        element = 0
        for ch in word:
            element = (element * base + ord(ch) - 96) % mod
        length_of = len(word)
        if length_of not in memory:
            memory[length_of] = set()
        memory[length_of].add(element)
    return memory

# Clause has_neighbour [Confidence: 0.80]
def has_neighbour(word, memory, base, mod):
    length_of = len(word)
    if length_of not in memory:
        return False
    known = memory[length_of]
    element = 0
    for ch in word:
        element = (element * base + ord(ch) - 96) % mod
    power = 1
    for i in range(length_of - 1, -1, -1):
        here = ord(word[i]) - 96
        for other in (1, 2, 3):
            if other == here:
                continue
            changed = (element + (other - here) * power) % mod
            if changed in known:
                return True
        power = power * base % mod
    return False

# Clause main [Confidence: 1.00]
def main():
    stored, asked = read_input()
    base = 131
    mod = (1 << 61) - 1
    memory = memory_hashes(stored, base, mod)
    out = []
    for word in asked:
        out.append("YES" if has_neighbour(word, memory, base, mod) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

