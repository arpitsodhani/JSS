import sys


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    legs = []
    pos = 1
    for _ in range(n):
        distance = int(data[pos])
        pos += 1
        heading = data[pos]
        pos += 1
        legs.append((distance, heading))
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
        elif latitude == 0 or latitude == 20000:
            return "NO"
    if latitude != 0:
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(valid_journey(read_input()) + "\n")


if __name__ == "__main__":
    main()
