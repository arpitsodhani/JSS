import sys

def main():
    data = sys.stdin.read().split()
    a = int(data[0])
    b = int(data[1])
    
    while a and b:
        if a >= 2 * b:
            a %= 2 * b
        elif b >= 2 * a:
            b %= 2 * a
        else:
            break
    
    print(a, b)

main()
