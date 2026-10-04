import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    people = []
    idx = 1
    
    for _ in range(n):
        name = data[idx]
        a = int(data[idx + 1])
        idx += 2
        people.append((a, name))
    
    people.sort()
    
    queue = []
    for i, (a, name) in enumerate(people):
        if a > len(queue):
            print(-1)
            return
        
        height = n - i
        queue.insert(a, (name, height))
    
    for name, height in queue:
        print(name, height)

if __name__ == "__main__":
    main()
