import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    
    idx = 1
    for i in range(1, n + 1):
        left[i] = data[idx]
        right[i] = data[idx + 1]
        idx += 2
    
    heads = []
    tails = []
    
    for i in range(1, n + 1):
        if left[i] == 0:
            heads.append(i)
        if right[i] == 0:
            tails.append(i)
    
    for i in range(len(heads) - 1):
        right[tails[i]] = heads[i + 1]
        left[heads[i + 1]] = tails[i]
    
    out = []
    for i in range(1, n + 1):
        out.append(f"{left[i]} {right[i]}")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
