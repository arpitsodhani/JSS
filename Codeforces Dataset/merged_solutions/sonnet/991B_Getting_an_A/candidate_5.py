import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    grades = list(map(int, data[1:1 + n]))
    return n, grades


# --- clause: redo_count :: (n: int, grades: list[int]) -> int ---
def redo_count(n, grades):
    tally = [0] * 6
    total = 0
    for value in grades:
        tally[value] += 1
        total += value
    done = 0
    grade = 2
    while total * 2 < 9 * n:
        while not tally[grade]:
            grade += 1
        tally[grade] -= 1
        total += 5 - grade
        done += 1
    return done


# --- clause: main :: () -> None ---
def main():
    n, grades = read_input()
    sys.stdout.write(str(redo_count(n, grades)) + "\n")


if __name__ == "__main__":
    main()
