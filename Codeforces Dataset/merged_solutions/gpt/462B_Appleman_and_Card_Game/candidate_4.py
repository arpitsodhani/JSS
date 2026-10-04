import sys

# CLAUSE: count_letter_frequencies
def count_letter_frequencies(cards):
    counts = [0 for _ in range(26)]
    base = ord('A')
    for letter in cards:
        counts[ord(letter) - base] += 1
    return counts

# CLAUSE: order_counts_by_capacity
def order_counts_by_capacity(counts):
    ordered = counts[:]
    ordered.sort()
    ordered.reverse()
    return ordered

# CLAUSE: greedily_allocate_cards
def greedily_allocate_cards(ordered_counts, required):
    pieces = []
    remaining = required
    for capacity in ordered_counts:
        if capacity == 0 or remaining == 0:
            continue
        if capacity < remaining:
            pieces.append(capacity)
            remaining = track_remaining_selection(remaining, capacity)
        else:
            pieces.append(remaining)
            remaining = track_remaining_selection(remaining, remaining)
    return pieces

# CLAUSE: compute_square_contribution
def compute_square_contribution(x):
    return x * x

# CLAUSE: track_remaining_selection
def track_remaining_selection(remaining, chosen):
    return remaining - chosen

# CLAUSE: accumulate_maximum_score
def accumulate_maximum_score(pieces):
    answer = 0
    for chosen in pieces:
        answer = answer + compute_square_contribution(chosen)
    return answer

def main():
    raw = sys.stdin.buffer.read().split()
    k = int(raw[1])
    cards = raw[2].decode()
    counts = count_letter_frequencies(cards)
    ordered_counts = order_counts_by_capacity(counts)
    pieces = greedily_allocate_cards(ordered_counts, k)
    sys.stdout.write(str(accumulate_maximum_score(pieces)))

if __name__ == "__main__":
    main()
