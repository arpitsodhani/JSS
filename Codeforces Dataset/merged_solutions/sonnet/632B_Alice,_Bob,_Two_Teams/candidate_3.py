import sys


# --- clause: read_input :: () -> tuple[int, list[int], bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    strength = []
    for token in data[1:n + 1]:
        strength.append(int(token))
    teams = data[n + 1]
    return n, strength, teams


# --- clause: prefix_sums :: (n: int, strength: list[int], teams: bytes) -> tuple[list[int], list[int]] ---
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


# --- clause: best_strength :: (n: int, alice: list[int], bob: list[int]) -> int ---
def best_strength(n, alice, bob):
    total_a = alice[n]
    total_b = bob[n]
    best = total_b
    i = 0
    while i <= n:
        prefix_gain = alice[i] + total_b - bob[i]
        suffix_gain = bob[i] + total_a - alice[i]
        if best < prefix_gain:
            best = prefix_gain
        if best < suffix_gain:
            best = suffix_gain
        i += 1
    return best


# --- clause: main :: () -> None ---
def main():
    n, strength, teams = read_input()
    alice, bob = prefix_sums(n, strength, teams)
    print(best_strength(n, alice, bob))


if __name__ == "__main__":
    main()
