from get_data import *
from parse_data import *
from sort_data import *
import time, csv

### Fetches player data from API and writes to csv file
def load_player_data():
    
    ### Prepare to write to csv file
    player_data = open('player_data.csv','w')
    
    writer = csv.writer(player_data)
    
    headers = ['player', 'games_played', 'min', 'pts', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct'
                'ftm', 'fta', 'ft_pct', 'oreb', 'dreb', 'reb', 'ast', 'turnover',
                'stl' 'blk', 'pf', 'era']
    
    writer.writerow(headers)
    
    ### Get player_name strings from txt files
    with open("best_players_80s.txt") as f1:
        lines1 = f1.readlines()
        
    with open("best_players_90s.txt") as f2:
        lines2 = f2.readlines()
    
    with open("best_players_00s.txt") as f3:
        lines3 = f3.readlines()
        
    with open("best_players_10s.txt") as f4:
        lines4 = f4.readlines()
    
    ### Fetch data from API    
    era1 = [i for i in range(1979,1990)]
    era2 = [i for i in range(1989,2000)]
    era3 = [i for i in range(1999,2010)]
    era4 = [i for i in range(2009,2020)]
    
    for line in lines1:
        player_data = []
        years_played = 0
        for year in era1:
            player_name = line.rstrip('\n')
            data = get_player_data(player_name,year)
            if len(data['data']) != 0:    
                player_data.append(parse_player_data(data['data'][0]))
                years_played += 1
        writer.writerow([player_name] + [sum(x)/years_played for x in zip(*player_data)] + ['80s'])
        time.sleep(30)
        
    for line in lines2:
        player_data = []
        years_played = 0
        for year in era2:
            player_name = line.rstrip('\n')
            data = get_player_data(player_name,year)
            if len(data['data']) != 0:    
                player_data.append(parse_player_data(data['data'][0]))
                years_played += 1
        writer.writerow([player_name] + [sum(x)/years_played for x in zip(*player_data)] + ['90s'])
        time.sleep(30)
        
    for line in lines3:
        player_data = []
        years_played = 0
        for year in era3:
            player_name = line.rstrip('\n')
            data = get_player_data(player_name,year)
            if len(data['data']) != 0:    
                player_data.append(parse_player_data(data['data'][0]))
                years_played += 1
        writer.writerow([player_name] + [sum(x)/years_played for x in zip(*player_data)] + ['00s'])
        time.sleep(30)

    for line in lines4:
        player_data = []
        years_played = 0
        for year in era4:
            player_name = line.rstrip('\n')
            data = get_player_data(player_name,year)
            if len(data['data']) != 0:    
                player_data.append(parse_player_data(data['data'][0]))
                years_played += 1
        writer.writerow([player_name] + [sum(x)/years_played for x in zip(*player_data)] + ['10s'])
        time.sleep(30)
        