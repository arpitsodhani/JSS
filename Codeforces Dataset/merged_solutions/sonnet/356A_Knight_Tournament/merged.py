import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    fights = []
    for i in range(m):
        fights.append((data[2 + 3 * i], data[3 + 3 * i], data[4 + 3 * i]))
    return n, fights

# Clause run_tournament [Confidence: 1.00]
def run_tournament(n, fights):
    beaten = [0] * (n + 2)
    nxt = list(range(n + 2))
    for left, high, winner in fights:
        spot = left
        while spot <= high:
            while nxt[spot] != spot:
                spot = nxt[spot]
            if spot > high:
                break
            if spot != winner:
                beaten[spot] = winner
                nxt[spot] = spot + 1
                spot += 1
            else:
                spot += 1
    return beaten[1:n + 1]

# Clause main [Confidence: 1.00]
def main():
    n, fights = read_input()
    sys.stdout.write(" ".join(map(str, run_tournament(n, fights))) + "\n")


if __name__ == "__main__":
    main()

