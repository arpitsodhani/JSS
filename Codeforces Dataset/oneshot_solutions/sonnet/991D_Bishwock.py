import sys

def main():
    s = sys.stdin.read().strip()
    
    free_columns = 0
    answer = 0
    
    for c in s:
        if c == '0':
            free_columns += 1
        else:
            answer += free_columns // 3
            free_columns = 0
    
    answer += free_columns // 3
    print(answer)

if __name__ == "__main__":
    main()
