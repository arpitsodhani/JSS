# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def make_answer(n, k):
    if n == 1:
        return "\n".join(["1"] * k)
    need = n - 1
    rounds = len(bin(need - 1)) - 2 if need > 1 else 0
    if k < rounds:
        return "-1"
    result = []
    previous = 1
    distances = list(range(n - 1, -1, -1))
    for _ in range(k):
        current = min(need, previous * 2)
        cells = map(lambda d: str(n - (min(d, current) - min(d, previous))), distances)
        result.append(" ".join(cells))
        previous = current
    return "\n".join(result)

# CLAUSE: finish_program
def main():
    raw = sys.stdin.read().strip().split()
    if not raw:
        return
    print(make_answer(int(raw[0]), int(raw[1])), end="")

if __name__ == "__main__":
    main()
