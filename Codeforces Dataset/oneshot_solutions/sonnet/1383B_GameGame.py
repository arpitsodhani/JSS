import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = []
        total_xor = 0
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            a.append(x)
            total_xor ^= x
        
        if total_xor == 0:
            answers.append("DRAW")
            continue
        
        bit = total_xor.bit_length() - 1
        ones = 0
        for x in a:
            if (x >> bit) & 1:
                ones += 1
        
        zeros = n - ones
        
        if ones % 4 == 1:
            answers.append("WIN")
        else:
            if zeros % 2 == 1:
                answers.append("WIN")
            else:
                answers.append("LOSE")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
