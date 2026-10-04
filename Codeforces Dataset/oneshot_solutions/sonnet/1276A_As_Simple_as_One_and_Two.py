import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    out = []
    for case in range(1, t + 1):
        s = data[case]
        n = len(s)
        positions = []
        
        i = 0
        while i < n:
            if i + 4 < n and s[i:i + 5] == "twone":
                positions.append(i + 3)
                i += 5
            elif i + 2 < n and (s[i:i + 3] == "one" or s[i:i + 3] == "two"):
                positions.append(i + 2)
                i += 3
            else:
                i += 1
        
        out.append(str(len(positions)))
        out.append(" ".join(map(str, positions)))
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
