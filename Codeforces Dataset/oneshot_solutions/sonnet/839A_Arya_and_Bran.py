import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n, k = data[0], data[1]
    candies = data[2:]
    
    saved = 0
    given = 0
    
    for day in range(n):
        saved += candies[day]
        today = min(8, saved)
        saved -= today
        given += today
        
        if given >= k:
            print(day + 1)
            return
    
    print(-1)

if __name__ == "__main__":
    main()
