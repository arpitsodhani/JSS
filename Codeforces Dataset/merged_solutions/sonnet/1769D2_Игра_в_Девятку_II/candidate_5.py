# CLAUSE: setup_environment
import random

# CLAUSE: solve_logic
def solve():
    deck = []
    for rank in range(9):
        for suit in range(4):
            deck.append("6789TJQKA"[rank] + "CDSH"[suit])
    random.shuffle(deck)
    lines = [" ".join(deck[:18]), " ".join(deck[18:])]
    print("\n".join(lines))

# CLAUSE: finish_program
tests = int(input())
answers_done = 0
while answers_done < tests:
    solve()
    answers_done += 1
