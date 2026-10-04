import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        row_odd = 0
        col_parity = [0] * m
        
        for _ in range(n):
            row = data[idx]
            idx += 1
            
            cur = 0
            for j, ch in enumerate(row):
                bit = ord(ch) - 48
                cur ^= bit
                col_parity[j] ^= bit
            
            row_odd += cur
        
        col_odd = sum(col_parity)
        answers.append(str(max(row_odd, col_odd)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
