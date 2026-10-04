import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    position = [0] * (n + 1)
    for i in range(1, n + 1):
        value = data[idx]
        idx += 1
        position[value] = i
    
    m = data[idx]
    idx += 1
    
    vasya = 0
    petya = 0
    for _ in range(m):
        value = data[idx]
        idx += 1
        pos = position[value]
        vasya += pos
        petya += n - pos + 1
    
    print(vasya, petya)

if __name__ == "__main__":
    main()
