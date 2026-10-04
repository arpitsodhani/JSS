import sys
import heapq

# CLAUSE: count_letter_frequencies
def count_letter_frequencies(cards):
    table = {}
    for ch in cards:
        if ch in table:
            table[ch] += 1
        else:
            table[ch] = 1
    return table

# CLAUSE: order_counts_by_capacity
def order_counts_by_capacity(table):
    heap = []
    for count in table.values():
        heapq.heappush(heap, -count)
    return heap

# CLAUSE: greedily_allocate_cards
def greedily_allocate_cards(heap, need):
    chosen_amounts = []
    remaining = need
    while heap and remaining:
        capacity = -heapq.heappop(heap)
        chosen = min(capacity, remaining)
        chosen_amounts.append(chosen)
        remaining = track_remaining_selection(remaining, chosen)
    return chosen_amounts

# CLAUSE: compute_square_contribution
def compute_square_contribution(x):
    return x * x

# CLAUSE: track_remaining_selection
def track_remaining_selection(remaining, chosen):
    return remaining - chosen

# CLAUSE: accumulate_maximum_score
def accumulate_maximum_score(chosen_amounts):
    total = 0
    for chosen in chosen_amounts:
        total += compute_square_contribution(chosen)
    return total

def main():
    data = sys.stdin.read().split()
    k = int(data[1])
    cards = data[2]
    table = count_letter_frequencies(cards)
    heap = order_counts_by_capacity(table)
    chosen_amounts = greedily_allocate_cards(heap, k)
    print(accumulate_maximum_score(chosen_amounts))

if __name__ == "__main__":
    main()
