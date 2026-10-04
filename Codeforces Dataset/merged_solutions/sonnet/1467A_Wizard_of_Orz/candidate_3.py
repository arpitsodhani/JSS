# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pattern = "9012345678"
    out = []
    for item in data[1:1 + t]:
        n = int(item)
        if n < 3:
            out.append("9" if n == 1 else "98")
        else:
            out.append("98" + "".join(pattern[i % 10] for i in range(n - 2)))

# CLAUSE: finish_program
    print("\n".join(out))

if __name__ == "__main__":
    main()
