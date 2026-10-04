# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    result = []
    for _ in range(t):
        n = data[p]
        p += 1
        freq = [0] * (n + 1)
        for _ in range(n):
            end = p + n
            c = 0
            q = end - 1
            while q >= p and data[q] == 1:
                c += 1
                q -= 1
            freq[c] += 1
            p = end
        need = 1
        for c, amount in enumerate(freq):
            while amount and c >= need:
                need += 1
                amount -= 1
        result.append(str(min(need, n)))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
