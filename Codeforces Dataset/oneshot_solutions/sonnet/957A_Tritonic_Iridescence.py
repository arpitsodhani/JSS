n = int(input())
s = input().strip()

# Check if current fixed positions are valid
for i in range(n - 1):
    if s[i] != '?' and s[i+1] != '?' and s[i] == s[i+1]:
        print("No")
        exit()

colors = ['C', 'M', 'Y']

# dp[c] = number of ways to color up to current position, with current position colored as c
if s[0] == '?':
    dp = {c: 1 for c in colors}
else:
    dp = {s[0]: 1}

for i in range(1, n):
    new_dp = {}
    for prev_color, prev_ways in dp.items():
        if s[i] == '?':
            for color in colors:
                if color != prev_color:
                    new_dp[color] = new_dp.get(color, 0) + prev_ways
        else:
            if s[i] != prev_color:
                new_dp[s[i]] = new_dp.get(s[i], 0) + prev_ways
    
    dp = new_dp
    
    if not dp:
        print("No")
        exit()

total_ways = sum(dp.values())
print("Yes" if total_ways >= 2 else "No")
