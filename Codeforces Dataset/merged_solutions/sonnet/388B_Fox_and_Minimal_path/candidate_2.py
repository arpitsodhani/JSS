# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_answer(k):
    positions = []
    value = k
    index = 0
    while value:
        if value & 1:
            positions.append(index)
        value >>= 1
        index += 1

    if k == 1:
        return ["2", "NY", "YN"]

    highest = positions[-1]
    size = 2 + 2 * highest
    matrix = [["N"] * size for _ in range(size)]

    def link(a, b):
        matrix[a][b] = "Y"
        matrix[b][a] = "Y"

    groups = [[0]]
    for level in range(1, highest + 1):
        groups.append([2 * level, 2 * level + 1])

    for level in range(highest):
        for left in groups[level]:
            for right in groups[level + 1]:
                link(left, right)

    if positions and positions[0] == 0:
        link(0, 1)

    for bit in positions:
        if bit:
            link(groups[bit][0], 1)

    return [str(size)] + ["".join(row) for row in matrix]

# CLAUSE: finish_program
def main():
    k = int(sys.stdin.readline())
    sys.stdout.write("\n".join(build_answer(k)))

if __name__ == "__main__":
    main()
