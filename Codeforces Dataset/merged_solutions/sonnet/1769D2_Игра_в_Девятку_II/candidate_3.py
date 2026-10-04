# CLAUSE: setup_environment
from random import sample

# CLAUSE: solve_logic
def make_deck():
    cards = []
    for rank in "6789TJQKA":
        for suit in "CDSH":
            cards.append(rank + suit)
    return cards

def solve():
    shuffled = sample(make_deck(), 36)
    first = shuffled[:18]
    second = shuffled[18:36]
    print(*first)
    print(*second)

# CLAUSE: finish_program
for _ in range(int(input())):
    solve()
