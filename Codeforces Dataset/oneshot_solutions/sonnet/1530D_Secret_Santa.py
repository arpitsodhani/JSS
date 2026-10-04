import sys

def solve_case(n, wishes):
    assigned = [0] * (n + 1)
    used = [False] * (n + 1)
    
    for i in range(1, n + 1):
        target = wishes[i - 1]
        if target != i and not used[target]:
            assigned[i] = target
            used[target] = True
    
    free_people = []
    missing_targets = []
    
    for i in range(1, n + 1):
        if assigned[i] == 0:
            free_people.append(i)
        if not used[i]:
            missing_targets.append(i)
    
    m = len(free_people)
    
    if m == 1 and free_people[0] == missing_targets[0]:
        person = free_people[0]
        for i in range(1, n + 1):
            if assigned[i] != 0:
                assigned[person] = assigned[i]
                assigned[i] = person
                break
    else:
        bad = -1
        for i in range(m):
            if free_people[i] == missing_targets[i]:
                bad = i
                break
        
        if bad != -1:
            missing_targets[bad], missing_targets[(bad + 1) % m] = missing_targets[(bad + 1) % m], missing_targets[bad]
        
        for i in range(m):
            assigned[free_people[i]] = missing_targets[i]
    
    fulfilled = 0
    for i in range(1, n + 1):
        if assigned[i] == wishes[i - 1]:
            fulfilled += 1
    
    return fulfilled, assigned[1:]

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    output = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        wishes = list(map(int, data[idx:idx + n]))
        idx += n
        
        fulfilled, result = solve_case(n, wishes)
        output.append(str(fulfilled))
        output.append(' '.join(map(str, result)))
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
