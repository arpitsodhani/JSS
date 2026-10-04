import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    
    rounds = []
    final_score = defaultdict(int)
    idx = 1
    
    for _ in range(n):
        name = data[idx]
        score = int(data[idx + 1])
        idx += 2
        
        rounds.append((name, score))
        final_score[name] += score
    
    best = max(final_score.values())
    candidates = {name for name, score in final_score.items() if score == best}
    
    current = defaultdict(int)
    for name, score in rounds:
        current[name] += score
        if name in candidates and current[name] >= best:
            print(name)
            return

if __name__ == "__main__":
    main()
