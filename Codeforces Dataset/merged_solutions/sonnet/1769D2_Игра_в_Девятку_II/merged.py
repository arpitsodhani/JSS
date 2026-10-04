# Clause setup_environment [Confidence: 0.40]
import random


# Clause solve_logic [Confidence: 0.20]
def solve():
    deck = []
    for rank in range(9):
        for suit in range(4):
            deck.append("6789TJQKA"[rank] + "CDSH"[suit])
    random.shuffle(deck)
    lines = [" ".join(deck[:18]), " ".join(deck[18:])]
    print("\n".join(lines))


# Clause finish_program [Confidence: 0.40]
for _ in range(int(input())):
    solve()


