import sys
from collections import defaultdict

def factorial(n):
    if n > 20:
        return 10**20
    result = 1
    for i in range(2, n + 1):
        result *= i
        if result > 10**18:
            return 10**20
    return result

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    S = int(data[2])
    cubes = [int(data[i]) for i in range(3, 3 + n)]
    
    # Precompute factorials
    fact = {val: factorial(val) for val in set(cubes)}
    
    # Split into two halves
    mid = n // 2
    left = cubes[:mid]
    right = cubes[mid:]
    
    # Generate all states for left half
    left_states = defaultdict(int)
    for mask in range(1 << len(left)):
        indices = [i for i in range(len(left)) if mask & (1 << i)]
        for fact_mask in range(1 << len(indices)):
            total = 0
            factorials_used = 0
            for j, idx in enumerate(indices):
                if fact_mask & (1 << j):
                    total += fact[left[idx]]
                    factorials_used += 1
                else:
                    total += left[idx]
                if total > S:
                    break
            else:
                if factorials_used <= k:
                    left_states[(total, factorials_used)] += 1
    
    # Match with right half
    answer = 0
    for mask in range(1 << len(right)):
        indices = [i for i in range(len(right)) if mask & (1 << i)]
        for fact_mask in range(1 << len(indices)):
            total = 0
            factorials_used = 0
            for j, idx in enumerate(indices):
                if fact_mask & (1 << j):
                    total += fact[right[idx]]
                    factorials_used += 1
                else:
                    total += right[idx]
                if total > S:
                    break
            else:
                if factorials_used <= k:
                    needed = S - total
                    for left_fact in range(k - factorials_used + 1):
                        answer += left_states.get((needed, left_fact), 0)
    
    # Subtract empty subset case
    if S == 0:
        answer -= 1
    
    print(answer)

if __name__ == "__main__":
    main()
