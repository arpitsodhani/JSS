import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause game_total [Confidence: 1.00]
def game_total(n):
    total = 1
    current = n
    while current > 1:
        total += current
        smallest = current
        step = 2
        while step * step <= current:
            if current % step == 0:
                smallest = step
                break
            step += 1
        current = current // smallest
    return total

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(str(game_total(read_input())) + "\n")


if __name__ == "__main__":
    main()

