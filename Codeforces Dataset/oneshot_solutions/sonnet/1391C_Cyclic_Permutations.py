n = int(input())
MOD = 10**9 + 7

# Compute n!
factorial = 1
for i in range(1, n + 1):
    factorial = (factorial * i) % MOD

# Compute 2^(n-1)
power_of_2 = pow(2, n - 1, MOD)

# Answer: n! - 2^(n-1)
answer = (factorial - power_of_2 + MOD) % MOD
print(answer)
