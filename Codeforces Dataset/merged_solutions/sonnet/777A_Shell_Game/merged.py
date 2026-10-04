import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause start_shell [Confidence: 1.00]
def start_shell(n, x):
    for guess in range(3):
        place = guess
        for move in range(n % 6):
            if move % 2 == 0:
                if place == 0:
                    place = 1
                elif place == 1:
                    place = 0
            else:
                if place == 1:
                    place = 2
                elif place == 2:
                    place = 1
        if place == x:
            return guess
    return 0

# Clause main [Confidence: 1.00]
def main():
    n, x = read_input()
    sys.stdout.write("%d\n" % start_shell(n, x))


if __name__ == "__main__":
    main()

