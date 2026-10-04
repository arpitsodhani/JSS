import sys

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

def solve(n, k, a):
    if k == 0:
        return sum(a)
    
    seen = {tuple(a): 0}
    states = [a[:]]
    
    for step in range(1, k + 1):
        new_a = []
        for i in range(n):
            others = a[:i] + a[i+1:]
            new_a.append(mex(set(others)))
        a = new_a
        
        state = tuple(a)
        if state in seen:
            cycle_start = seen[state]
            cycle_length = step - cycle_start
            final_idx = cycle_start + (k - cycle_start) % cycle_length
            return sum(states[final_idx])
        
        seen[state] = step
        states.append(a[:])
    
    return sum(a)

def main():
    input_data = sys.stdin.buffer.read().decode('utf-8')
    data = input_data.split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
        results.append(solve(n, k, a))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
