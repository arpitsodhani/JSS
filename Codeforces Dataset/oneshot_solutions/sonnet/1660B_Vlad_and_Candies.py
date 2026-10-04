import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        candies = list(map(int, data[idx:idx + n]))
        idx += n
        
        candies.sort()
        largest = candies[-1]
        second_largest = candies[-2] if n > 1 else 0
        
        if largest - second_largest <= 1:
            answers.append("YES")
        else:
            answers.append("NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
