# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    parts = sys.stdin.buffer.read().split()
    n = int(parts[0])
    answer = 0
    best_time = 10 ** 40
    idx = 0
    while idx < n:
        current = int(parts[idx + 1])
        if current <= idx:
            candidate = idx
        else:
            full_rounds, extra = divmod(current - idx, n)
            candidate = idx + full_rounds * n
            if extra:
                candidate += n
        if candidate < best_time:
            best_time = candidate
            answer = idx
        idx += 1
    sys.stdout.write(f"{answer + 1}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
