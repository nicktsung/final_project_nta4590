# final_project_nta4590
NU DE200 Final Project

## Instructions
Run python3 write_csv_file.py first.  
Then run main.py.

### Code
- main.py: Main code file to run
- sort_data.py: Organizes data from player_data.csv into a 2d python list where each instance is an NBA stat and each attribute is a season average across all players
- graph_data.py: Graphs sorted data to visualize how main stats (points, assists, rebounds) changed across each decade
- split_data.py: Splits player_data.csv by era into four csv files
- write_csv_file.py: Starts Python script to fetch data
- load_data.py: Calls functions from get_data.py and parse_data.py to get data from API and write it to player_data.csv
- get_data.py: Gets player_id given player_name string and gets season averages from player_id
- parse_data.py: Formats JSON from API into lists

### Datasets
- player_data.csv: stores deceade averages for all players across all seasons
- 80s_data.csv: same as player_data.csv but only for players from the 80s
- 90s_data.csv: same as player_data.csv but only for players from the 90s
- 00s_data.csv: same as player_data.csv but only for players from the 00s
- 10s_data.csv: same as player_data.csv but only for players from the 10s

### Tableau Sheets
- 80s_visualization.twbx: Tableau sheets with visualizations for 80s data
- 90s_visualization.twbx: Tableau sheets with visualizations for 90s data
- 00s_visualization.twbx: Tableau sheets with visualizations for 00s data
- 10s_visualization.twbx: Tableau sheets with visualizations for 10s data

### Miscellaneous
- How_Mainline_Stats_Changed_in_Each_Era.pdf: Graph showing how main stats (points, assists, rebounds) changed across each decade
- best_players_80s.txt: Player_name strings for best players in 80s
- best_players_90s.txt: Player_name strings for best players in 90s
- best_players_00s.txt: Player_name strings for best players in 00s
- best_players_10s.txt: Player_name strings for best players in 10s
