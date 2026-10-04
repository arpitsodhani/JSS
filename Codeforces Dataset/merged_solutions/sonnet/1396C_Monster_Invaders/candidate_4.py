# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    r1 = int(data[1])
    r2 = int(data[2])
    r3 = int(data[3])
    d = int(data[4])
    a = [int(x) for x in data[5:]]

    clear = []
    wound = []
    for x in a:
        clear.append(min(x * r1 + r3, (x + 2) * r1))
        wound.append(min((x + 1) * r1, r2))

    normal = 0
    pending = 10 ** 30

    for clear_cost, wound_cost in zip(clear[:-1], wound[:-1]):
        normal, pending = min(
            normal + clear_cost + d,
            pending + clear_cost + 2 * d,
        ), min(
            normal + wound_cost + 2 * d,
            pending + wound_cost + 2 * d,
        )

    answer = min(
        normal + clear[-1],
        pending + clear[-1] + d,
        normal + wound[-1] + r1,
        pending + wound[-1] + r1 + d,
    )

    sys.stdout.write(f"{answer}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
