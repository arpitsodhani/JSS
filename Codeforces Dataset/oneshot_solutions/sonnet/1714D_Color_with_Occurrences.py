import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    tests = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(tests):
        text = data[idx]
        idx += 1
        
        n = int(data[idx])
        idx += 1
        
        strings = []
        for i in range(n):
            strings.append(data[idx])
            idx += 1
        
        m = len(text)
        intervals = []
        
        for i, s in enumerate(strings):
            length = len(s)
            for start in range(m - length + 1):
                if text.startswith(s, start):
                    intervals.append((start, start + length, i + 1))
        
        covered = 0
        answer = []
        
        while covered < m:
            best_end = covered
            best_interval = None
            
            for start, end, string_id in intervals:
                if start <= covered and end > best_end:
                    best_end = end
                    best_interval = (string_id, start + 1)
            
            if best_interval is None:
                answer = None
                break
            
            answer.append(best_interval)
            covered = best_end
        
        if answer is None:
            out.append("-1")
        else:
            out.append(str(len(answer)))
            for string_id, position in answer:
                out.append(f"{string_id} {position}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
