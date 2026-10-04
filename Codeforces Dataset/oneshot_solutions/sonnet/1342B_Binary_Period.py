import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    result = []
    
    for i in range(1, t + 1):
        s = data[i]
        if '0' not in s or '1' not in s:
            result.append(s)
        else:
            result.append('01' * len(s))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
