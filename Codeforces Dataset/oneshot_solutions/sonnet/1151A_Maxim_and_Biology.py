n = int(input())
s = input()

target = "ACTG"

def min_distance(c1, c2):
    # Calculate minimum circular distance between two characters
    forward = (ord(c2) - ord(c1)) % 26
    backward = (ord(c1) - ord(c2)) % 26
    return min(forward, backward)

min_cost = float('inf')

# Try each possible starting position for "ACTG"
for i in range(n - 3):
    cost = 0
    for j in range(4):
        cost += min_distance(s[i + j], target[j])
    min_cost = min(min_cost, cost)

print(min_cost)
