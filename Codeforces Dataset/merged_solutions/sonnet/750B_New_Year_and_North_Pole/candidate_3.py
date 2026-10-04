import sys


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    legs = []
    pos = 1
    while len(legs) < n:
        legs.append((int(data[pos]), data[pos + 1]))
        pos += 2
    return legs


# --- clause: valid_journey :: (legs: list[tuple[int, bytes]]) -> str ---
def valid_journey(legs):
    latitude = 0
    shift = {b"South": 1, b"North": -1}
    for distance, heading in legs:
        step = shift.get(heading, 0)
        if step:
            latitude += step * distance
            if latitude < 0 or latitude > 20000:
                return "NO"
            continue
        if latitude == 0 or latitude == 20000:
            return "NO"
    if latitude != 0:
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    print(valid_journey(read_input()))


if __name__ == "__main__":
    main()
