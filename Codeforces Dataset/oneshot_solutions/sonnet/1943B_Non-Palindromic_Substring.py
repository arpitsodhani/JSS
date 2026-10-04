import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        q = int(data[idx + 1])
        idx += 2
        
        s = data[idx]
        idx += 1
        
        diff1 = [0] * n
        diff2 = [0] * n
        
        for i in range(1, n):
            diff1[i] = diff1[i - 1] + (s[i] != s[i - 1])
        
        for i in range(2, n):
            diff2[i] = diff2[i - 1] + (s[i] != s[i - 2])
        
        for _ in range(q):
            l = int(data[idx]) - 1
            r = int(data[idx + 1]) - 1
            idx += 2
            
            length = r - l + 1
            
            if diff1[r] - diff1[l] == 0:
                out.append("0")
                continue
            
            total = length * (length + 1) // 2 - 1
            
            if diff2[r] - diff2[l + 1] == 0:
                if length % 2 == 0:
                    bad_sum = (length // 2) * (length // 2 + 1)
                else:
                    x = (length - 1) // 2
                    bad_sum = x * (x + 1) + length
                total -= bad_sum
            else:
                total -= length
            
            out.append(str(total))
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
