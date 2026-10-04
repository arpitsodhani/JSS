# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def pair_type(x, y):
    if x == y:
        return x + y
    return "M"

def flip_pair(pair):
    return pair[1] + pair[0]

def apply_reverse(arr, k):
    arr[:k] = [flip_pair(p) for p in arr[:k][::-1]]

def solve_case(a, b):
    n = len(a)
    m = n // 2
    
    arr = [a[2 * i:2 * i + 2] for i in range(m)]
    target = [b[2 * i:2 * i + 2] for i in range(m)]
    
    count_a = {"00": 0, "11": 0, "M": 0}
    count_b = {"00": 0, "11": 0, "M": 0}
    
    for p in arr:
        count_a[pair_type(p[0], p[1])] += 1
    for p in target:
        count_b[pair_type(p[0], p[1])] += 1
    
    if count_a != count_b:
        return None
    
    ops = []
    
    for pos in range(m - 1, -1, -1):
        if arr[pos] == target[pos]:
            continue
        
        need = pair_type(target[pos][0], target[pos][1])
        chosen = -1
        
        for i in range(pos + 1):
            if pair_type(arr[i][0], arr[i][1]) != need:
                continue
            
            if need != "M":
                chosen = i
                break
            
            if i == 0:
                if flip_pair(arr[i]) == target[pos]:
                    chosen = i
                    break
            else:
                if arr[i] == target[pos]:
                    chosen = i
                    break
        
        if chosen == -1:
            for i in range(pos + 1):
                if pair_type(arr[i][0], arr[i][1]) == need:
                    chosen = i
                    break
            
            ops.append(2)
            apply_reverse(arr, 1)
        
        if chosen != 0:
            ops.append(2 * (chosen + 1))
            apply_reverse(arr, chosen + 1)
        
        ops.append(2 * (pos + 1))
        apply_reverse(arr, pos + 1)
    
    return ops

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        
        ops = solve_case(a, b)
        if ops is None:
            out.append("-1")
        else:
            out.append(str(len(ops)))
            if ops:
                out.append(" ".join(map(str, ops)))
            else:
                out.append("")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
