import datetime

### Takes player data from response JSON and returns data formatted into list
def parse_player_data(data):
    games_played = data['games_played']
    minutes = convert_to_seconds(data['min'])
    pts = data['pts']
    fgm = data['fgm']
    fga = data['fga']
    fg_pct = data['fg_pct']
    fg3m = data['fg3m']
    fg3a = data['fg3a']
    fg3_pct = data['fg3_pct']
    ftm = data['ftm']
    fta = data['ftm']
    ft_pct = data['ft_pct']
    oreb = data['oreb']
    dreb = data['dreb']
    reb = data['reb']
    ast = data['ast']
    turnover = data['turnover']
    stl = data['stl']
    blk = data['blk']
    pf = data['pf']
    
    parsed_data = [games_played, minutes, pts, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct,
                   ftm, fta, ft_pct, oreb, dreb, reb, ast, turnover,
                   stl, blk, pf]

    return process_parsed_data(parsed_data)

### Takes minutes and converts to seconds
def convert_to_seconds(minutes):
    time = datetime.datetime.strptime(minutes, "%M:%S")
    delta = time - datetime.datetime(1900, 1, 1)
    seconds = delta.total_seconds()

    return seconds    

### Takes parsed data and returns a list with any empty responses filtered.
### This accounts for seasons a player was not active.
def process_parsed_data(data):
    for i in range(0,len(data)):
        if data[i] == None:
            data[i] = 0.0
    
    return data