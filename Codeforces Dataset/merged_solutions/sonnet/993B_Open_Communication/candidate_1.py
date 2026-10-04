# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    first = []
    for _ in range(n):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        first.append((a, b))
    
    second = []
    for _ in range(m):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        second.append((a, b))
    
    possible = []
    for a, b in first:
        for c, d in second:
            common = set((a, b)) & set((c, d))
            if len(common) == 1:
                possible.append((a, b, c, d, next(iter(common))))
    
    answers = {x[4] for x in possible}
    if len(answers) == 1:
        print(next(iter(answers)))
        return
    
    for a, b in first:
        seen = set()
        for c, d in second:
            common = set((a, b)) & set((c, d))
            if len(common) == 1:
                seen.add(next(iter(common)))
        if len(seen) > 1:
            print(-1)
            return
    
    for c, d in second:
        seen = set()
        for a, b in first:
            common = set((a, b)) & set((c, d))
            if len(common) == 1:
                seen.add(next(iter(common)))
        if len(seen) > 1:
            print(-1)
            return
    
    print(0)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
