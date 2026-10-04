import sys


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    legs = []
    for i in range(n):
        legs.append((int(data[2 * i + 1]), data[2 * i + 2]))
    return legs


# --- clause: valid_journey :: (legs: list[tuple[int, bytes]]) -> str ---
def valid_journey(legs):
    latitude = 0
    for distance, heading in legs:
        if heading == b"North":
            latitude -= distance
            if latitude < 0:
                return "NO"
        elif heading == b"South":
            latitude += distance
            if latitude > 20000:
                return "NO"
        else:
            if latitude in (0, 20000):
                return "NO"
    if latitude != 0:
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%s\n" % valid_journey(read_input()))


if __name__ == "__main__":
    main()
