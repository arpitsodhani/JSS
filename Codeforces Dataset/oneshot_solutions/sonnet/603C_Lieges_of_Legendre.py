import sys

def grundy_odd_k(x):
    if x == 0:
        return 0
    
    if x % 2 == 1:
        return 1 if x % 4 == 1 else 0
    
    half = x // 2
    if half % 2 == 1:
        return 2
    
    return 1 if grundy_odd_k(half) == 0 else 2

def grundy_even_k(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x % 2 == 1:
        return 0
    return 1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    k = data[1]
    piles = data[2:2 + n]
    
    xor_sum = 0
    if k % 2 == 0:
        for pile in piles:
            xor_sum ^= grundy_even_k(pile)
    else:
        for pile in piles:
            xor_sum ^= grundy_odd_k(pile)
    
    print("Kevin" if xor_sum else "Nicky")

if __name__ == "__main__":
    main()
