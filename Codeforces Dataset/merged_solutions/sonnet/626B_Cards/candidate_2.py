import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()


# --- clause: possible_colors :: (deck: str) -> str ---
def possible_colors(deck):
    tally = [deck.count("B"), deck.count("G"), deck.count("R")]
    names = "BGR"
    zeros = [i for i in range(3) if tally[i] == 0]
    if len(zeros) == 2:
        for i in range(3):
            if tally[i]:
                return names[i]
    if len(zeros) == 1:
        gap = zeros[0]
        ones = [i for i in range(3) if i != gap and tally[i] == 1]
        if len(ones) == 2:
            return names[gap]
        if len(ones) == 1:
            return "".join(names[i] for i in sorted(ones + [gap]))
    return "BGR"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(possible_colors(read_input()) + "\n")


if __name__ == "__main__":
    main()
