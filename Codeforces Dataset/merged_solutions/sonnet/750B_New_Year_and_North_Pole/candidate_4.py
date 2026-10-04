import sys


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    legs = []
    pos = 1
    for _ in range(n):
        legs.append((int(data[pos]), bytes(data[pos + 1])))
        pos += 2
    return legs


# --- clause: valid_journey :: (legs: list[tuple[int, bytes]]) -> str ---
def valid_journey(legs):
    latitude = 0
    for distance, heading in legs:
        if heading == b"South":
            if latitude + distance > 20000:
                return "NO"
            latitude += distance
        elif heading == b"North":
            if latitude - distance < 0:
                return "NO"
            latitude -= distance
        else:
            if latitude == 0 or latitude == 20000:
                return "NO"
    if latitude:
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    legs = read_input()
    sys.stdout.write(valid_journey(legs) + "\n")


if __name__ == "__main__":
    main()
