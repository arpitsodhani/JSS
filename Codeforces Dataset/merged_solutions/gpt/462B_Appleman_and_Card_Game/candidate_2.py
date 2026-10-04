import sys
from collections import Counter

# CLAUSE: count_letter_frequencies
def count_letter_frequencies(cards):
    return Counter(cards)

# CLAUSE: order_counts_by_capacity
def order_counts_by_capacity(frequencies):
    values = list(frequencies.values())
    values.sort(reverse=True)
    return values

# CLAUSE: greedily_allocate_cards
def greedily_allocate_cards(capacities, k):
    allocations = []
    remaining = k
    index = 0
    while index < len(capacities) and remaining > 0:
        current = capacities[index]
        used = current if current <= remaining else remaining
        allocations.append(used)
        remaining = track_remaining_selection(remaining, used)
        index += 1
    return allocations

# CLAUSE: compute_square_contribution
def compute_square_contribution(x):
    return pow(x, 2)

# CLAUSE: track_remaining_selection
def track_remaining_selection(remaining, used):
    return remaining - used

# CLAUSE: accumulate_maximum_score
def accumulate_maximum_score(allocations):
    return sum(compute_square_contribution(x) for x in allocations)

def main():
    tokens = sys.stdin.read().split()
    k = int(tokens[1])
    cards = tokens[2]
    frequencies = count_letter_frequencies(cards)
    capacities = order_counts_by_capacity(frequencies)
    allocations = greedily_allocate_cards(capacities, k)
    answer = accumulate_maximum_score(allocations)
    sys.stdout.write(str(answer))

if __name__ == "__main__":
    main()
