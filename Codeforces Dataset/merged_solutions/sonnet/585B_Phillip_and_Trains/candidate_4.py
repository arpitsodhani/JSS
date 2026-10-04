# CLAUSE: setup_environment
import sys

def clear_cell(track, row, col, moment, n):
    original = col + 2 * moment
    return original >= n or track[row][original] == "."

def can_escape(track, n, positions, moment):
    if not positions:
        return False
    later = []
    for row, col in positions:
        if col >= n - 1:
            return True
        if not clear_cell(track, row, col, moment, n):
            continue
        step_col = col + 1
        for step_row in (row, row - 1, row + 1):
            if step_row < 0 or step_row > 2:
                continue
            if step_col >= n:
                return True
            if clear_cell(track, step_row, step_col, moment, n) and clear_cell(track, step_row, step_col, moment + 1, n):
                later.append((step_row, step_col))
    return can_escape(track, n, list(set(later)), moment + 1)

def main():
    parts = sys.stdin.read().split()
    i = 0
    cases = int(parts[i])
    i += 1
    result = []

# CLAUSE: solve_logic
    for _ in range(cases):
        n = int(parts[i])
        i += 2
        track = []
        start = []
        for r in range(3):
            line = parts[i]
            i += 1
            for c, ch in enumerate(line):
                if ch == "s":
                    start.append((r, c))
            track.append(line.replace("s", ".") + "." * 25)
        result.append("YES" if can_escape(track, n, start, 0) else "NO")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
