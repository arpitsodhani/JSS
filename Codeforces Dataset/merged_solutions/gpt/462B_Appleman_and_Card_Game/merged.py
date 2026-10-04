import sys

# CLAUSE: count_letter_frequencies
def count_letter_frequencies(cards):
    counts = [0] * 26
    for ch in cards:
        counts[ord(ch) - ord('A')] += 1
    return counts

# CLAUSE: order_counts_by_capacity
def order_counts_by_capacity(counts):
    return sorted(counts, reverse=True)

# CLAUSE: greedily_allocate_cards
def greedily_allocate_cards(ordered_counts, need):
    chosen = []
    for amount in ordered_counts:
        if need == 0:
            break
        take = min(amount, need)
        chosen.append(take)
        need -= take
    return chosen, need

# CLAUSE: compute_square_contribution
def compute_square_contribution(x):
    return x * x

# CLAUSE: track_remaining_selection
def track_remaining_selection(remaining):
    return remaining

# CLAUSE: accumulate_maximum_score
def accumulate_maximum_score(chosen):
    total = 0
    for x in chosen:
        total += compute_square_contribution(x)
    return total

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    cards = data[2]
    counts = count_letter_frequencies(cards)
    ordered = order_counts_by_capacity(counts)
    chosen, remaining = greedily_allocate_cards(ordered, k)
    track_remaining_selection(remaining)
    print(accumulate_maximum_score(chosen))

if __name__ == "__main__":
    main()
