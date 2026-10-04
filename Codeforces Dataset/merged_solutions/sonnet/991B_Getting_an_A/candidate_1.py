import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    grades = [int(token) for token in data[1:n + 1]]
    return n, grades


# --- clause: redo_count :: (n: int, grades: list[int]) -> int ---
def redo_count(n, grades):
    grades.sort()
    total = 0
    for value in grades:
        total += value
    done = 0
    index = 0
    while total * 2 < 9 * n:
        total += 5 - grades[index]
        index += 1
        done += 1
    return done


# --- clause: main :: () -> None ---
def main():
    n, grades = read_input()
    sys.stdout.write(str(redo_count(n, grades)) + "\n")


if __name__ == "__main__":
    main()
