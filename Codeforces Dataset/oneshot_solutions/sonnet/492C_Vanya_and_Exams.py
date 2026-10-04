import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    r = int(data[idx])
    idx += 1
    avg = int(data[idx])
    idx += 1
    
    exams = []
    for i in range(n):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        exams.append((a, b))
    
    current_total = sum(a for a, b in exams)
    required_total = n * avg
    
    if current_total >= required_total:
        print(0)
        return
    
    need = required_total - current_total
    
    # Sort by essays per point (b_i)
    exams.sort(key=lambda x: x[1])
    
    essays = 0
    for a, b in exams:
        can_add = r - a
        add = min(can_add, need)
        essays += add * b
        need -= add
        if need == 0:
            break
    
    print(essays)

solve()
