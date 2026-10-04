# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    x = data[1]
    b = data[2]
    y = 0
    if 4 < len(data):
        y = int(data[4])
    value = 0
    for i in range(n):
        xi = ord(x[i]) - 48
        bi = ord(b[i]) - 48
        if bi == 1:
            value ^= xi
        else:
            value ^= xi ^ 1
    sys.stdout.write(str(y ^ value))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
