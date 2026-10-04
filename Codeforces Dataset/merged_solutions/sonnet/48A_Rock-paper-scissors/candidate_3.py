import sys


# --- clause: read_input :: () -> tuple[bytes, bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    first = data[0]
    second = data[1]
    third = data[2]
    return first, second, third


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
    if beats(m, f) and beats(m, s):
        return "M"
    if beats(s, f) and beats(s, m):
        return "S"
    return "?"


# --- clause: main :: () -> None ---
def main():
    f, m, s = read_input()
    print(find_winner(f, m, s))


if __name__ == "__main__":
    main()
