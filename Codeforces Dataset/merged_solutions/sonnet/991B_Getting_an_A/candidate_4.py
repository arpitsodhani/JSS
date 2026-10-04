import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    grades = [int(data[i + 1]) for i in range(n)]
    return n, grades


# --- clause: redo_count :: (n: int, grades: list[int]) -> int ---
def redo_count(n, grades):
    grades.sort()
    total = 0
    for value in grades:
        total += value
    done = 0
    index = 0
    while 2 * total < 9 * n:
        total = total + 5 - grades[index]
        index = index + 1
        done = done + 1
    return done


# --- clause: main :: () -> None ---
def main():
    n, grades = read_input()
    answer = redo_count(n, grades)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
