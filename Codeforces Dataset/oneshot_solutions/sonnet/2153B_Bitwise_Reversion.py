import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    t = data[0]
    idx = 1
    answers = []
    
    for _ in range(t):
        x = data[idx]
        y = data[idx + 1]
        z = data[idx + 2]
        idx += 3
        
        pair_bits = (x & y) | (y & z) | (x & z)
        all_bits = x & y & z
        
        answers.append("YES" if pair_bits == all_bits else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
