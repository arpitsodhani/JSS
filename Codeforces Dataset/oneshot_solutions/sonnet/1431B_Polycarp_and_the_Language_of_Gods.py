import sys

def solve_string(s):
    result = 0
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == 'v':
            j = i
            while j < n and s[j] == 'v':
                j += 1
            result += (j - i) // 2
            i = j
        else:
            result += 1
            i += 1
    
    return result

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    answers = []
    for i in range(1, t + 1):
        answers.append(str(solve_string(data[i])))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
