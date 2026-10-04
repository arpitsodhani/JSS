# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def choose_three(v):
    return v * (v - 1) * (v - 2) // 6

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    freq = {}
    for i in range(1, 2 * n, 2):
        key = (((data[i] // 2) & 1), ((data[i + 1] // 2) & 1))
        freq[key] = freq.get(key, 0) + 1

    vals = [freq.get((0, 0), 0), freq.get((0, 1), 0), freq.get((1, 0), 0), freq.get((1, 1), 0)]
    bad = vals[0] * vals[1] * vals[2] + vals[0] * vals[1] * vals[3] + vals[0] * vals[2] * vals[3] + vals[1] * vals[2] * vals[3]
    print(choose_three(n) - bad)

# CLAUSE: finish_program
main()
