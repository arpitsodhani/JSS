# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    n = data[p]
    p += 1
    scientists = data[p:p + n]
    p += n
    m = data[p]
    p += 1
    audio = data[p:p + m]
    p += m
    subtitles = data[p:p + m]

    known = Counter(scientists)
    answer = 1
    best_audio = -1
    best_subtitles = -1

    for i in range(m):
        current_audio = known[audio[i]]
        current_subtitles = known[subtitles[i]]
        if current_audio > best_audio or (current_audio == best_audio and current_subtitles > best_subtitles):
            best_audio = current_audio
            best_subtitles = current_subtitles
            answer = i + 1

    sys.stdout.write(str(answer))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


