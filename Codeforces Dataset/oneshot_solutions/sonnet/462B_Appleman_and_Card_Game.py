from collections import Counter

n, k = map(int, input().split())
cards = input().strip()

# Count frequency of each letter
freq = Counter(cards)

# Sort frequencies in descending order
frequencies = sorted(freq.values(), reverse=True)

# Greedily pick cards
total_coins = 0
remaining = k

for f in frequencies:
    if remaining == 0:
        break
    take = min(f, remaining)
    total_coins += take * take
    remaining -= take

print(total_coins)
