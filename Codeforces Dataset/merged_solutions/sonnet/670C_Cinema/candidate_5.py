# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    idx = 0

    n = int(tokens[idx])
    idx += 1

    known = {}
    end = idx + n
    while idx < end:
        lang = int(tokens[idx])
        known[lang] = known.get(lang, 0) + 1
        idx += 1

    m = int(tokens[idx])
    idx += 1

    audio = [int(x) for x in tokens[idx:idx + m]]
    idx += m

    best_movie = 1
    best_audio = -1
    best_subtitles = -1

    for movie, sub_token in zip(range(1, m + 1), tokens[idx:idx + m]):
        audio_count = known.get(audio[movie - 1], 0)
        subtitle_count = known.get(int(sub_token), 0)
        if audio_count > best_audio:
            best_audio = audio_count
            best_subtitles = subtitle_count
            best_movie = movie
        elif audio_count == best_audio and subtitle_count > best_subtitles:
            best_subtitles = subtitle_count
            best_movie = movie

    print(best_movie)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
