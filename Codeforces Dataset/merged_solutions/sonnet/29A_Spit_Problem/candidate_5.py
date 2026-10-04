# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = tuple(map(int, sys.stdin.buffer.read().split()))
    if len(data) == 0:
        return

    n = data[0]
    incoming = set()
    camels = []
    for i in range(n):
        x = data[1 + 2 * i]
        d = data[2 + 2 * i]
        camels.append((x, d))
        incoming.add((x + d, d))

    result = "NO"
    for x, d in camels:
        if d != 0 and (x, -d) in incoming:
            result = "YES"
            break

    print(result)

# CLAUSE: finish_program
main()
