import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    snacks = data[1:]
    
    ready = [False] * (n + 1)
    need = n
    output = []
    
    for snack in snacks:
        ready[snack] = True
        today = []
        
        while need > 0 and ready[need]:
            today.append(str(need))
            need -= 1
        
        output.append(' '.join(today))
    
    sys.stdout.write('\n'.join(output))

if __name__ == "__main__":
    main()
