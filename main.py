import csv
from sort_data import *
from graph_data import *
from split_data import *

### Takes data from csv file 
file = open('player_data.csv')

csvreader = csv.reader(file)

header = []
header = next(csvreader)

### Separate data by era
stats1 = []
stats2 = []
stats3 = []
stats4 = []

for row in csvreader:
    if row[-1] == '80s':
        stats1.append(row[1:len(row)-1])
    elif row[-1] == '90s':
        stats2.append(row[1:len(row)-1])
    elif row[-1] == '00s':
        stats3.append(row[1:len(row)-1])
    else:
        stats4.append(row[1:len(row)-1])

### Format player data to show all values for each stat
stats1 = sort_player_data(stats1)
stats2 = sort_player_data(stats2)
stats3 = sort_player_data(stats3)
stats4 = sort_player_data(stats4)

### Get average values of each stat
avg_stats1 = [sum(x)/len(stats1) for x in stats1]
avg_stats2 = [sum(x)/len(stats2) for x in stats2]
avg_stats3 = [sum(x)/len(stats3) for x in stats3]
avg_stats4 = [sum(x)/len(stats4) for x in stats4]

### Visualize all main stats (points, assists, rebounds)
stats = [avg_stats1] + [avg_stats2] + [avg_stats3] + [avg_stats4]
graph_main_stats(stats)

### Split player data into separate csv files for Tableau
split_player_data()