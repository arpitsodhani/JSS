import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    answers = []
    
    for _ in range(t):
        suneet = [data[idx], data[idx + 1]]
        slavic = [data[idx + 2], data[idx + 3]]
        idx += 4
        
        wins = 0
        for first_suneet in range(2):
            for first_slavic in range(2):
                suneet_score = 0
                slavic_score = 0
                
                if suneet[first_suneet] > slavic[first_slavic]:
                    suneet_score += 1
                elif suneet[first_suneet] < slavic[first_slavic]:
                    slavic_score += 1
                
                second_suneet = 1 - first_suneet
                second_slavic = 1 - first_slavic
                
                if suneet[second_suneet] > slavic[second_slavic]:
                    suneet_score += 1
                elif suneet[second_suneet] < slavic[second_slavic]:
                    slavic_score += 1
                
                if suneet_score > slavic_score:
                    wins += 1
        
        answers.append(str(wins))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
