# CLAUSE: setup_environment
import random

RANKS = "6789TJQKA"
SUITS = "CDSH"

# CLAUSE: solve_logic
def solve():
    deck = [rank + suit for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    print(" ".join(deck[:18]))
    print(" ".join(deck[18:]))

# CLAUSE: finish_program
t = int(input())
for _ in range(t):
    solve()
