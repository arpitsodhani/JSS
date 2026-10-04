import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        notes = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        perfect = True
        for i in range(n - 1):
            interval = abs(notes[i + 1] - notes[i])
            if interval != 5 and interval != 7:
                perfect = False
                break
        
        print("YES" if perfect else "NO")

main()
