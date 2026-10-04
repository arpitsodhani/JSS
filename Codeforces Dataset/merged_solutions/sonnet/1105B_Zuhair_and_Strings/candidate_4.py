# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    parts = sys.stdin.buffer.read().split()
    k = int(parts[1])
    s = parts[2]
    best = 0
    current = 0
    previous = None
    for ch in s:
        if ch == previous:
            current += 1
        else:
            if current // k > best:
                best = current // k
            previous = ch
            current = 1
    if current // k > best:
        best = current // k

# CLAUSE: finish_program
    sys.stdout.write(str(best))

if __name__ == "__main__":
    main()
