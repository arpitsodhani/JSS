# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    tests = int(raw[0])
    at = 1
    result = []
    for _ in range(tests):
        n = int(raw[at])
        at += 1
        arr = raw[at:at + n]
        at += n
        arr.sort()
        longest = 1
        run = 1
        for j in range(1, n):
            if arr[j] == arr[j - 1]:
                run += 1
            else:
                if run > longest:
                    longest = run
                run = 1
        if run > longest:
            longest = run
        moves = 0
        while longest < n:
            remaining = n - longest
            if longest < remaining:
                moves += longest + 1
                longest *= 2
            else:
                moves += remaining + 1
                longest = n
        result.append(str(moves))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
