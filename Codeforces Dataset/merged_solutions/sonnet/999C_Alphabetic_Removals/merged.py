import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[1]), data[2].decode()

# Clause removal_budget [Confidence: 1.00]
def removal_budget(k, s):
    buckets = [0] * 26
    for ch in s:
        buckets[ord(ch) - 97] += 1
    budget = [0] * 26
    for letter in range(26):
        take = buckets[letter] if buckets[letter] < k else k
        budget[letter] = take
        k -= take
        if k == 0:
            break
    return budget

# Clause strip_letters [Confidence: 1.00]
def strip_letters(s, budget):
    kept = []
    for ch in s:
        letter = ord(ch) - 97
        if budget[letter]:
            budget[letter] -= 1
        else:
            kept.append(ch)
    return "".join(kept)

# Clause main [Confidence: 1.00]
def main():
    k, s = read_input()
    sys.stdout.write(strip_letters(s, removal_budget(k, s)) + "\n")


if __name__ == "__main__":
    main()

