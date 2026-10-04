# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = [0] * (n + 1)

    idx = 1
    for i in range(1, n + 1):
        pos[data[idx]] = i
        idx += 1

    m = data[idx]
    idx += 1

    vasya = 0
    petya = 0

    for _ in range(m):
        p = pos[data[idx]]
        vasya += p
        petya += n - p + 1
        idx += 1

    print(vasya, petya)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
