import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    skills = [int(data[i+2]) for i in range(n)]
    
    while k > 0:
        # Find skill with minimum cost to reach next threshold
        best_idx = -1
        best_cost = float('inf')
        
        for i in range(n):
            if skills[i] >= 100:
                continue
            
            # Calculate cost to next multiple of 10 (or 100 if closer)
            current_tier = skills[i] // 10
            next_threshold = min((current_tier + 1) * 10, 100)
            cost = next_threshold - skills[i]
            
            if cost < best_cost:
                best_cost = cost
                best_idx = i
        
        # Stop if no skill can be improved or not enough units
        if best_idx == -1 or best_cost > k:
            break
        
        # Apply improvement
        skills[best_idx] += best_cost
        k -= best_cost
    
    # Calculate total rating
    rating = sum(skill // 10 for skill in skills)
    print(rating)

main()
