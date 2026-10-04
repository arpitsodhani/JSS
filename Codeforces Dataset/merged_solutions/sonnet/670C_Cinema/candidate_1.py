# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    scientists = data[idx:idx + n]
    idx += n
    
    m = data[idx]
    idx += 1
    
    audio = data[idx:idx + m]
    idx += m
    
    subtitles = data[idx:idx + m]
    
    known = Counter(scientists)
    
    best_movie = 0
    best_audio = -1
    best_subtitles = -1
    
    for i in range(m):
        pleased = known[audio[i]]
        almost = known[subtitles[i]]
        
        if pleased > best_audio or (pleased == best_audio and almost > best_subtitles):
            best_audio = pleased
            best_subtitles = almost
            best_movie = i
    
    print(best_movie + 1)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
