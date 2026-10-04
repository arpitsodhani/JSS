# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    result = []
    for _ in range(t):
        n = int(next(tokens))
        ok = any(int(next(tokens)) == 67 for _ in range(n))
        result.append("YES" if ok else "NO")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
