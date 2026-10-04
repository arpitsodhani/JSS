import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    strength = [int(token) for token in data[1:n + 1]]
    teams = data[n + 1]
    return n, strength, teams

# Clause prefix_sums [Confidence: 1.00]
def prefix_sums(n, strength, teams):
    alice = [0] * (n + 1)
    bob = [0] * (n + 1)
    for i in range(n):
        alice[i + 1] = alice[i]
        bob[i + 1] = bob[i]
        if teams[i] == 65:
            alice[i + 1] += strength[i]
        else:
            bob[i + 1] += strength[i]
    return alice, bob

# Clause best_strength [Confidence: 1.00]
def best_strength(n, alice, bob):
    total_a = alice[n]
    total_b = bob[n]
    best = total_b
    for i in range(n + 1):
        flipped_prefix = alice[i] + total_b - bob[i]
        if flipped_prefix > best:
            best = flipped_prefix
        flipped_suffix = bob[i] + total_a - alice[i]
        if flipped_suffix > best:
            best = flipped_suffix
    return best

# Clause main [Confidence: 1.00]
def main():
    n, strength, teams = read_input()
    alice, bob = prefix_sums(n, strength, teams)
    sys.stdout.write(str(best_strength(n, alice, bob)) + "\n")


if __name__ == "__main__":
    main()

