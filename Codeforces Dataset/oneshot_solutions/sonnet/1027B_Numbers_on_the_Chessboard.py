import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    q = int(data[1])
    
    half = (n * n + 1) // 2
    big = (n + 1) // 2
    small = n // 2
    
    out = []
    idx = 2
    
    for _ in range(q):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        
        same_parity = (x + y) % 2 == 0
        
        if n % 2 == 0:
            before = (x - 1) * small
        else:
            odd_rows = x // 2
            even_rows = (x - 1) // 2
            
            if same_parity:
                before = odd_rows * big + even_rows * small
            else:
                before = odd_rows * small + even_rows * big
        
        if y % 2 == 1:
            inside = (y + 1) // 2
        else:
            inside = y // 2
        
        ans = before + inside
        if not same_parity:
            ans += half
        
        out.append(str(ans))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
