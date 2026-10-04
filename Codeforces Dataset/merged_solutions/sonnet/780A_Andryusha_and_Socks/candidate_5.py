# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    unmatched = set()
    sizes = []
    for sock in numbers[1:]:
        if sock not in unmatched:
            unmatched.add(sock)
            sizes.append(len(unmatched))
        else:
            unmatched.discard(sock)
    answer = max(sizes) if sizes else 0

# CLAUSE: finish_program
    sys.stdout.write(f"{answer}\n")

if __name__ == "__main__":
    main()
