import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    boss = [0] * (n + 1)
    documents = []
    
    for _ in range(m):
        event_type = int(data[idx])
        idx += 1
        
        if event_type == 1:
            x = int(data[idx])
            idx += 1
            y = int(data[idx])
            idx += 1
            boss[x] = y
        elif event_type == 2:
            x = int(data[idx])
            idx += 1
            signers = set()
            current = x
            while current != 0:
                signers.add(current)
                current = boss[current]
            documents.append(signers)
        else:  # event_type == 3
            x = int(data[idx])
            idx += 1
            y = int(data[idx])
            idx += 1
            if y <= len(documents) and x in documents[y - 1]:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
