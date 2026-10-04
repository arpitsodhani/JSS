# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pointer = 1
    lines = []
    for _ in range(t):
        n = int(data[pointer])
        pointer += 1
        current = set(data[pointer:pointer + n])
        pointer += n
        lines.append("YES" if b"67" in current else "NO")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
