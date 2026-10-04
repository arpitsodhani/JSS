import sys
from math import gcd

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    t = data[0]
    idx = 1
    answers = []
    
    for _ in range(t):
        l = data[idx]
        r = data[idx + 1]
        G = data[idx + 2]
        idx += 3
        
        left = (l + G - 1) // G
        right = r // G
        
        if left > right:
            answers.append("-1 -1")
            continue
        
        best_a = -1
        best_b = -1
        best_dist = -1
        
        limit = min(200, right - left + 1)
        
        for x in range(left, left + limit):
            for y in range(right, right - limit, -1):
                if y < x:
                    continue
                
                dist = y - x
                if dist < best_dist:
                    break
                
                if gcd(x, y) == 1:
                    if dist > best_dist or (dist == best_dist and x < best_a):
                        best_dist = dist
                        best_a = x
                        best_b = y
                    break
        
        if best_a == -1:
            answers.append("-1 -1")
        else:
            answers.append(f"{best_a * G} {best_b * G}")
    
    print("\n".join(answers))

if __name__ == "__main__":
    main()
