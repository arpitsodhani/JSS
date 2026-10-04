import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    
    screen = []
    shown = set()
    
    for i in range(n):
        friend = int(data[i + 2])
        
        if friend in shown:
            continue
        
        if len(screen) == k:
            removed = screen.pop()
            shown.remove(removed)
        
        screen.insert(0, friend)
        shown.add(friend)
    
    print(len(screen))
    print(' '.join(map(str, screen)))

if __name__ == "__main__":
    main()
