import sys

def solve_case(k, a, b):
    i = 0
    j = 0
    result = []
    
    while i < len(a) or j < len(b):
        if i < len(a) and a[i] == 0:
            result.append(0)
            k += 1
            i += 1
        elif j < len(b) and b[j] == 0:
            result.append(0)
            k += 1
            j += 1
        elif i < len(a) and a[i] <= k:
            result.append(a[i])
            i += 1
        elif j < len(b) and b[j] <= k:
            result.append(b[j])
            j += 1
        else:
            return None
    
    return result

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        k = int(data[idx])
        n = int(data[idx + 1])
        m = int(data[idx + 2])
        idx += 3
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        b = list(map(int, data[idx:idx + m]))
        idx += m
        
        result = solve_case(k, a, b)
        if result is None:
            answers.append("-1")
        else:
            answers.append(" ".join(map(str, result)))
    
    print("\n".join(answers))

if __name__ == "__main__":
    main()
