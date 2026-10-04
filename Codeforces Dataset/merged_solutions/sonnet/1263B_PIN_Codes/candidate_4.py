# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    lines = sys.stdin.read().strip().split()
    k = 0
    t = int(lines[k])
    k += 1
    output = []

    for _ in range(t):
        n = int(lines[k])
        k += 1
        pins = []
        seen = set()
        repeated_positions = []

        for i in range(n):
            code = lines[k]
            k += 1
            pins.append(code)
            if code in seen:
                repeated_positions.append(i)
            else:
                seen.add(code)

        total = len(repeated_positions)

        for index in repeated_positions:
            current = pins[index]
            for digit in "0123456789":
                candidate = digit + current[1:]
                if candidate not in seen:
                    pins[index] = candidate
                    seen.add(candidate)
                    break
            else:
                for digit in "0123456789":
                    candidate = current[0] + digit + current[2:]
                    if candidate not in seen:
                        pins[index] = candidate
                        seen.add(candidate)
                        break

        output.append(str(total))
        output.extend(pins)

    sys.stdout.write("\n".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
