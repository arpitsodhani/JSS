import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    
    blocks = []
    for x in a:
        blocks.append([x, 1])
        
        while len(blocks) >= 2:
            s1, c1 = blocks[-2]
            s2, c2 = blocks[-1]
            if s1 * c2 <= s2 * c1:
                break
            
            blocks.pop()
            blocks.pop()
            blocks.append([s1 + s2, c1 + c2])
    
    out = []
    for total, count in blocks:
        value = total / count
        for _ in range(count):
            out.append(f"{value:.9f}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
