# CLAUSE: setup_environment
import sys

def query(numbers):
    sys.stdout.write("? " + " ".join(str(v) for v in numbers) + "\n")
    sys.stdout.flush()
    value = int(sys.stdin.readline())
    if value == -1:
        sys.exit()
    return value

# CLAUSE: solve_logic
def main():
    lower = (1 << 7) - 1
    upper = lower << 7
    first = query(range(1, 101))
    second = query((i << 7 for i in range(1, 101)))
    answer = (first & upper) | (second & lower)

# CLAUSE: finish_program
    print("! " + str(answer), flush=True)

if __name__ == "__main__":
    main()
