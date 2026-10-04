import sys

def main():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2
    
    forbidden_count = [0] * (n + 1)  # 1-indexed
    
    for _ in range(m):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        forbidden_count[a] += 1
        forbidden_count[b] += 1
    
    # Find a city with 0 forbidden connections
    hub = -1
    for i in range(1, n + 1):
        if forbidden_count[i] == 0:
            hub = i
            break
    
    # Output
    print(n - 1)
    for i in range(1, n + 1):
        if i != hub:
            print(hub, i)

if __name__ == "__main__":
    main()
