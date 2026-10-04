import sys

def main():
    data = sys.stdin.read().split()
    
    if len(data) == 1:
        s = data[0]
        n = len(s) // 2
        a = s[:n]
        b = s[n:]
    else:
        a, b = data[0], data[1]
    
    four_to_seven = 0
    seven_to_four = 0
    
    for x, y in zip(a, b):
        if x == '4' and y == '7':
            four_to_seven += 1
        elif x == '7' and y == '4':
            seven_to_four += 1
    
    print(max(four_to_seven, seven_to_four))

if __name__ == "__main__":
    main()
