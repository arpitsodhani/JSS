import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    x = int(data[1])
    a = list(map(int, data[2:]))
    
    before = 0
    during = 0
    after = 0
    answer = 0
    
    for value in a:
        multiplied = value * x
        
        new_before = max(0, before + value)
        new_during = max(before + multiplied, during + multiplied)
        new_after = max(during + value, after + value)
        
        before = new_before
        during = new_during
        after = new_after
        
        answer = max(answer, before, during, after)
    
    print(answer)

if __name__ == "__main__":
    main()
