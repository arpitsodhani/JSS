import sys

def main():
    data = sys.stdin.read().split()
    n, m, x, y, z, p = map(int, data[:6])
    
    candies = []
    idx = 6
    for _ in range(p):
        candies.append((int(data[idx]), int(data[idx+1])))
        idx += 2
    
    # Reduce rotations
    x %= 4
    y %= 2
    z %= 4
    
    # Current dimensions
    h, w = n, m
    
    # Apply x clockwise rotations
    for _ in range(x):
        candies = [(j, h + 1 - i) for i, j in candies]
        h, w = w, h
    
    # Apply y horizontal flips
    if y:
        candies = [(i, w + 1 - j) for i, j in candies]
    
    # Apply z counterclockwise rotations
    for _ in range(z):
        candies = [(w + 1 - j, i) for i, j in candies]
        h, w = w, h
    
    # Output
    for i, j in candies:
        print(i, j)

main()
