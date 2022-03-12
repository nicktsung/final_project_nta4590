import datetime

### Takes data from all players and returns formatted 2d list of all values for each stat
def sort_player_data(data):
    games_played = []
    minutes = []
    pts = []
    fgm = []
    fga = []
    fg_pct = []
    fg3m = []
    fg3a = []
    fg3_pct = []
    ftm = []
    fta = []
    ft_pct = []
    oreb = []
    dreb = []
    reb = []
    ast = []
    turnover = []
    stl = []
    blk = []
    pf = []
    
    for player in data:
        games_played.append(float(player[0]))
        minutes.append(float(player[1]))
        pts.append(float(player[2]))
        fgm.append(float(player[3]))
        fga.append(float(player[4]))
        fg_pct.append(float(player[5]))
        fg3m.append(float(player[6]))
        fg3a.append(float(player[7]))
        fg3_pct.append(float(player[8]))
        ftm.append(float(player[9]))
        fta.append(float(player[10]))
        ft_pct.append(float(player[11]))
        oreb.append(float(player[12]))
        dreb.append(float(player[13]))
        reb.append(float(player[14]))
        ast.append(float(player[15]))
        turnover.append(float(player[16]))
        stl.append(float(player[17]))
        blk.append(float(player[18]))
        pf.append(float(player[19]))
            
    sorted_data = [games_played, minutes, pts, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct,
                   ftm, fta, ft_pct, oreb, dreb, reb, ast, turnover,
                   stl, blk, pf]
    
    return sorted_data
    
    