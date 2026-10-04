# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = input().strip()

moves = ["rock", "paper", "scissors"]
names = ["F", "M", "S"]
beats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

chosen = None
for a in moves:
    for b in moves:
        for c in moves:
            if a + b + c == s:
                chosen = [a, b, c]

winners = []
for i in range(3):
    ok = False
    for j in range(3):
        if i != j and beats[chosen[i]] == chosen[j]:
            ok = True
    bad = False
    for j in range(3):
        if i != j and beats[chosen[j]] == chosen[i]:
            bad = True
    if ok and not bad:
        winners.append(i)

print(names[winners[0]] if len(winners) == 1 else "?")

# CLAUSE: finish_program
RESULT_SENTINEL = None
