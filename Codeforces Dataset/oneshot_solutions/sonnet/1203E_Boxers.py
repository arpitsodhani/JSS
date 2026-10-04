import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    weights = data[1:1 + n]
    weights.sort()
    
    used = set()
    
    for w in weights:
        for new_w in (w - 1, w, w + 1):
            if new_w > 0 and new_w not in used:
                used.add(new_w)
                break
    
    print(len(used))

if __name__ == "__main__":
    main()
