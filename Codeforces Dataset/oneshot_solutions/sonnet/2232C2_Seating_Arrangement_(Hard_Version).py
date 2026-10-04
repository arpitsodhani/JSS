def solve():
    x, s, t = map(int, input().split())
    line = input().strip()
    
    # count[i] = number of tables with i people
    count = [0] * (s + 1)
    count[0] = x
    
    seated = 0
    for person in line:
        if person == 'I':
            # Need an empty table
            if count[0] > 0:
                count[0] -= 1
                count[1] += 1
                seated += 1
        elif person == 'E':
            # Need a non-empty, non-full table (prefer most occupied)
            for i in range(s - 1, 0, -1):
                if count[i] > 0:
                    count[i] -= 1
                    count[i + 1] += 1
                    seated += 1
                    break
        else:  # 'A'
            # Prefer empty tables to create more non-empty tables
            if count[0] > 0:
                count[0] -= 1
                count[1] += 1
                seated += 1
            else:
                # If no empty tables, use non-empty (prefer most occupied)
                for i in range(s - 1, 0, -1):
                    if count[i] > 0:
                        count[i] -= 1
                        count[i + 1] += 1
                        seated += 1
                        break
    
    return seated

num_tests = int(input())
for _ in range(num_tests):
    print(solve())
