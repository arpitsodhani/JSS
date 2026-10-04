import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        candies = data[idx:idx + n]
        idx += n
        
        smallest = min(candies)
        answers.append(str(sum(c - smallest for c in candies)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
