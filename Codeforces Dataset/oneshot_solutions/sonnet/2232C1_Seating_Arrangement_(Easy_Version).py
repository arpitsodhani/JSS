import sys

def solve():
    line = sys.stdin.readline().split()
    n, x, s = int(line[0]), int(line[1]), int(line[2])
    friends = sys.stdin.readline().strip()
    
    # Count of tables at each occupancy level
    count = [0] * (s + 1)
    count[0] = x  # Initially all tables are empty
    
    seated = 0
    
    for friend in friends:
        if friend == 'I':
            # Need an empty table
            if count[0] > 0:
                count[0] -= 1
                count[1] += 1
                seated += 1
        elif friend == 'E':
            # Need a non-empty table with space
            for i in range(1, s):
                if count[i] > 0:
                    count[i] -= 1
                    count[i + 1] += 1
                    seated += 1
                    break
        else:  # 'A'
            # Prefer non-empty tables to preserve empty ones
            found = False
            for i in range(1, s):
                if count[i] > 0:
                    count[i] -= 1
                    count[i + 1] += 1
                    seated += 1
                    found = True
                    break
            if not found and count[0] > 0:
                count[0] -= 1
                count[1] += 1
                seated += 1
    
    print(seated)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
