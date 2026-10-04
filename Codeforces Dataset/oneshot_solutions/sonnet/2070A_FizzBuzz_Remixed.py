import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    ans = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        ans.append(str((n // 15) * 3 + min(n % 15 + 1, 3)))
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
