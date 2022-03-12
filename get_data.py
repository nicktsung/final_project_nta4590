import requests, json

### Gets season average stats for player in a particular season and returns JSON
def get_player_data(player,season):
    id = get_player_id(player)
    url = "https://www.balldontlie.io/api/v1/season_averages?season={search_season}&player_ids[]={search_id}".format(search_id = id,search_season=season)
    r = requests.get(url).text
    res = json.loads(r)
    
    return res

### Gets player_id based on player_name from txt files
def get_player_id(player):
    url = "https://www.balldontlie.io/api/v1/players?search={search_player}".format(search_player = player)
    r = requests.get(url).text
    res = json.loads(r)
    
    return res['data'][0]['id']

