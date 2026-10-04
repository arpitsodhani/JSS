import sys
from math import isqrt

def wythoff_losing(a, b):
    if a > b:
        a, b = b, a
    
    d = b - a
    if d == 0:
        return a == 0
    
    floor_d_sqrt5 = isqrt(5 * d * d)
    lower = (d + floor_d_sqrt5) // 2
    return a == lower

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    a = data[1:1 + n]
    
    if n == 1:
        print("BitLGM" if a[0] > 0 else "BitAryo")
    elif n == 2:
        print("BitAryo" if wythoff_losing(a[0], a[1]) else "BitLGM")
    else:
        xor_sum = 0
        for x in a:
            xor_sum ^= x
        print("BitAryo" if xor_sum == 0 else "BitLGM")

if __name__ == "__main__":
    main()
