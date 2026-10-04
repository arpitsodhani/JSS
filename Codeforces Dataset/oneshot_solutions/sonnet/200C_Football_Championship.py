import sys
from collections import defaultdict

def parse_match(line):
    parts = line.split()
    team1 = parts[0]
    team2 = parts[1]
    score_parts = parts[2].split(':')
    score1 = int(score_parts[0])
    score2 = int(score_parts[1])
    return team1, team2, score1, score2

def compute_standings(matches):
    stats = defaultdict(lambda: {'points': 0, 'scored': 0, 'conceded': 0, 'name': ''})
    
    for team1, team2, score1, score2 in matches:
        stats[team1]['name'] = team1
        stats[team2]['name'] = team2
        
        stats[team1]['scored'] += score1
        stats[team1]['conceded'] += score2
        stats[team2]['scored'] += score2
        stats[team2]['conceded'] += score1
        
        if score1 > score2:
            stats[team1]['points'] += 3
        elif score1 < score2:
            stats[team2]['points'] += 3
        else:
            stats[team1]['points'] += 1
            stats[team2]['points'] += 1
    
    return stats

def rank_teams(stats):
    teams = list(stats.keys())
    
    def compare(team):
        s = stats[team]
        gd = s['scored'] - s['conceded']
        return (-s['points'], -gd, -s['scored'], s['name'])
    
    teams.sort(key=compare)
    return teams

def main():
    input_data = sys.stdin.read().strip()
    lines = input_data.split('\n')
    
    matches = []
    for line in lines:
        team1, team2, score1, score2 = parse_match(line)
        matches.append((team1, team2, score1, score2))
    
    all_teams = set()
    for team1, team2, _, _ in matches:
        all_teams.add(team1)
        all_teams.add(team2)
    
    all_teams.add('BERLAND')
    
    berland_opponents = set()
    for team1, team2, _, _ in matches:
        if team1 == 'BERLAND':
            berland_opponents.add(team2)
        elif team2 == 'BERLAND':
            berland_opponents.add(team1)
    
    remaining_opponent = None
    for team in all_teams:
        if team != 'BERLAND' and team not in berland_opponents:
            remaining_opponent = team
            break
    
    best_result = None
    MAX_GOALS = 100
    
    for conceded in range(MAX_GOALS):
        found = False
        for scored in range(MAX_GOALS):
            test_matches = matches + [('BERLAND', remaining_opponent, scored, conceded)]
            stats = compute_standings(test_matches)
            ranking = rank_teams(stats)
            
            berland_rank = ranking.index('BERLAND')
            
            if berland_rank < 2:
                best_result = (scored, conceded)
                found = True
                break
        
        if found:
            break
    
    if best_result:
        print(f"{best_result[0]}:{best_result[1]}")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()
