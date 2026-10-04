# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def is_good(x):
    while x:
        if x % 3 == 2:
            return False
        x //= 3
    return True

def next_good(n):
    while not is_good(n):
        n += 1
    return n

def main():
    values = sys.stdin.buffer.read().split()
    q = int(values[0])
    result = []
    for item in values[1:q + 1]:
        result.append(str(next_good(int(item))))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
