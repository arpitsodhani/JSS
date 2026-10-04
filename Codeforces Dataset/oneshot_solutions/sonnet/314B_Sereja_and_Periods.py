def solve():
    b, d = map(int, input().split())
    a = input().strip()
    c = input().strip()
    
    # Check if all characters of c exist in a
    if not set(c).issubset(set(a)):
        print(0)
        return
    
    # Precompute transitions: for each start position in a,
    # where do we end after matching c once?
    transition = [None] * len(a)
    
    for start_pos in range(len(a)):
        pos = start_pos
        a_consumed = 0
        
        for char in c:
            found = False
            # Search for char, possibly wrapping to next copy of a
            for _ in range(len(a) + 1):
                if pos < len(a) and a[pos] == char:
                    pos += 1
                    found = True
                    break
                pos += 1
                if pos >= len(a):
                    a_consumed += 1
                    pos = 0
            
            if not found:
                break
        else:
            # Successfully matched c
            while pos >= len(a):
                a_consumed += 1
                pos -= len(a)
            transition[start_pos] = (pos, a_consumed)
    
    # Simulate with cycle detection
    c_matched = 0
    a_used = 0
    current_pos = 0
    visited = {}
    
    while a_used < b:
        if current_pos in visited:
            # Cycle detected
            prev_c, prev_a = visited[current_pos]
            delta_c = c_matched - prev_c
            delta_a = a_used - prev_a
            
            remaining_a = b - a_used
            full_cycles = remaining_a // delta_a
            
            c_matched += full_cycles * delta_c
            a_used += full_cycles * delta_a
            
            if a_used >= b:
                break
            
            visited.clear()
        
        visited[current_pos] = (c_matched, a_used)
        
        if transition[current_pos] is None:
            break
        
        next_pos, a_needed = transition[current_pos]
        if a_used + a_needed > b:
            break
        
        c_matched += 1
        a_used += a_needed
        current_pos = next_pos
    
    print(c_matched // d)

solve()
