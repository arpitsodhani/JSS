# CLAUSE: setup_environment
import sys

def run_case(start_positions, movable_string, moves, energy, target):
    positions = start_positions.copy()
    active = set(i for i, ch in enumerate(movable_string) if ch == "1")

# CLAUSE: solve_logic
    for _ in range(moves):
        if not active:
            break

        dancer = min(active, key=positions.__getitem__)
        current = positions[dancer]

        right_side = [positions[j] for j in range(len(positions)) if j != dancer and positions[j] > current]
        if right_side:
            positions[dancer] = min(current + energy, min(right_side) - 1)
        else:
            positions[dancer] = current + energy

        active.remove(dancer)

    return positions[target]

def main():
    data = sys.stdin.buffer.read().decode().split()
    n, m, q = map(int, data[:3])
    a = [int(x) for x in data[3:3 + n]]
    s = data[3 + n]
    at = 4 + n
    out = []

    for _ in range(q):
        d = int(data[at])
        k = int(data[at + 1]) - 1
        at += 2
        out.append(str(run_case(a, s, m, d, k)))

# CLAUSE: finish_program
    print("\n".join(out))

if __name__ == "__main__":
    main()
