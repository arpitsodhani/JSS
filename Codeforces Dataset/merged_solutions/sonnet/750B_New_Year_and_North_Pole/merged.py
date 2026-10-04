import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    legs = []
    pos = 1
    for _ in range(n):
        legs.append((int(data[pos]), data[pos + 1]))
        pos += 2
    return legs

# Clause valid_journey [Confidence: 1.00]
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
    if latitude != 0:
        return "NO"
    return "YES"

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(valid_journey(read_input()) + "\n")


if __name__ == "__main__":
    main()

