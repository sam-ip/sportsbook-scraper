import csv
import time
from time import strftime, localtime

class Market:
    def __init__(self, sport_league, home_team, away_team, commence_time, market_name, bet_selection_name, odds, timestamp):
        self.market = {}
        self.market["sport_league"] = sport_league
        self.market["home_team"] = home_team
        self.market["away_team"] = away_team
        self.market["commence_time"] = commence_time
        self.market["market_name"] = market_name
        self.market["bet_selection_name"] = bet_selection_name
        self.market["odds"] = odds
        self.market["timestamp"] = timestamp

def get_markets(markets, sport_league, home_team, away_team, commence_time):
    final_markets = []
    time_now = time.time()
    formatted_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time_now))
    for book in markets["bookmakers"]:
        for market in book["markets"]:
            market_name = market["key"]
            for outcome in  market["outcomes"]:
                bet_selection_name = market_name + " " + outcome["name"]
                if market_name != "h2h":
                    bet_selection_name += " " + str(outcome["point"])
                odds = outcome["price"]

                final_markets.append(
                    Market(sport_league, home_team, away_team, commence_time, market_name, bet_selection_name, odds, formatted_time)
                )
    return final_markets
        
def write_to_file(markets):
    file_name = 'final_odds.csv'
    field_names = ['sport_league', 'home_team', 'away_team', 'commence_time', 'market_name', 'bet_selection_name', 'odds', 'timestamp']

    with open(file_name, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
    
        for market in markets:
            writer.writerow(market.market)
    print("Final Odds spreadsheet updated")