# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    
    laptops = []
    idx = 1
    for i in range(n):
        speed = data[idx]
        ram = data[idx + 1]
        hdd = data[idx + 2]
        price = data[idx + 3]
        idx += 4
        laptops.append((speed, ram, hdd, price, i + 1))
    
    best_price = 10**18
    answer = -1
    
    for i in range(n):
        outdated = False
        s1, r1, h1, p1, id1 = laptops[i]
        
        for j in range(n):
            s2, r2, h2, _, _ = laptops[j]
            if s1 < s2 and r1 < r2 and h1 < h2:
                outdated = True
                break
        
        if not outdated and p1 < best_price:
            best_price = p1
            answer = id1
    
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
