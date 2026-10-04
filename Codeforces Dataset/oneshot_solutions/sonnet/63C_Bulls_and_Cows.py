import sys
from itertools import permutations

def score(secret, guess):
    bulls = 0
    common = 0
    
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
    
    secret_set = set(secret)
    for ch in guess:
        if ch in secret_set:
            common += 1
    
    return bulls, common - bulls

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    idx = 1
    
    guesses = []
    for _ in range(n):
        guess = data[idx]
        bulls = int(data[idx + 1])
        cows = int(data[idx + 2])
        idx += 3
        guesses.append((guess, bulls, cows))
    
    possible = []
    for p in permutations("0123456789", 4):
        secret = ''.join(p)
        ok = True
        
        for guess, bulls, cows in guesses:
            if score(secret, guess) != (bulls, cows):
                ok = False
                break
        
        if ok:
            possible.append(secret)
            if len(possible) > 1:
                break
    
    if len(possible) == 0:
        print("Incorrect data")
    elif len(possible) == 1:
        print(possible[0])
    else:
        print("Need more data")

if __name__ == "__main__":
    main()
