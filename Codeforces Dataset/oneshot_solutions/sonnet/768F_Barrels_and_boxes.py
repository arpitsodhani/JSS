f, w, h = map(int, input().split())
MOD = 10**9 + 7

# Precompute factorials and inverse factorials
MAX_N = f + w + 10
fact = [1] * MAX_N
for i in range(1, MAX_N):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * MAX_N
inv_fact[MAX_N-1] = pow(fact[MAX_N-1], MOD-2, MOD)
for i in range(MAX_N-2, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def C(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

total = 0
good = 0

# Iterate over number of stacks
for num_food in range(1, f+1):
    for num_wine in range(1, w+1):
        # Check if they can alternate
        if abs(num_food - num_wine) > 1:
            continue
        
        # Number of ways to arrange these stacks
        if num_food == num_wine:
            arrangements = 2  # Start with food or wine
        else:
            arrangements = 1  # Only one way to alternate
        
        # Ways to partition food
        ways_food = C(f-1, num_food-1)
        
        # Ways to partition wine (total)
        ways_wine_total = C(w-1, num_wine-1)
        
        # Ways to partition wine (all > h)
        ways_wine_good = C(w - num_wine * h - 1, num_wine - 1)
        
        total = (total + arrangements * ways_food % MOD * ways_wine_total % MOD) % MOD
        good = (good + arrangements * ways_food % MOD * ways_wine_good % MOD) % MOD

# Calculate probability
result = good * pow(total, MOD-2, MOD) % MOD
print(result)
