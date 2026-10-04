import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        bad = 0
        for i in range(1, n + 1):
            x = data[idx]
            idx += 1
            if (x - i) % k != 0:
                bad += 1
        
        if bad == 0:
            answers.append("0")
        elif bad == 2:
            answers.append("1")
        else:
            answers.append("-1")
    
    print("\n".join(answers))

if __name__ == "__main__":
    main()
