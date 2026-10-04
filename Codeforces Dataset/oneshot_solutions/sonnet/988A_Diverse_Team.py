import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    k = data[1]
    ratings = data[2:]
    
    seen = set()
    result = []
    
    for i, rating in enumerate(ratings, 1):
        if rating not in seen:
            seen.add(rating)
            result.append(i)
            if len(result) == k:
                break
    
    if len(result) < k:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))

main()
