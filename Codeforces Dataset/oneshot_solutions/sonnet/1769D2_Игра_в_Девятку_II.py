import random

def solve():
    ranks = '6789TJQKA'
    suits = 'CDSH'
    
    # Create deck of all 36 cards
    deck = [r + s for r in ranks for s in suits]
    
    # Shuffle the deck
    random.shuffle(deck)
    
    # Deal 18 cards to each player
    print(' '.join(deck[:18]))
    print(' '.join(deck[18:]))

n = int(input())
for _ in range(n):
    solve()
