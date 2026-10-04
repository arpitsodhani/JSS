import sys

def main():
    t = sys.stdin.readline().strip()
    n = len(t)
    
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and t[i] != t[j]:
            j = pi[j - 1]
        if t[i] == t[j]:
            j += 1
        pi[i] = j
    
    border = pi[-1] if n else 0
    while border > 0:
        if border * 2 > n:
            print("YES")
            print(t[:border])
            return
        border = pi[border - 1]
    
    print("NO")

if __name__ == "__main__":
    main()
