# CLAUSE: setup_environment
import sys

MODULO = 32768

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    nums = data[1:n + 1]

    dist = [99] * MODULO
    dist[0] = 0
    layer = [0]
    depth = 0

    while layer:
        depth += 1
        next_layer = []
        for value in layer:
            candidate = (value - 1) % MODULO
            if dist[candidate] == 99:
                dist[candidate] = depth
                next_layer.append(candidate)

            if value & 1 == 0:
                candidate = value >> 1
                if dist[candidate] == 99:
                    dist[candidate] = depth
                    next_layer.append(candidate)

                candidate += MODULO >> 1
                if dist[candidate] == 99:
                    dist[candidate] = depth
                    next_layer.append(candidate)

        layer = next_layer

    out = [str(dist[item]) for item in nums]
    sys.stdout.write(" ".join(out))

# CLAUSE: finish_program
main()
