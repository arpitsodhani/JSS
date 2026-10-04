# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def choose_movie(values):
    n = values[0]
    left = 1
    counts = {}
    for language in values[left:left + n]:
        counts[language] = counts.get(language, 0) + 1
    left += n

    m = values[left]
    left += 1
    audio = values[left:left + m]
    left += m
    subtitles = values[left:left + m]

    scores = ((counts.get(audio[i], 0), counts.get(subtitles[i], 0), -i) for i in range(m))
    best = max(scores)
    return str(-best[2] + 1)

def main():
    values = [int(x) for x in sys.stdin.buffer.read().split()]
    sys.stdout.write(choose_movie(values))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
