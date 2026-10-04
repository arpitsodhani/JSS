import sys


# --- clause: read_input :: () -> tuple[bytes, bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0], data[1], data[2]


# --- clause: beats :: (attacker: bytes, target: bytes) -> bool ---
def beats(attacker, target):
    if attacker == b"rock":
        return target == b"scissors"
    if attacker == b"paper":
        return target == b"rock"
    return target == b"paper"


# --- clause: find_winner :: (f: bytes, m: bytes, s: bytes) -> str ---
def find_winner(f, m, s):
    if beats(f, m) and beats(f, s):
        return "F"
    if beats(m, s) and beats(m, f):
        return "M"
    if beats(s, f) and beats(s, m):
        return "S"
    return "?"


# --- clause: main :: () -> None ---
def main():
    f, m, s = read_input()
    sys.stdout.write(find_winner(f, m, s) + "\n")


if __name__ == "__main__":
    main()
