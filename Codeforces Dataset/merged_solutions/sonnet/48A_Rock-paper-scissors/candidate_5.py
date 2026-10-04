import sys


# --- clause: read_input :: () -> tuple[bytes, bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    fyodor = data[0]
    matroskin = data[1]
    sharic = data[2]
    return fyodor, matroskin, sharic


# --- clause: beats :: (attacker: bytes, target: bytes) -> bool ---
def beats(attacker, target):
    if attacker == b"rock":
        return target == b"scissors"
    if attacker == b"scissors":
        return target == b"paper"
    return target == b"rock"


# --- clause: find_winner :: (f: bytes, m: bytes, s: bytes) -> str ---
def find_winner(f, m, s):
    if not beats(f, m) or not beats(f, s):
        if not beats(m, f) or not beats(m, s):
            if not beats(s, f) or not beats(s, m):
                return "?"
            return "S"
        return "M"
    return "F"


# --- clause: main :: () -> None ---
def main():
    f, m, s = read_input()
    answer = find_winner(f, m, s)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
