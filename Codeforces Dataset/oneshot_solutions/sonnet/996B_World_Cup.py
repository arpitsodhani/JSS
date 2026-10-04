import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]
    
    best_time = 10 ** 30
    answer = 1
    
    for i in range(n):
        if a[i] <= i:
            time = i
        else:
            cycles = (a[i] - i + n - 1) // n
            time = i + cycles * n
        
        if time < best_time:
            best_time = time
            answer = i + 1
    
    print(answer)

if __name__ == "__main__":
    main()
