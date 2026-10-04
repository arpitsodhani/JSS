# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    values = data[1:]
    half = n // 2
    
    for i in range(half):
        if values[i] == values[i + half]:
            print(i + 1)
            return
    
    print(-1)

if __name__ == "__main__":
    main()


# Clause finish_program [Confidence: 0.40]
def main():
    content = sys.stdin.buffer.read()
    if not content.strip():
        return
    data = list(map(int, content.split()))
    sys.stdout.write(str(first_same_across(data[0], data[1:])))

if __name__ == "__main__":
    main()


