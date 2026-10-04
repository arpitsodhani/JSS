import sys

# CLAUSE: count_letter_frequencies
def count_letter_frequencies(cards):
    frequencies = {}
    for ch in cards:
        frequencies[ch] = frequencies.get(ch, 0) + 1
    return frequencies

# CLAUSE: order_counts_by_capacity
def order_counts_by_capacity(frequencies):
    return sorted(frequencies.values(), key=lambda x: -x)

# CLAUSE: greedily_allocate_cards
def greedily_allocate_cards(counts, required):
    selected = []
    remaining = required
    for count in counts:
        take = min(count, remaining)
        if take > 0:
            selected.append(take)
        remaining = track_remaining_selection(remaining, take)
        if remaining <= 0:
            break
    return selected

# CLAUSE: compute_square_contribution
def compute_square_contribution(x):
    return x ** 2

# CLAUSE: track_remaining_selection
def track_remaining_selection(remaining, take):
    return remaining - take

# CLAUSE: accumulate_maximum_score
def accumulate_maximum_score(selected):
    score = 0
    for take in selected:
        score += compute_square_contribution(take)
    return score

def main():
    first = sys.stdin.readline().split()
    n, k = map(int, first)
    cards = sys.stdin.readline().strip()
    frequencies = count_letter_frequencies(cards)
    counts = order_counts_by_capacity(frequencies)
    selected = greedily_allocate_cards(counts, k)
    print(accumulate_maximum_score(selected))

if __name__ == "__main__":
    main()
