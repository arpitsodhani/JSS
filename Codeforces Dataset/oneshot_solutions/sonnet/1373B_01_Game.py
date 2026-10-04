import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    result = []
    for i in range(1, t + 1):
        s = data[i]
        moves = min(s.count('0'), s.count('1'))
        result.append("DA" if moves % 2 == 1 else "NET")
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
