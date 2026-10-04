import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    s = data[idx]
    idx += 1
    
    positions = [[] for _ in range(26)]
    for i, ch in enumerate(s, 1):
        positions[ord(ch) - 97].append(i)
    
    m = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(m):
        t = data[idx]
        idx += 1
        
        need = [0] * 26
        result = 0
        
        for ch in t:
            c = ord(ch) - 97
            need[c] += 1
            result = max(result, positions[c][need[c] - 1])
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
