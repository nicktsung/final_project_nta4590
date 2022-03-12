import csv

### Takes player data from csv file and splits by era into separate csv files for Tableau
def split_player_data():
    
    player1_data = open('80s_data.csv','w')
    player2_data = open('90s_data.csv','w')
    player3_data = open('00s_data.csv','w')
    player4_data = open('10s_data.csv','w')
    
    writer1 = csv.writer(player1_data)
    writer2 = csv.writer(player2_data)
    writer3 = csv.writer(player3_data)
    writer4 = csv.writer(player4_data)
    
    headers = ['player', 'games_played', 'min', 'pts', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct',
                'ftm', 'fta', 'ft_pct', 'oreb', 'dreb', 'reb', 'ast', 'turnover',
                'stl', 'blk', 'pf', 'era']
    
    writer1.writerow(headers)
    writer2.writerow(headers)
    writer3.writerow(headers)
    writer4.writerow(headers)
    
    file = open('player_data.csv')

    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)
    
    players1 = ['Magic Johnson', 'Larry Bird', 'Kareem Abdul-Jabbar', 'Moses Malone', 'Michael Jordan', 
            'Isiah Thomas', 'Julius Erving', 'Dominique Wilkins', 'James Worthy', 'Kevin McHale']
    players2 = ['Michael Jordan', 'Hakeem Olajuwon', 'David Robinson', 'Karl Malone', 'Scottie Pippen',
                "Shaquille O'Neal", 'Charles Barkley', 'John Stockton', 'Clyde Drexler', 'Shawn Kemp']
    players3 = ['Kobe Bryant', "Shaquille O'Neal", 'Tim Duncan', 'Kevin Garnett', 'Allen Iverson',
                'Lebron James', 'Dwyane Wade', 'Steve Nash', 'Jason Kidd', 'Dirk Nowitzki']
    players4 = ['Lebron James', 'Kevin Durant', 'Stephen Curry', 'Kawhi Leonard', 'James Harden',
                'Russell Westbrook', 'Chris Paul', 'Dwyane Wade', 'Paul George', 'Tim Duncan']

    player1_index = 0
    player2_index = 0
    player3_index = 0
    player4_index = 0

    for row in csvreader:
        if row[-1] == '80s':
            writer1.writerow([players1[player1_index]] + row[1:])
            player1_index += 1    
        elif row[-1] == '90s':
            writer2.writerow([players2[player2_index]] + row[1:])
            player2_index += 1 
        elif row[-1] == '00s':
            writer3.writerow([players3[player3_index]] + row[1:])
            player3_index += 1 
        else:
            writer4.writerow([players4[player4_index]] + row[1:])
            player4_index += 1 
        