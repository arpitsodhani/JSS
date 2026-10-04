# CLAUSE: setup_environment
import random

CARDS = tuple(a + b for a in "6789TJQKA" for b in "CDSH")

# CLAUSE: solve_logic
def deal_once():
    deck = list(CARDS)
    for i in range(35, 0, -1):
        j = random.randrange(i + 1)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

def solve():
    deck = deal_once()
    print(" ".join(deck[i] for i in range(18)))
    print(" ".join(deck[i] for i in range(18, 36)))

# CLAUSE: finish_program
count = int(input())
while count:
    solve()
    count -= 1
