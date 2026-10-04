# CLAUSE: setup_environment
import sys
from math import isqrt

# CLAUSE: solve_logic
def is_second_player_win(two):
    x, y = two
    if x > y:
        x, y = y, x
    delta = y - x
    return x == 0 if delta == 0 else x == (delta + isqrt(delta * delta * 5)) // 2

def winner_name(data):
    n = data[0]
    values = data[1:1 + n]
    if n > 2:
        nim = 0
        index = 0
        while index < n:
            nim ^= values[index]
            index += 1
        return "BitAryo" if nim == 0 else "BitLGM"
    if n == 2:
        return "BitAryo" if is_second_player_win(values) else "BitLGM"
    return "BitLGM" if values[0] > 0 else "BitAryo"

# CLAUSE: finish_program
raw = sys.stdin.buffer.read()
if raw.strip():
    sys.stdout.write(winner_name(list(map(int, raw.split()))))
