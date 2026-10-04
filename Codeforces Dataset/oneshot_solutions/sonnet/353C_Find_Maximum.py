import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    s = data[1 + n].strip()
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    
    higher = 0
    answer = 0
    
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            answer = max(answer, higher + prefix[i])
            higher += a[i]
    
    answer = max(answer, higher)
    print(answer)

if __name__ == "__main__":
    main()
