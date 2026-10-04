import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    base = "9890123456789"
    result = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        if n == 1:
            result.append("9")
        else:
            s = "98"
            digit = 9
            for _ in range(3, n + 1):
                s += str(digit)
                digit = (digit + 1) % 10
            result.append(s)
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
