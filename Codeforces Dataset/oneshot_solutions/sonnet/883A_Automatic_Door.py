import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n, m, a, d = data[:4]
    clients = data[4:]
    
    events = []
    for i in range(1, n + 1):
        events.append(i * a)
    events.extend(clients)
    events.sort()
    
    opens = 0
    close_time = -1
    
    for t in events:
        if t >= close_time:
            opens += 1
            close_time = t + d
    
    print(opens)

if __name__ == "__main__":
    main()
