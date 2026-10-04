import sys


# --- clause: read_input :: () -> tuple[bytes, bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    first, second, third = data[0], data[1], data[2]
    return first, second, third


# --- clause: beats :: (attacker: bytes, target: bytes) -> bool ---
def beats(attacker, target):
    if attacker == b"rock":
        return target == b"scissors"
    elif attacker == b"scissors":
        return target == b"paper"
    else:
        return target == b"rock"


# --- clause: find_winner :: (f: bytes, m: bytes, s: bytes) -> str ---
def find_winner(f, m, s):
    if beats(f, s) and beats(f, m):
        return "F"
    if beats(m, s) and beats(m, f):
        return "M"
    if beats(s, m) and beats(s, f):
        return "S"
    return "?"


# --- clause: main :: () -> None ---
def main():
    f, m, s = read_input()
    sys.stdout.write("%s\n" % find_winner(f, m, s))


if __name__ == "__main__":
    main()
